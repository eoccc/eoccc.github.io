# 服务器

服务器是 Mindustry 的重要组成部分，它让人们能够一起游玩。服务器主要分为两类：专用服务器与本地局域网服务器。

## 专用服务器

专用服务器是独立运行、无图形界面的游戏版本，只专注于提供多人游戏服务。它们通常作为独立程序在电脑上运行，而非在游戏内开启，并通过终端操作。相比本地局域网服务器，专用服务器通常更强，因为可用资源更多，能支持两三人以上同时游玩，且可 24 小时运行。它还提供大量命令，让管理员拥有更强的控制力，也能方便地按需加载模组。

你可以通过「开始游戏」菜单下的「加入游戏」按钮连接。与本地局域网服务器不同，你需要手动输入主机的 IP 地址与端口。另外，一旦添加了服务器，它就会自动出现在你的服务器列表中，游戏也会自动检测其状态。

要搭建专用服务器，**强烈**建议使用一台专门的 Linux 或 Windows 机器。

- 如果尚未安装，请先安装 Java。

- 从 [itch.io](https://anuke.itch.io/mindustry) 或 [Github releases](https://github.com/Anuken/Mindustry/releases) 下载所需的服务器版本。文件名应为 `server.jar` 或 `server-release.jar`；不过在 Windows 上可能只显示为 `server` 或 `server-release`。

- 把服务器文件移动到目标文件夹。建议放在桌面上的一个新目录中。

- 打开新的终端窗口（Windows 上为 CMD）。使用 "[cd](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands/)" 命令进入你放置服务器文件的目录，例如先 `cd Desktop` 再 `cd Server`。运行 `java -jar [server].jar`，其中 [server] 替换为你的服务器文件名。

- 服务器应能启动。输入 `help` 可查看全部控制台命令。如果出现类似 "Unable to access file server.jar" 的提示，通常说明你所在的目录不对。

- 使用 `host  [mode]` 命令开始主持地图。

- 如果你在 Windows 上运行服务器，请自行搜索如何为 Windows 防火墙添加规则——防火墙多数情况下会拦截所需端口。请确保放行 **6567 端口的 TCP 与 UDP**。

- 要关闭服务器，可关闭终端窗口，或在终端窗口中按 Ctrl+C。

除非你已启用端口映射，否则专用服务器只能被局域网内的客户端连接。若想让服务器对外网开放，请继续阅读下文。

### 什么是 IP？如何查看自己的 IP？

简单来说，IP 地址是标识你计算机在互联网上位置的一串数字。只要知道对方的 IP 地址，你就能连接到他的 Mindustry 服务器。地址分为两种：**公网**地址与**本地**地址。

- 对于**本地 IP**，比如你想和与自己同一网络的朋友联机时，每台设备显示它的方式都不一样。你可以搜索自己设备的做法，例如“在 Mac 上查找本地 IP”。

- 若需要**公网 IP**，直接搜索「what is my ip」即可。

### 在家中运行专用服务器

大多数时候，这是你应该记住的：**如果你在家里开服，永远不要把公网 IP 分享给公众，除非你明白这样做的后果！** 你的公网 IP 与你的家庭绑定，一旦落入他人之手，就可能为你的网络带来漏洞与危险。**务必谨慎、做好调研，并尽可能使用 VPN 或虚拟主机。**

也建议你为公共服务器使用域名或 DNS 服务来掩盖 IP，以便于使用；或者更好的是，使用云服务（如 Amazon AWS），或来自 Linode、DigitalOcean 等主机商的专用服务器/虚拟机，那样安全得多。**做好调研**，并确定哪种方案最符合你的需求。

- 找到你路由器的品牌与型号，通常印在路由器底部或背面的标签上。

- 用你常用的搜索引擎搜索“port forward ASUS RT-ACRH17”，并参照指南转发 **6567 端口的 TCP 与 UDP**。每台路由器的操作都不同，所以务必仔细阅读你的指南！

- 你可以使用诸如 [You Get Signal](https://www.yougetsignal.com/tools/open-ports/) 之类的服务，来检查你的端口转发是否设置正确。

## 局域网与 Steam 服务器

本地局域网或 Steam 服务器是内置于游戏中的服务器，可通过游戏内菜单的“主持多人游戏”按钮启动。它设计得简单直接，适用于局域网网络（即你家里的 WiFi 网络）中少数几名玩家之间的对局。它并不真正适合多名玩家，因为那样会占用设备越来越多的资源；那种场景你需要上面提到的专用服务器。它只能在游戏打开时运行，游戏关闭时会立即终止。

你可以用“游玩”菜单下的“加入游戏”按钮连接到它。与专用服务器不同，你的设备会自动找到主机设备，通常无需手动输入主机的 IP 地址就会出现在服务器列表中。

## 专用服务器命令

- `help [command]`：*显示命令列表，或获取特定命令的帮助。*

- `version`：*显示服务器版本信息。*

- `exit`: *退出服务器程序。*

- `stop`: *停止托管服务器。*

- `host [mapname] [mode]`：*打开服务器。未指定时默认为生存模式与随机地图。*

- `maps [all/custom/default]`：*显示可用地图。默认仅显示自定义地图。*

- `reloadassets`：*从磁盘重新加载所有内容/补丁素材文件。*

- `reloadmaps`：*从磁盘重新加载所有地图。*

- `status`: *显示服务器状态。*

- `mods`: *显示所有已加载的模组。*

- `mod `：*显示已加载插件的信息。*

- `js `: *运行任意 Javascript。*

- `say `：*向所有玩家发送一条消息。*

- `pause `：*暂停或取消暂停游戏。*

- `rules [remove/add] [name] [value...]`：*列出、移除或添加全局规则。无论地图如何都会生效。*

- `dumpsettings`：*打印每一项设置值。便于调试。*

- `fillitems [team]`：*用物品填充核心。*

- `playerlimit [off/somenumber]`：*设置服务器玩家上限。*

- `config [name] [value...]`: *配置服务器设置。*

- `subnet-ban [add/remove] [address]`：*封禁一个子网。这只是拒绝所有以某字符串开头的 IP 的连接。*

- `name-ban [add/remove/clear] [regex]`：*按不区分大小写的正则封禁名称。*

- `whitelist [add/remove] [ID]`：*使用玩家 ID 将其加入或移出白名单。*

- `shuffle [none/all/custom/builtin]`: *设置地图随机模式。*

- `nextmap `：*设置游戏结束后要游玩的下一个地图。会覆盖随机切换。*

- `kick `: *按名称踢出某人。*

- `ban  `: *封禁某人。*

- `bans`：*列出所有被封禁的 IP 与 ID。*

- `unban `：*按 IP 或 ID 完全解封某人。*

- `pardon `：*按 ID 赦免被投票踢出的玩家，并允许其重新加入。*

- `admin  `：*将一名在线用户设为管理员*

- `admins`: *列出所有管理员。*

- `players`：*列出当前在游戏中的所有玩家。*

- `runwave`: *触发下一波。*

- `loadautosave`：*加载上一次自动存档。*

- `load `: *从存档槽加载存档。*

- `save  [embedAssets]`：*将游戏状态保存到某个存档槽。*

- `saves`：*列出存档目录中的所有存档。*

- `gameover`: *强制游戏结束。*

- `info `：*查找玩家信息。可选地检查某玩家使用过的所有名称或 IP。*

- `search `：*搜索使用过某段名字的玩家。*

- `gc`：*触发一次垃圾回收。仅用于测试。*

- `yes`：*运行上一条建议的错误命令。*

- `dos-ban [add/remove] [ip]`：*添加或移除一个 DOS 封禁。*

## 专用服务器配置项

- `name`：*客户端上显示的服务器名称。*

- `desc`：*服务器描述，显示在名称下方。最多 100 个字符。*

- `port`：*用于托管服务的端口。*

- `autoUpdate`：*是否在有新的前沿更新时自动更新并退出。*

- `showConnectMessages`：*是否显示连接/断开连接的消息。*

- `enableVotekick`: *是否启用投票踢人。*

- `startCommands`：*启动时运行的命令。这应该是一个以逗号分隔的列表。*

- `logging`：*是否把所有内容记录到文件。*

- `strict`：*是否开启严格模式——修正位置并阻止重复 UUID。*

- `antiSpam`：*是否自动踢出并限流刷屏者。*

- `interactRateWindow`：*方块交互速率限制窗口，单位为秒。*

- `interactRateLimit`: *方块交互速率限制。*

- `interactRateKick`：*玩家在窗口期内必须交互多少次才会被踢出。*

- `messageRateLimit`：*消息速率限制，单位为秒。0 表示禁用。*

- `messageSpamKick`：*玩家在冷却前必须发送多少条消息才会被踢出。0 表示禁用。*

- `packetSpamLimit`：*3 秒内发送的数据包数量上限，超过将被拉黑并踢出。*

- `uuidChangeLimit`：*在 uuidChangeTimePeriod 指定的时间范围内，一个 IP 在被封禁前可发送的 UUID 变更次数上限。*

- `uuidChangeTimePeriod`：*uuidChangeLimit 配置的时间窗口，单位为小时。*

- `chatSpamLimit`：*2 秒内发送的聊天数据包数量上限，超过将被拉黑并踢出。与速率限制不同。*

- `socketInput`：*允许本地应用通过本地 TCP 套接字控制此服务器。*

- `socketInputPort`：*套接字输入的端口。*

- `socketInputAddress`：*套接字输入的绑定地址。*

- `allowCustomClients`：*是否允许自定义客户端连接。*

- `whitelist`：*是否启用白名单。*

- `motd`：*连接时向玩家显示的消息。*

- `autosave`：*游玩时是否定期保存地图。*

- `autosaveAmount`：*自动存档的最大数量。较旧的会被替换。*

- `autosaveSpacing`：*自动存档之间的间隔（秒）。*

- `debug`: *启用调试日志。*

- `snapshotInterval`：*客户端实体快照间隔，单位为毫秒。*

- `autoPause`：*无人在线时游戏是否应暂停。*

- `roundExtraTime`：*游戏结束后加载新地图前的等待时间，单位为秒。*

- `maxLogLength`：*日志文件的最大大小，单位为字节。*

- `logCommands`：*是否记录玩家命令。*
