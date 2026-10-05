# 环境搭建

本教程带你从零开始，把文档站跑在本地，为后续写作和预览做准备。

## 1. 安装 Python

MkDocs 基于 Python 运行：

Windows / macOS：到 [python.org](https://www.python.org/downloads/) 下载安装包，安装时勾选 **Add Python to PATH**
Linux：`sudo apt install python3 python3-pip`

安装后验证：

```bash
python3 --version
pip3 --version
```

## 2. 安装 MkDocs 与主题

```bash
pip3 install mkdocs mkdocs-material
```

如果系统提示 `externally-managed-environment`（PEP 668 保护），推荐用虚拟环境：

```bash
python3 -m venv ~/docs-venv
~/docs-venv/bin/pip install mkdocs mkdocs-material
# 之后把 mkdocs 替换为 ~/docs-venv/bin/mkdocs 即可
```

## 3. 克隆文档仓库

```bash
git clone https://github.com/eoccc/eoccc.github.io.git
cd eoccc.github.io
```

没有命令行经验？也可以先跳过克隆，用 GitHub 网页端编辑（见[提交与上线流程](../contribute/)）。

克隆完成后，你会看到如下目录结构——其中 `CNAME` 为域名配置，`data/`、`js/`、`css/` 为可维护的站点资源，其余多为构建产物：

<img src="../../ext/svg/repo-layout.svg" alt="文档仓库根目录结构示意图，标注 CNAME 为自定义域名配置、请勿删除" width="880">

### 关于 CNAME 文件

克隆完成后，你会看到仓库根目录有一个名为 `CNAME` 的文件，内容只有一行：

```text
docs.66131466.xyz
```

它是本站的**自定义域名配置**——GitHub Pages 读取该文件后，把仓库对外服务的地址从默认的 `eoccc.github.io` 指向社区域名。当前的正式访问地址是 [docs.66131466.xyz](https://docs.66131466.xyz)。

因此：

- **请勿删除该文件**。一旦删除，GitHub Pages 会失去自定义域名配置，域名解析随即失效，站点将回落到默认域名或无法正常访问，必须重新配置 DNS 才能恢复
- **请勿改动其内容**。多写空格、大小写不一致或补上 `https://` 前缀都属于无效配置
- 该文件由维护者管理，普通的文档贡献**不要**在提交中改动它

> **注意**：`CNAME` 只影响线上访问地址，**不影响**本地预览。执行 `mkdocs serve` 时访问的仍是 `http://127.0.0.1:8000/`，与你是否保留该文件无关。

若你发现站点域名无法访问，请先确认 `CNAME` 是否存在且内容完整，再联系维护者排查 DNS 配置。

## 4. 启动本地预览

```bash
mkdocs serve
```

看到 `Serving on http://127.0.0.1:8000/` 即成功，浏览器打开该地址。此后修改任何页面内容并保存，页面自动刷新。

## 5. 安装 .NET 8 SDK（参与项目开发）

参与社区项目开发（后端服务、工具链等）需要 .NET 8 SDK。**仅撰写文档不需要安装**，可跳过本节。

推荐用微软官方源安装，避免系统自带旧包版本：

```bash
# 导入微软 apt 密钥与软件源（Ubuntu / Debian）
wget -q https://packages.microsoft.com/config/debian/12/packages-microsoft-prod.deb -O /tmp/packages-microsoft-prod.deb
sudo dpkg -i /tmp/packages-microsoft-prod.deb
sudo apt-get update

# 只安装 SDK，不升级系统其他软件包
sudo apt-get install -y --no-install-recommends dotnet-sdk-8.0
```

验证：

```bash
dotnet --list-sdks
dotnet --version
```

### 关于版本号

若机器上同时存在多个 SDK（例如 .NET 9），`dotnet --version` 返回的是**最高版本**，而不是 8.x——这属于正常行为，.NET 允许多个 SDK 并存。要在项目中固定使用 8.x，在项目根目录放置 `global.json`：

```json
{
  "sdk": { "version": "8.0.425", "rollForward": "latestPatch" }
}
```

此时 `dotnet --version` 输出 `8.0.425`。

### 本机环境记录

| 项 | 值 |
|---|---|
| 系统 | Ubuntu 24.04（amd64） |
| 软件源 | packages.microsoft.com/debian/12/prod（bookworm） |
| 安装包 | dotnet-sdk-8.0 |
| SDK 版本 | 8.0.425 |
| 运行时 | Microsoft.NETCore.App 8.0.31、Microsoft.AspNetCore.App 8.0.31 |
| 并存的 SDK | 9.0.315（安装前已存在，本次未改动） |

安装过程只拉取 `dotnet-sdk-8.0` 及其依赖（runtime、targeting-pack、apphost-pack 等），未升级系统其他软件包。

## 常见问题

| 现象 | 原因与解决 |
|---|---|
| mkdocs: command not found | Python Scripts 目录不在 PATH，或用了虚拟环境却没带全路径 |
| pip install 报权限错误 | 加 --user 参数，或改用虚拟环境 |
| 端口 8000 被占用 | mkdocs serve -a 127.0.0.1:8888 换端口 |
| 预览正常但字体/图标缺失 | 检查是否安装了 mkdocs-material 而不是仅有 mkdocs |

环境就绪后，请继续阅读 [Markdown 写作规范](../writing/)。
