#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验并装配 inbox/ 投稿区的投稿。

用法:
    python3 tools/apply_inbox.py --check              # 只校验，不改动任何文件
    python3 tools/apply_inbox.py --check --json       # 校验并输出 JSON 结果
    python3 tools/apply_inbox.py --apply              # 校验通过后装配到 docs/
    python3 tools/apply_inbox.py --apply --dry-run    # 预览将要执行的动作

行为:
  1. 扫描 inbox/ 下每个含 index.json 的投稿文件夹(跳过 _template 与隐藏目录)。
  2. 按规范校验 index.json: 必填字段、id 与文件夹名一致、日期格式、target 合法性、
     files 包含 index.md、status 取值等。
  3. --apply 时把 files 与 assets 装配到 target 对应的 docs/ 目录下,
     并把投稿的 status 标记为 done、记录实际落点。
  4. 输出需要在 mkdocs.yml 中登记的导航片段, 并检查该路径是否已登记。

本工具只做「校验 + 装配」, 不执行构建、不改 mkdocs.yml、不碰 data/site-info.json。
"""

import argparse
import datetime
import json
import os
import re
import shutil
import sys

# ---------------------------------------------------------------- 配置

# 投稿目录名(相对仓库根)
INBOX_DIR = "inbox"

# 跳过扫描的条目: 模板与以 _ / . 开头的目录
SKIP_ENTRIES = {"_template"}

# target 取值 -> 实际落点(相对仓库根)
TARGETS = {
    "wiki/community": "docs/wiki/community",
    "wiki/mindustry": "docs/wiki/mindustry",
    "dev": "docs/dev",
    "faq": "docs/faq",
    "about": "docs/about",
}

# 推荐(默认)target
DEFAULT_TARGET = "wiki/community"

# status 合法取值
STATUS_VALUES = ("draft", "ready", "done")

# 必填字段
REQUIRED_FIELDS = (
    "schema_version", "id", "title", "author", "date",
    "summary", "target", "files", "status",
)

# id 命名规则: 小写字母、数字、连字符; 首尾必须是字母或数字
ID_RE = re.compile(r"^[a-z0-9]([a-z0-9-]*[a-z0-9])?$")

# 投稿目录内不允许覆盖的落点(避免撞上既有栏目)
RESERVED_DEST = {
    "docs/wiki/langs", "docs/wiki/index.md", "docs/wiki/CHANGELOG.md",
    "docs/index.md", "docs/release", "docs/rules",
}

# 单个字段长度上限, 防止把整篇正文塞进 json
MAX_SUMMARY_LEN = 200


class Problem:
    """一条校验问题。"""

    def __init__(self, level, field, message):
        self.level = level      # error | warn
        self.field = field
        self.message = message

    def __str__(self):
        mark = "错误" if self.level == "error" else "警告"
        return "[%s] %s: %s" % (mark, self.field, self.message)


def is_under(path, parent):
    """判断 path 是否位于 parent 目录内(防路径穿越)。"""
    p = os.path.realpath(path)
    par = os.path.realpath(parent)
    return p == par or p.startswith(par + os.sep)


def read_json(path):
    """读取 JSON, 失败时抛出带可读信息的异常。"""
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def validate_meta(meta, folder_name, sub_dir, problems):
    """校验单个投稿的 index.json 内容。"""
    if not isinstance(meta, dict):
        problems.append(Problem("error", "index.json", "顶层必须是 JSON 对象"))
        return

    # ---- 必填字段 ----
    for field in REQUIRED_FIELDS:
        if field not in meta:
            problems.append(Problem("error", field, "缺少必填字段"))
        elif meta[field] in ("", None, [], {}):
            # files 允许为空列表(只有想法的投稿), 其余不允许空值
            if field == "files":
                continue
            problems.append(Problem("error", field, "字段值不能为空"))

    # ---- schema_version ----
    if meta.get("schema_version") not in (None, "1.0"):
        problems.append(Problem(
            "error", "schema_version",
            "当前工具只支持 \"1.0\", 实际为 %r" % (meta.get("schema_version"),)))

    # ---- id 与文件夹名 ----
    sub_id = meta.get("id")
    if isinstance(sub_id, str) and sub_id:
        if sub_id != folder_name:
            problems.append(Problem(
                "error", "id",
                "必须与文件夹名一致: 文件夹为 %r, 字段为 %r" % (folder_name, sub_id)))
        if not ID_RE.match(sub_id):
            problems.append(Problem(
                "error", "id",
                "只允许小写字母、数字与连字符, 且首尾不能是连字符"))

    # ---- date ----
    date = meta.get("date")
    if isinstance(date, str) and date:
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            problems.append(Problem("error", "date", "格式必须为 YYYY-MM-DD, 实际为 %r" % date))

    # ---- summary 长度 ----
    summary = meta.get("summary")
    if isinstance(summary, str) and len(summary) > MAX_SUMMARY_LEN:
        problems.append(Problem(
            "warn", "summary",
            "长度 %d 超过建议上限 %d, 摘要应简短" % (len(summary), MAX_SUMMARY_LEN)))
    if isinstance(summary, str) and "\n" in summary:
        problems.append(Problem("warn", "summary", "摘要不应包含换行"))

    # ---- target ----
    target = meta.get("target")
    if isinstance(target, str) and target and target not in TARGETS:
        problems.append(Problem(
            "error", "target",
            "取值必须是 %s 之一, 实际为 %r" % ("、".join(sorted(TARGETS)), target)))

    # ---- status ----
    status = meta.get("status")
    if isinstance(status, str) and status and status not in STATUS_VALUES:
        problems.append(Problem(
            "error", "status",
            "取值必须是 %s 之一, 实际为 %r" % (" / ".join(STATUS_VALUES), status)))

    # ---- nav / tags / assets / files 类型 ----
    for field in ("nav", "tags", "assets", "files"):
        value = meta.get(field)
        if value is None:
            continue
        if not isinstance(value, list):
            problems.append(Problem("error", field, "必须是数组"))
            continue
        if not all(isinstance(v, str) and v for v in value):
            problems.append(Problem("error", field, "数组元素必须是非空字符串"))

    # ---- files 必须包含 index.md, 且文件真实存在 ----
    files = meta.get("files")
    if isinstance(files, list) and files:
        if "index.md" not in files:
            problems.append(Problem("error", "files", "必须包含 \"index.md\""))
        for rel in files:
            if not isinstance(rel, str) or not rel:
                continue
            candidate = os.path.join(sub_dir, rel)
            if not is_under(candidate, sub_dir):
                problems.append(Problem(
                    "error", "files", "路径越出投稿文件夹: %r" % rel))
            elif not os.path.isfile(candidate):
                problems.append(Problem(
                    "error", "files", "文件不存在: %r" % rel))

    # ---- assets 存在性 ----
    assets = meta.get("assets")
    if isinstance(assets, list):
        for rel in assets:
            if not isinstance(rel, str) or not rel:
                continue
            candidate = os.path.join(sub_dir, rel)
            if not is_under(candidate, sub_dir):
                problems.append(Problem(
                    "error", "assets", "路径越出投稿文件夹: %r" % rel))
            elif not os.path.exists(candidate):
                problems.append(Problem(
                    "error", "assets", "资源不存在: %r" % rel))

    # ---- 正文体检: front matter 与一级标题 ----
    index_md = os.path.join(sub_dir, "index.md")
    if os.path.isfile(index_md):
        check_markdown(index_md, problems)

    # ---- 落点是否撞上保留目录 ----
    if isinstance(target, str) and target in TARGETS and isinstance(sub_id, str) and sub_id:
        dest_rel = os.path.join(TARGETS[target], sub_id)
        if dest_rel in RESERVED_DEST:
            problems.append(Problem(
                "error", "id", "落点 %s 与既有栏目冲突, 请更换 id" % dest_rel))


def check_markdown(path, problems):
    """检查正文的两条硬规则: 无 YAML front matter、只有一个一级标题。"""
    try:
        with open(path, "r", encoding="utf-8") as fh:
            lines = fh.read().splitlines()
    except (OSError, UnicodeDecodeError) as exc:
        problems.append(Problem("error", "index.md", "无法读取: %s" % exc))
        return

    if lines and lines[0].strip() == "---":
        problems.append(Problem(
            "error", "index.md",
            "不要写 YAML front matter(本站未启用 meta 扩展, 会当正文显示), "
            "元数据请只写在 index.json"))

    h1 = [ln for ln in lines if re.match(r"^#\s+\S", ln)]
    if not h1:
        problems.append(Problem("warn", "index.md", "建议以 \"# 标题\" 开头(缺少一级标题)"))
    elif len(h1) > 1:
        problems.append(Problem(
            "error", "index.md",
            "出现 %d 个一级标题, 每页只允许一个" % len(h1)))

    # 跳级检查: 出现 ## 之前不该有 ###
    seen = set()
    for ln in lines:
        m = re.match(r"^(#{1,6})\s+\S", ln)
        if not m:
            continue
        level = len(m.group(1))
        if level > 1 and (level - 1) not in seen and level != 1:
            if level - 1 >= 1 and (level - 1) not in seen:
                problems.append(Problem(
                    "warn", "index.md",
                    "标题层级跳跃: 出现 %s 级标题但缺少 %d 级" % ("#" * level, level - 1)))
        seen.add(level)


def discover(root):
    """扫描投稿区, 返回 [(folder_name, sub_dir, meta_or_None, problems)]。"""
    inbox = os.path.join(root, INBOX_DIR)
    if not os.path.isdir(inbox):
        return None, [Problem("error", INBOX_DIR, "投稿目录不存在")]

    results = []
    for name in sorted(os.listdir(inbox)):
        sub_dir = os.path.join(inbox, name)
        if not os.path.isdir(sub_dir):
            continue
        if name in SKIP_ENTRIES or name.startswith((".", "_")):
            continue

        meta_path = os.path.join(sub_dir, "index.json")
        if not os.path.isfile(meta_path):
            results.append((name, sub_dir, None, [
                Problem("error", "index.json", "投稿缺少索引文件 index.json")]))
            continue

        problems = []
        try:
            meta = read_json(meta_path)
        except json.JSONDecodeError as exc:
            results.append((name, sub_dir, None, [
                Problem("error", "index.json", "JSON 语法错误: %s (行 %d 列 %d)" % (
                    exc.msg, exc.lineno, exc.colno))]))
            continue
        except OSError as exc:
            results.append((name, sub_dir, None, [
                Problem("error", "index.json", "无法读取: %s" % exc)]))
            continue

        validate_meta(meta, name, sub_dir, problems)
        results.append((name, sub_dir, meta, problems))

    return results, []


def nav_registered(root, dest_rel):
    """检查 mkdocs.yml 中是否已登记某个路径。"""
    mkdocs_yml = os.path.join(root, "mkdocs.yml")
    if not os.path.isfile(mkdocs_yml):
        return None
    try:
        with open(mkdocs_yml, "r", encoding="utf-8") as fh:
            content = fh.read()
    except (OSError, UnicodeDecodeError):
        return None
    # 路径以 : 路径 的形式出现在 nav 中
    return dest_rel.replace(os.sep, "/") + "/index.md" in content or \
        dest_rel.replace(os.sep, "/") in content


def nav_snippet(meta):
    """生成建议登记的导航 YAML 片段。"""
    nav = meta.get("nav")
    title = meta.get("title", "")
    if isinstance(nav, list) and nav:
        parts = list(nav)
    else:
        parts = ["Wiki", "社区投稿", title]

    lines = []
    for depth, name in enumerate(parts):
        indent = " " * (4 + depth * 4)
        if depth == len(parts) - 1:
            lines.append("%s- %s: %s" % (indent, name, _dest_nav_path(meta)))
        else:
            lines.append("%s- %s:" % (indent, name))
    return "\n".join(lines)


def _dest_nav_path(meta):
    """投稿装配后的 nav 路径(相对 docs/)。"""
    target = meta.get("target", DEFAULT_TARGET)
    base = TARGETS.get(target, TARGETS[DEFAULT_TARGET])
    return "%s/%s/index.md" % (base.replace("docs/", "", 1), meta.get("id", ""))


def apply_submission(root, folder_name, sub_dir, meta, dry_run=False):
    """把投稿装配到 docs/ 下。返回 (是否成功, 落点相对路径, 信息列表)。"""
    target = meta["target"]
    base = TARGETS[target]
    dest_rel = os.path.join(base, meta["id"])
    dest_abs = os.path.join(root, dest_rel)
    messages = []

    if os.path.exists(dest_abs):
        return False, dest_rel, ["落点已存在: %s (若为重复装配请先手动清理)" % dest_rel]

    if dry_run:
        messages.append("将创建 %s" % dest_rel)
        for rel in meta.get("files", []):
            messages.append("  装配文件 %s" % rel)
        for rel in meta.get("assets", []):
            messages.append("  装配资源 %s" % rel)
        messages.append("  标记 status: done")
        return True, dest_rel, messages

    try:
        os.makedirs(dest_abs, exist_ok=True)
        for rel in meta.get("files", []):
            src = os.path.join(sub_dir, rel)
            dst = os.path.join(dest_abs, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
        for rel in meta.get("assets", []):
            src = os.path.join(sub_dir, rel)
            dst = os.path.join(dest_abs, rel)
            if os.path.isdir(src):
                if os.path.exists(dst):
                    shutil.rmtree(dst)
                shutil.copytree(src, dst)
            else:
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(src, dst)
    except (OSError, shutil.Error) as exc:
        return False, dest_rel, ["装配失败: %s" % exc]

    # 回写投稿状态, 保留原始投稿作为归档
    meta["status"] = "done"
    meta["applied"] = {
        "path": dest_rel.replace(os.sep, "/"),
        "date": datetime.date.today().isoformat(),
    }
    meta_path = os.path.join(sub_dir, "index.json")
    try:
        with open(meta_path, "w", encoding="utf-8") as fh:
            json.dump(meta, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
    except OSError as exc:
        return False, dest_rel, ["装配成功但回写 index.json 失败: %s" % exc]

    messages.append("已装配到 %s" % dest_rel)
    return True, dest_rel, messages


def main():
    ap = argparse.ArgumentParser(
        description="校验并装配 inbox/ 投稿区的投稿",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".", help="仓库根目录(默认当前目录)")
    ap.add_argument("--check", action="store_true", help="只校验, 不改动文件")
    ap.add_argument("--apply", action="store_true", help="校验通过后装配到 docs/")
    ap.add_argument("--dry-run", action="store_true", help="预览将要执行的动作")
    ap.add_argument("--json", action="store_true", help="以 JSON 输出结果")
    ap.add_argument("--all", action="store_true",
                    help="同时处理 status=draft 的投稿(默认跳过)")
    args = ap.parse_args()

    if not args.check and not args.apply:
        ap.error("必须指定 --check 或 --apply 之一")

    root = os.path.abspath(args.root)
    results, fatal = discover(root)

    if fatal:
        for p in fatal:
            print(p, file=sys.stderr)
        return 2

    report = []
    error_count = 0
    ready_count = 0
    skipped_draft = 0
    applied = []

    for folder_name, sub_dir, meta, problems in results:
        entry = {"folder": folder_name, "problems": [str(p) for p in problems],
                 "status": None, "action": None, "dest": None}
        has_error = any(p.level == "error" for p in problems)
        if has_error:
            error_count += 1

        if meta is None:
            entry["action"] = "跳过(索引不可用)"
            report.append(entry)
            continue

        entry["status"] = meta.get("status")
        target = meta.get("target", DEFAULT_TARGET)
        entry["dest"] = os.path.join(TARGETS.get(target, "?"), meta.get("id", "?")) \
            .replace(os.sep, "/")

        if has_error:
            entry["action"] = "跳过(存在校验错误)"
            report.append(entry)
            continue

        if meta.get("status") == "draft" and not args.all:
            skipped_draft += 1
            entry["action"] = "跳过(status=draft)"
            report.append(entry)
            continue

        ready_count += 1
        if args.apply:
            ok, dest_rel, msgs = apply_submission(
                root, folder_name, sub_dir, meta, dry_run=args.dry_run)
            entry["problems"].extend(msgs)
            entry["action"] = ("装配成功" if ok else "装配失败") + \
                ("(dry-run)" if args.dry_run else "")
            if ok and not args.dry_run:
                applied.append(dest_rel)
                reg = nav_registered(root, dest_rel)
                if reg is False:
                    entry["problems"].append(
                        "警告: %s 尚未在 mkdocs.yml 的 nav 中登记" % dest_rel)
                    entry["nav_snippet"] = nav_snippet(meta)
        else:
            entry["action"] = "校验通过, 待装配"
            entry["nav_snippet"] = nav_snippet(meta)
        report.append(entry)

    if args.json:
        print(json.dumps({
            "total": len(results),
            "errors": error_count,
            "ready": ready_count,
            "skipped_draft": skipped_draft,
            "applied": applied,
            "entries": report,
        }, ensure_ascii=False, indent=2))
    else:
        print("投稿区扫描: 共 %d 份投稿" % len(results))
        print("  校验错误 %d 份 / 可装配 %d 份 / 跳过草稿 %d 份"
              % (error_count, ready_count, skipped_draft))
        print("-" * 66)
        for entry in report:
            print("· %s  [%s]  %s" % (
                entry["folder"], entry["status"] or "-", entry["action"]))
            for p in entry["problems"]:
                print("    %s" % p)
            if entry.get("dest"):
                print("    落点: %s" % entry["dest"])
            if entry.get("nav_snippet") and args.apply:
                print("    待登记导航(mkdocs.yml):")
                for line in entry["nav_snippet"].splitlines():
                    print("      %s" % line)
        if args.apply and not args.dry_run and applied:
            print("-" * 66)
            print("已装配 %d 份。后续请手动完成:" % len(applied))
            print("  1. 在 mkdocs.yml 的 nav 中登记上面的导航片段")
            print("  2. 更新 data/site-info.json 的 version 与 updated")
            print("  3. 构建站点并落地产物")
            print("  4. 重新生成 sitemap: python3 tools/gen_sitemap.py "
                  "--root . --base https://docs.66131466.xyz/")

    return 1 if error_count else 0


if __name__ == "__main__":
    sys.exit(main())
