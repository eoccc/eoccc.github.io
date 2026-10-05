# Sitemap 生成与维护

本页说明站点 `sitemap.xml` 的构建方式，以及**新增页面后如何更新 sitemap**。

## 什么是 sitemap

`sitemap.xml` 是提交给搜索引擎（Google、Bing 等）的站点地图，用于告知有哪些页面可供抓取。本站同时输出一份纯文本备选 `sitemap.txt`，每行一个 URL，便于人工核对与部分工具直接读取。

两者都在仓库根目录，构建后由 GitHub Pages 直接发布：

| 文件 | 用途 |
|---|---|
| `sitemap.xml` | 标准站点地图，含 `loc` / `lastmod` / `changefreq` / `priority` |
| `sitemap.txt` | 纯文本 URL 列表，内容与 `sitemap.xml` 完全一致 |

## 生成方式

sitemap 由脚本 `tools/gen_sitemap.py` 扫描站点页面生成，**不使用** MkDocs 的自动 sitemap（自动版本缺少 `changefreq` 与 `priority`，且会把 404 页一并收录）。

```bash
# 在仓库根目录执行：扫描 + 线上校验 + 写出 sitemap.xml / sitemap.txt
python3 tools/gen_sitemap.py --root . --base https://docs.66131466.xyz/

# 仅本地生成、跳过线上校验（离线可用）
python3 tools/gen_sitemap.py --root . --base https://docs.66131466.xyz/ --no-online
```

### 处理流程

1. **扫描页面**：递归查找所有 `index.html`（站点路由为目录形式）与根级 `.html`，保留目录层级以匹配文档路由结构。跳过 `.git`、`assets`、`search`、`css`、`js`、`ext` 等非页面目录，忽略草稿目录与隐藏目录。
2. **提取字段**：
   - `loc`：基准主域名 + 目录路径，拼成完整绝对链接；
   - `lastmod`：取该文件最后一次 git 提交日期（无 git 信息时回退文件修改时间），格式为 `YYYY-MM-DD`；
   - `changefreq` 与 `priority`：按页面类型与层级自动判定，见下表。
3. **线上校验**：对每个 URL 发起**轻量请求**，仅读取响应开头若干字节用于检测 `noindex`，不抓取页面正文、不下载图片资源。
4. **自动过滤**：`4xx` / `5xx` 页面、带 `noindex`（`meta` 或 `X-Robots-Tag`）的页面、草稿页、隐藏页、`404.html` 一律不写入。
5. **去重与转义**：URL 去重后输出，XML 特殊字符（`&`、`<`、`>` 等）按协议转义。
6. 输出前自检条目数、转义与重复情况，任一异常即以非零状态退出。

脚本**不会**自动向任何搜索引擎提交，只生成文件。

### changefreq 与 priority 规则

| 页面类型 | changefreq | priority |
|---|---|---|
| 首页 | daily | 1.0 |
| `release/update/`（完整日志列表） | daily | 0.9 |
| 一级栏目页 | weekly | 0.8 |
| 二级页面 | weekly | 0.7 |
| Wiki 中文版目录级 | weekly | 0.7 |
| Wiki 中文版深层 | monthly | 0.6 |
| Wiki 英文版 | monthly | 0.5 |

## 新增页面后如何更新 sitemap

**新增任何页面后，都需要重新生成 sitemap**，否则新页面不会出现在站点地图中，搜索引擎难以发现。

### 操作步骤

1. 在 `mkdocs.yml` 的 `nav` 中登记新页面（详见 [导航与站点配置](../nav-config/)）。
2. 构建站点并发布，确认新页面线上可访问（返回 HTTP 200）。
3. 回到仓库根目录，重新生成 sitemap：

   ```bash
   python3 tools/gen_sitemap.py --root . --base https://docs.66131466.xyz/
   ```

4. 确认输出中的条目数增加、新页面已包含：

   ```bash
   grep -c "<loc>" sitemap.xml
   grep "你的新页面路径" sitemap.txt
   ```

5. 将更新后的 `sitemap.xml` 与 `sitemap.txt` 一并提交。

### 为什么要先发布再生成

脚本会**在线校验**每个 URL。若页面尚未发布，校验会得到 404，该条目会被自动过滤掉，导致新页面漏收。因此务必先发布、再生成。

若确需在发布前先本地生成，可加 `--no-online` 跳过校验，但**发布后应重新生成一次**。

### 校验缓存

线上校验结果缓存在仓库根的 `.sitemap-cache.json`，重复运行时会命中缓存、避免重复请求。若某页面状态发生变化（例如从 404 修复为 200）却未反映到结果中，删除该缓存文件后重跑即可：

```bash
rm -f .sitemap-cache.json
```

## 常见问题

**新页面没有出现在 sitemap 中？**

依次检查：页面是否已发布（线上返回 200）、是否被 `noindex` 标记、路径是否命中草稿规则、以及是否使用了过期的校验缓存。

**URL 中的 `%20` 为什么变成了 `%2520`？**

Wiki 部分目录名本身含字面 `%20`（来自上游仓库结构），按 URL 编码规范需再编码为 `%25`，因此站点地图中显示为 `Modding%2520Classes`。这是正确的，直接访问 `Modding%20Classes/` 会得到 404。

**能否让 MkDocs 自动生成 sitemap？**

不建议。自动版本缺少 `changefreq` 与 `priority`，且会把 `404.html` 收录进去，与本站的过滤要求不符。
