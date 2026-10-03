# eoccc.github.io

**EveryOne Create Co-Creation Community（人人共创社区）** 的官方文档站，托管于 GitHub Pages，通过自定义域名 [docs.git.eocc.top](https://docs.git.eocc.top) 访问。

## 站点方向与功能

本站点是社区的**公共知识库与协作文档中心**，大体方向包括：

- **社区文档**：社区介绍、组织架构、行为准则与协作规范
- **项目维基**：各共创项目的使用说明、开发指南与 FAQ
- **教程与分享**：成员贡献的经验总结、技术教程与最佳实践

其中**开发者教程**（`dev/`）按开发方式组织，涵盖环境搭建、Markdown 写作规范、提交与上线流程、导航与站点配置，以及 [GitHub 开发与软件包发布流程](dev/github-release-flow/)——从分支开发、评审、构建到 GitHub Release 发布的完整链路。

核心功能：

| 功能 | 说明 |
|---|---|
| 全站搜索 | 基于 MkDocs 内置搜索（lunr），纯前端实现，无需后端 |
| 响应式界面 | Material for MkDocs 主题，桌面 / 移动端自适应 |
| 版本化管理 | 所有内容由 Git 仓库管理，历史可追溯、可回滚 |
| 自动化部署 | 提交 Markdown 源文件后由 MkDocs 构建为纯静态 HTML 发布 |

## 贡献方法

欢迎每一位成员参与共建！所有页面源文件均为 Markdown，位于 `docs/` 目录：

1. **Fork** 本仓库到你的账户下
2. 新建分支，编辑或新增 `docs/*.md` 文件
3. 提交 Pull Request，说明改动内容
4. 经审核合并后，站点会自动更新

本地预览：

```bash
pip install mkdocs mkdocs-material
mkdocs serve   # 本地实时预览 http://127.0.0.1:8000
```

> 注意：`docs/CNAME` 文件为自定义域名配置，**请勿删除**。

## 目录结构

本仓库同时托管 MkDocs 构建产物与独立的静态资源，约定如下：

| 路径 | 用途 | 维护方式 |
|---|---|---|
| `index.html`、`about/`、`dev/`、`release/` | MkDocs 构建产物（页面 HTML） | 由 MkDocs 构建生成，勿手工改动结构 |
| `assets/` | Material 主题自带资源（样式、脚本、搜索 worker） | 随构建更新，勿手动改动 |
| `css/eocc-brand.css` | 站点自定义样式（社区名称渐变等） | 可维护 |
| `img/user/` | **用户头像**等图片资源（预留） | 本地存放、相对路径引用，禁止外链头像 |
| `ext/` | **扩展静态资源**（预留），如 `ext/svg/` 示意图 | 本地存放、相对路径引用，禁止外链 |
| `release/update/` | 版本更新日志子站（含 `releases.json` 与详情 MD） | 独立生成流程，由维护者管理 |
| `search/` | 全站搜索索引（`search_index.json`） | 随构建更新 |

> 资源路径方案（`img/user/` 与 `ext/` 的分工）仍在团队讨论中，各目录内的 `README.md` 记录了当前约定。

## 版权归属

- 文档内容采用 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 许可发布，转载需署名并相同方式共享
- 代码与站点配置部分遵循仓库所在许可
- © EveryOne Create Co-Creation Community（EOCCC）
