#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成兼容 Bing / Google 的 sitemap.xml 与 sitemap.txt。

用法:
    python3 tools/gen_sitemap.py                     # 扫描 + 线上校验 + 写出
    python3 tools/gen_sitemap.py --no-online         # 跳过线上校验(离线)
    python3 tools/gen_sitemap.py --root . --base https://docs.git.eocc.top/

行为:
  1. 扫描内容根目录下所有 index.html(站点路由为目录形式)与根级 .html。
  2. 提取 URL、lastmod(git 提交时间, 无 git 则回退文件 mtime)、changefreq、priority。
  3. 轻量线上校验: 逐个 GET 仅读取响应头部若干字节, 判定 HTTP 状态与 noindex。
  4. 过滤: 4xx/5xx、noindex、草稿、隐藏页、404 页、非页面资源。
  5. 去重后按协议写出 sitemap.xml, 并输出 sitemap.txt 备选。
  6. 不向任何搜索引擎提交, 仅生成文件。

校验结果缓存于 .sitemap-cache.json, 避免重复请求。
"""

import argparse
import concurrent.futures
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from urllib.parse import quote
from xml.sax.saxutils import escape

# ---------------------------------------------------------------- 配置

DEFAULT_BASE = "https://docs.git.eocc.top/"
DEFAULT_ROOT = "."

# 需要整体跳过的目录(相对内容根)
SKIP_DIRS = {
    ".git", ".github", ".atomcode", "node_modules", "assets",
    "search", "css", "js", "img", "ext", "data", "overrides",
    "drafts", "draft", "tmp", "temp", "build", "dist", "site",
}

# 需要跳过的具体文件名
SKIP_FILES = {"404.html"}

# 路径片段命中即视为草稿/隐藏页(不写入 sitemap)
DRAFT_PATTERNS = [
    re.compile(r"(^|/)(draft|drafts|tmp|temp|private|hidden|wip)(/|$)", re.I),
    re.compile(r"\.draft\.", re.I),
]

# 线上校验并发与超时
CHECK_WORKERS = 8
CHECK_TIMEOUT = 12
# 只读取页面开头这么多字节用于检测 meta noindex(位于 <head>)
SNIFF_BYTES = 16384
# 重试次数(网络抖动)
CHECK_RETRIES = 2

CACHE_FILE = ".sitemap-cache.json"

# ---------------------------------------------------------------- 工具


def run_git(args, cwd):
    """执行 git 命令, 失败返回 None。"""
    try:
        out = subprocess.run(
            ["git"] + args, cwd=cwd, capture_output=True, text=True, timeout=30
        )
        if out.returncode != 0:
            return None
        return out.stdout.strip()
    except Exception:
        return None


def git_lastmod_map(root):
    """返回 {相对路径: ISO8601 时间}, 取每个文件最后一次提交时间。"""
    if not os.path.isdir(os.path.join(root, ".git")):
        return {}
    out = run_git(
        ["log", "--pretty=format:@@%cI", "--name-only", "--diff-filter=ACMR"],
        root,
    )
    if not out:
        return {}
    result = {}
    cur = None
    for line in out.splitlines():
        if line.startswith("@@"):
            cur = line[2:].strip()
        elif line.strip() and cur:
            # 同一文件保留最新时间(git log 按时间倒序, 先见者即最新)
            result.setdefault(line.strip(), cur)
    return result


def norm_lastmod(value):
    """规范化为 sitemap 接受的 W3C 日期(YYYY-MM-DD)。"""
    if not value:
        return None
    m = re.match(r"(\d{4}-\d{2}-\d{2})", value)
    return m.group(1) if m else None


def url_for(base, rel_dir):
    """把站点相对目录拼成绝对 URL。

    目录名中可能含字面百分号(例如上游的 `Modding%20Classes` 目录名本身
    就带 `%20`), 按 RFC 3986 需对 `%` 再编码为 `%25`, 因此这里对路径做
    百分号编码, 否则搜索引擎按 `%20` 解码成空格会取到 404。
    """
    base = base if base.endswith("/") else base + "/"
    if rel_dir in ("", "."):
        return base
    path = quote(rel_dir.strip("/"), safe="/")
    return base + path + "/"


def classify(rel_dir):
    """按路径深度/类型给出 changefreq 与 priority。"""
    d = rel_dir.strip("/")
    if d == "":
        return "daily", "1.0"
    parts = d.split("/")
    depth = len(parts)
    if d == "release/update":
        return "daily", "0.9"
    if depth == 1:
        return "weekly", "0.8"
    if d.startswith("wiki/mindustry/en"):
        return "monthly", "0.5"
    if d.startswith("wiki/mindustry/zh") and depth <= 3:
        return "weekly", "0.7"
    if d.startswith("wiki/mindustry"):
        return "monthly", "0.6"
    if depth == 2:
        return "weekly", "0.7"
    return "monthly", "0.6"


def is_draft(rel_dir):
    p = "/" + rel_dir.strip("/") + "/"
    return any(rx.search(p) for rx in DRAFT_PATTERNS)


# ---------------------------------------------------------------- 扫描


def scan_pages(root):
    """扫描内容根, 返回候选页面列表 [{'rel': 相对目录, 'file': 绝对路径}]。"""
    pages = []
    root = os.path.abspath(root)
    for dirpath, dirnames, filenames in os.walk(root):
        # 就地剪枝: 跳过排除目录与隐藏目录
        dirnames[:] = [
            d for d in dirnames
            if d not in SKIP_DIRS and not d.startswith(".")
        ]

        rel_dir = os.path.relpath(dirpath, root)
        if rel_dir == ".":
            rel_dir = ""

        if "index.html" in filenames:
            pages.append({
                "rel": rel_dir,
                "file": os.path.join(dirpath, "index.html"),
            })

        # 根级独立 .html(如 404.html)按需纳入, 由调用方过滤
        if rel_dir == "":
            for fn in filenames:
                if fn.endswith(".html") and fn != "index.html":
                    pages.append({"rel": fn, "file": os.path.join(dirpath, fn)})

    # 排序保证输出稳定
    pages.sort(key=lambda x: x["rel"])
    return pages


# ---------------------------------------------------------------- 线上校验


def sniff_url(url, retries=CHECK_RETRIES):
    """轻量请求: 仅读取页面开头若干字节。

    返回 (status:int|None, noindex:bool, note:str)。
    status 为 None 表示网络失败(超时/连接错误)。
    """
    last_err = ""
    for attempt in range(retries + 1):
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "eocc-sitemap-validator/1.0 (+https://docs.git.eocc.top/)",
                "Accept": "text/html,application/xhtml+xml",
                "Range": "bytes=0-%d" % (SNIFF_BYTES - 1),
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=CHECK_TIMEOUT) as resp:
                status = resp.getcode()
                head = resp.read(SNIFF_BYTES)
                # 显式响应头 noindex
                xrobots = resp.headers.get("X-Robots-Tag", "") or ""
                text = head.decode("utf-8", "ignore")
                noindex = bool(re.search(r"noindex", xrobots, re.I)) or bool(
                    re.search(r'<meta[^>]+name=["\']robots["\'][^>]*noindex', text, re.I)
                )
                return status, noindex, ""
        except urllib.error.HTTPError as e:
            return e.code, False, "HTTP %s" % e.code
        except Exception as e:  # 超时/连接重置等
            last_err = type(e).__name__
            if attempt < retries:
                time.sleep(1.5 * (attempt + 1))
    return None, False, last_err


def load_cache(path):
    if os.path.isfile(path):
        try:
            with open(path, encoding="utf-8") as fh:
                return json.load(fh)
        except Exception:
            return {}
    return {}


def save_cache(path, cache):
    try:
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(cache, fh, ensure_ascii=False, indent=0, sort_keys=True)
    except Exception:
        pass


def check_online(urls, cache_path):
    """并发校验 URL 列表, 返回 {url: {'status':.., 'noindex':.., 'note':..}}。"""
    cache = load_cache(cache_path)
    todo = [u for u in urls if u not in cache]
    if todo:
        print("线上校验 %d 个 URL(并发 %d, 缓存命中 %d)…"
              % (len(todo), CHECK_WORKERS, len(urls) - len(todo)))
        done = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=CHECK_WORKERS) as ex:
            futs = {ex.submit(sniff_url, u): u for u in todo}
            for fut in concurrent.futures.as_completed(futs):
                u = futs[fut]
                status, noindex, note = fut.result()
                cache[u] = {"status": status, "noindex": noindex, "note": note}
                done += 1
                if done % 200 == 0:
                    print("  …已校验 %d/%d" % (done, len(todo)))
                    save_cache(cache_path, cache)
        save_cache(cache_path, cache)
    else:
        print("线上校验: 全部命中缓存(%d 个)" % len(urls))
    return cache


# ---------------------------------------------------------------- 输出


def write_outputs(entries, out_dir, base):
    os.makedirs(out_dir, exist_ok=True)
    xml_path = os.path.join(out_dir, "sitemap.xml")
    txt_path = os.path.join(out_dir, "sitemap.txt")

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for e in entries:
        lines.append("    <url>")
        lines.append("         <loc>%s</loc>" % escape(e["loc"]))
        if e.get("lastmod"):
            lines.append("         <lastmod>%s</lastmod>" % escape(e["lastmod"]))
        lines.append("         <changefreq>%s</changefreq>" % escape(e["changefreq"]))
        lines.append("         <priority>%s</priority>" % escape(e["priority"]))
        lines.append("    </url>")
    lines.append("</urlset>")
    lines.append("")

    with open(xml_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines))

    with open(txt_path, "w", encoding="utf-8", newline="\n") as fh:
        for e in entries:
            fh.write(e["loc"] + "\n")

    return xml_path, txt_path


def main():
    ap = argparse.ArgumentParser(description="生成 sitemap.xml / sitemap.txt")
    ap.add_argument("--root", default=DEFAULT_ROOT, help="内容根目录")
    ap.add_argument("--base", default=DEFAULT_BASE, help="基准主域名")
    ap.add_argument("--out", default=None, help="输出目录(默认同 --root)")
    ap.add_argument("--no-online", action="store_true", help="跳过线上校验")
    ap.add_argument("--cache", default=None, help="校验缓存文件路径")
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    out_dir = os.path.abspath(args.out) if args.out else root
    cache_path = args.cache or os.path.join(root, CACHE_FILE)

    print("内容根: %s" % root)
    print("基准域: %s" % args.base)

    pages = scan_pages(root)
    print("扫描到候选页面: %d" % len(pages))

    lastmod_map = git_lastmod_map(root)
    print("git lastmod 可用文件: %d" % len(lastmod_map))

    # ---- 组装候选 ----
    candidates = []
    seen = set()
    stats = {"skip_file": 0, "skip_draft": 0, "dup": 0}
    for p in pages:
        rel = p["rel"]
        fname = os.path.basename(p["file"])
        if fname in SKIP_FILES:
            stats["skip_file"] += 1
            continue
        if is_draft(rel):
            stats["skip_draft"] += 1
            continue
        loc = url_for(args.base, rel)
        if loc in seen:
            stats["dup"] += 1
            continue
        seen.add(loc)

        rel_file = os.path.relpath(p["file"], root).replace(os.sep, "/")
        lm = norm_lastmod(lastmod_map.get(rel_file))
        if not lm:
            try:
                lm = time.strftime("%Y-%m-%d", time.localtime(os.path.getmtime(p["file"])))
            except Exception:
                lm = None
        freq, prio = classify(rel)
        candidates.append({
            "rel": rel, "loc": loc, "lastmod": lm,
            "changefreq": freq, "priority": prio,
        })

    print("过滤: 排除特定文件 %d, 草稿 %d, 重复 %d" % (
        stats["skip_file"], stats["skip_draft"], stats["dup"]))
    print("待校验: %d" % len(candidates))

    # ---- 线上校验 ----
    dropped = {"http": 0, "noindex": 0, "net": 0}
    if args.no_online:
        print("已跳过线上校验(--no-online)")
    else:
        cache = check_online([c["loc"] for c in candidates], cache_path)
        kept = []
        for c in candidates:
            info = cache.get(c["loc"], {})
            st = info.get("status")
            if st is None:
                dropped["net"] += 1
                print("  [网络失败] %s (%s)" % (c["loc"], info.get("note", "")))
                continue
            if st >= 400:
                dropped["http"] += 1
                continue
            if info.get("noindex"):
                dropped["noindex"] += 1
                continue
            kept.append(c)
        candidates = kept
        print("线上过滤: 4xx/5xx %d, noindex %d, 网络失败 %d" % (
            dropped["http"], dropped["noindex"], dropped["net"]))

    # ---- 输出 ----
    xml_path, txt_path = write_outputs(candidates, out_dir, args.base)
    print("已写出: %s (%d 条)" % (xml_path, len(candidates)))
    print("已写出: %s (%d 条)" % (txt_path, len(candidates)))

    # ---- 简单自检 ----
    with open(xml_path, encoding="utf-8") as fh:
        content = fh.read()
    n_loc = content.count("<loc>")
    if n_loc != len(candidates):
        print("!! 自检失败: loc 数 %d != 条目数 %d" % (n_loc, len(candidates)))
        return 1
    if re.search(r"&(?!(amp|lt|gt|quot|apos);)", content):
        print("!! 自检失败: 存在未转义的 & 字符")
        return 1
    print("自检通过: %d 条, XML 转义正常, 无重复" % n_loc)
    return 0


if __name__ == "__main__":
    sys.exit(main())
