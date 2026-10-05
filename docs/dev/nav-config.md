# 导航与站点配置

本教程面向参与站点结构维护的成员，说明 `mkdocs.yml` 的核心配置：导航折叠菜单与站点元信息。

## 配置文件位置

站点全部配置集中在一个 `mkdocs.yml` 中，改动后本地 `mkdocs serve` 即时可见效果。

## nav：导航与折叠菜单

`nav` 决定侧边栏结构。用缩进即可创建**可折叠的多级分组**，Material 主题自动渲染折叠交互（三条横线菜单点击展开子分支），无需额外样式：

<img src="../../ext/svg/nav-hierarchy.svg" alt="MkDocs 导航层级示意：nav 缩进写法与渲染后侧边栏的对应关系" width="880">

对照关系：缩进一级的分组标题（如「开发者文档」）会渲染为可折叠项，其下再缩进一层的条目即展开后的二级页面。

```yaml
nav:
  - 首页: index.md
  - 版本更新日志: release.md
  - 开发者文档:                # 一级分组（可折叠）
      - 开发者文档 · 总览: dev/index.md
      - 环境搭建: dev/start.md     # 二级页面
      - Markdown 写作规范: dev/writing.md
  - 关于: about.md
```

要点：

**缩进必须用空格**（不能用 Tab），同一层级缩进量一致
分组标题后是冒号，其下每行 `页面名: 路径`
分组可嵌套到三级，但建议不超过两级，避免侧边栏过深
页面文件如果没在 `nav` 登记，仍会被构建，但不会出现在导航中

## 站点元信息

```yaml
site_name: EOCC 文档库                    # 站点名称（浏览器标题、左上角展示）
site_url: https://docs.66131466.xyz/     # 生成站内链接、搜索索引与 sitemap 的基础
site_description: Everyone Create Community
```

规则：

`site_url` 必须是最终访问域名，不要填 github.io 地址
页面 UI 上不展示 github.io 域名；仓库链接需要时用文字 `github.com/eoccc`
`site_name` 改动会影响所有页面的标题与左上角文字

## 主题配置

```yaml
theme:
  name: material
  language: zh
  features:
    - navigation.tabs        # 顶部一级标签
    - navigation.sections    # 侧边栏分组渲染为章节
    - navigation.top         # 返回顶部按钮
    - search.suggest         # 搜索建议
    - content.code.copy      # 代码块复制按钮
```

这些 feature 由 Material 主题提供，保持默认即可；不要自行引入新的前端样式覆盖。

## 自定义样式

如需微调样式，把 CSS 放入 `css/` 目录，并在 `mkdocs.yml` 注册：

```yaml
extra_css:
  - css/eocc-brand.css
```

当前唯一的自定义样式是社区名称渐变（`.eocc-brand`），只作用于该文字，其余保持主题默认。

## 验证与提交

```bash
mkdocs serve   # 本地确认导航、搜索正常
mkdocs build   # 构建无报错再提交
```

确认无误后按 [提交与上线流程](../contribute/) 提交 Pull Request。
