# eoccc.github.io

**EveryOne Create Co-Creation Community（人人共创社区）** 的官方文档站，托管于 GitHub Pages，通过自定义域名 [docs.git.eocc.top](https://docs.git.eocc.top) 访问。

## 站点方向与功能

本站点是社区的**公共知识库与协作文档中心**，大体方向包括：

- **社区文档**：社区介绍、组织架构、行为准则与协作规范
- **项目维基**：各共创项目的使用说明、开发指南与 FAQ
- **教程与分享**：成员贡献的经验总结、技术教程与最佳实践

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

## 版权归属

- 文档内容采用 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 许可发布，转载需署名并相同方式共享
- 代码与站点配置部分遵循仓库所在许可
- © EveryOne Create Co-Creation Community（EOCCC）
