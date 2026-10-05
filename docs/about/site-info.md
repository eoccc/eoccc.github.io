# 站点信息

本站的版本与更新状态一览。

| 项目 | 值 |
|---|---|
| 文档站版本 | <span class="md-sidebar-meta__ver-num">v1.1.0</span> |
| 最后更新 | 2026-10-05 |

## 数据来源

以上数据来自站点数据文件 [`data/site-info.json`](https://github.com/eoccc/eoccc.github.io/blob/main/data/site-info.json)，页面上的版本号即读取该文件，避免多处硬编码导致不一致。

- **版本号**：随文档站的结构性调整递增（语义化版本）
- **最后更新**：取本站最近一次提交日期

## 如何更新

改动方法与时机见[提交与上线流程 · 提交前更新站点版本信息](../../dev/contribute/#site-info)：每次改动更新 `updated`，仅在结构性调整时递增 `version`。

> 页脚与侧边栏显示的版本号与本站点信息同源，均由脚本依据 `data/site-info.json` 回填。
