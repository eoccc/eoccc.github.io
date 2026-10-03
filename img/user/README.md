# img/user/ —— 用户头像目录（预留）

本目录存放**仓库本地**的用户头像资源，供文档页内直接引用。

## 约定

- 一个用户一个文件，文件名用「英文小写 + 连字符」，例如 `kevin-station.png`
- **推荐**把头像存放在本目录内，以相对路径引用；这样不依赖外部服务，图片长期可用、加载稳定
- 也**支持外部头像链接**（如各类 `https://` 头像接口、Gravatar 等），此时直接写完整 URL 即可
- 推荐 SVG 或体积较小的 PNG / WebP；尺寸建议 128 × 128 或 256 × 256
- 引用示例：

  ```html
  <!-- 本地头像（推荐） -->
  <img src="../../img/user/kevin-station.png" alt="Kevin Station" width="48" height="48">

  <!-- 外部头像链接（同样受支持） -->
  <img src="https://example.com/avatar.png" alt="某成员" width="48" height="48">
  ```

> **提示**：外部链接的可用性取决于对方服务，可能因对方限制防盗链、改版或下线而失效；对长期展示的头像，优先使用本地文件。

## 现有资源

| 文件 | 对应成员 | 说明 |
|---|---|---|
| `kevin-station.png` | Kevin Station | 主要开发者头像，取自其 [GitHub 主页](https://github.com/Kevincn2010)，已本地化存储 |

## 相关文档

- 仓库总览与完整目录结构：[`../../README.md`](../../README.md)
- 扩展静态资源目录约定：[`../../ext/README.md`](../../ext/README.md)
- 资源与素材规范（开发者文档）：[GitHub 开发与软件包发布流程](../../dev/github-release-flow/)

> 路径方案（`img/user/` 与 `ext/` 的分工）仍在团队讨论中，本目录按当前约定先行落地，后续如有调整会同步更新本节说明。
