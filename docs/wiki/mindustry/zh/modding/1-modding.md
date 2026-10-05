# 模组开发入门

Mindustry 模组本质上就是一些素材目录。使用模组 API 的方式有很多种，具体取决于你想做什么，以及你愿意为此投入多少精力。

你既可以只是重绘现有游戏内容的精灵图，也可以用更简单的 Json API 创建全新的游戏内容（这也是本文档的主要关注点）。你可以添加自定义音效（或复用现有音效）、把地图加入战役模式，以及添加脚本为模组编写特殊行为，例如自定义特效。

分享模组就像把项目目录交给别人一样简单；只要平台支持，模组就能运行。你最好使用 [GitHub](#github)（*或类似的服务*）来托管源代码。
制作模组，你真正需要的只是一台装有文本编辑器的电脑。

## 编辑

如果你的模组使用 HJSON，建议使用 [Visual Studio Code](https://code.visualstudio.com/) 搭配 [Mindustry HJSON](https://github.com/Anuken/MindustryHJsonVSCode/releases/latest) 扩展。

要安装该扩展，请从链接的发行版页面下载 `mindustry-hjson-x.x.x.vsix`。在 VSCode 中打开「扩展」标签页，点击右上角的三个点 -> 「Install From VSIX...」-> 选择下载好的 VSIX 文件。

该扩展提供自动补全、语法高亮，以及对内容中未知或无效字段的警告。

## 目录结构

你的项目目录大致应如下所示：

```
project
├── mod.hjson
├── content
│   ├── items
│   ├── blocks
│   ├── liquids
│   ├── weather
│   ├── liquids
│   └── units
├── maps
├── bundles
├── sounds
├── schematics
├── scripts
├── sprites-override
└── sprites
```

- `mod.hjson`（必需）你的模组的元数据文件，

- `content/*` 游戏[内容](#content)的目录，

- `maps/` 游戏内地图的目录，

- `bundles/` [语言包](#bundles)的目录，

- `sounds/` [音效](#sound)文件的目录，

- `schematics/` 蓝图文件的目录，

- `scripts/` Javascript 脚本文件的目录，

- `sprites-override/` 用于覆盖游戏内内容的[精灵图](#sprites)目录，

- `sprites/` 你的内容的[精灵图](#sprites)目录，

每个平台的用户应用程序数据目录都不同，你的模组应放入其中：

- Linux: `~/.local/share/Mindustry/mods/`

- Steam: `steam/steamapps/common/Mindustry/saves/mods/`

- Windows: `%appdata%/Mindustry/mods/`

- MacOS: `~/Library/Application Support/Mindustry/mods/`

*注意，文件名应使用小写并以连字符分隔：*

- 正确：`my-custom-block.json`

- 错误：`My Custom Block.json`

## HJSON

Mindustry 使用 [Hjson](https://hjson.github.io/)，它是广为人知的 [JSON ](https://en.wikipedia.org/wiki/JSON) 格式的超集。这意味着任何合法的 JSON 都能使用，同时你还能获得额外的功能：

```
# 单行注释

// 单行注释

/* 多行
   注释 */

key1: "single line string"

key2:
  '''
  multiline
  string
  '''

key3: [
  //字符串的引号和逗号是可选的
  value1
  value2
  value3
]

key4: {
  key1: astring
  key2: 0
}

//与官方 HJSON 规范不同，数组的同一行中允许多个不带引号的字符串

arrayExample: [several, words, that, will, work]
```

如果你不懂上面这些词：序列化语言就是一种为程序编码信息的语言，而*编码（encode）*指的是把信息从一种形式转换为另一种形式，在这里就是把文本转换为 Java 数据结构。

值得一提的是，「官方」HJSON 标准已经废弃，并且存在若干严重缺陷。例如，Mindustry 的 HJSON 解析器使用了略微修改的格式，允许不带引号的多行数组。

## `mod.hjson`

在项目目录的根目录下，你必须有一个 `mod.hjson`，它定义了项目的基本元数据。

```
name: "mod-name"
displayName: "This isn't a mod."
author: Yourself
description: "A short description of your mod."
version: "1.0"
minGameVersion: "160.5"
dependencies: [ ]
hidden: false
```

-   `name` 将用于引用你的模组，因此请谨慎命名。应使用 kebab-case（全小写，空格用 '-' 填充），且不应包含任何颜色格式。
-   `displayName` 将作为 UI 中显示的名称，你可以用它为该名称添加格式。
-   `description` 模组的描述会显示在游戏内的模组管理器中，因此请保持简短扼要。
-   `dependencies` 是可选的，若想了解更多，请参阅[依赖](#dependencies)一节。
-   `minGameVersion` 是游戏的最低构建版本。该值**必须**是大于 136 的数字。
-   `hidden` 表示该模组对多人游戏是否为必需，默认为 false。材质包、JS 插件等应将其设为 true，以免造成服务器与客户端之间的版本不匹配冲突。经验法则是：如果你的模组会创建内容，就不应设为隐藏。

## 内容

在项目目录的根目录下可以有一个 `content/` 目录，所有 JSON/HJSON 数据都放在这里。`content/` 内按内容种类划分了多个子目录；以下是目前常见的几种：

- `content/items/` 用于[物品](#item)，例如 `copper` 和 `surge-alloy`；

- `content/blocks/` 用于[方块](#block)，例如炮塔和地板；

- `content/liquids/` 用于[液体](#liquid)，例如 `water` 和 `slag`；

- `content/units/` 用于飞行或地面[单位](#unittype)，例如 `eclipse` 和 `dagger`；

注意，这些子目录各自需要特定的内容类型。文件名很重要，因为路径的主干名*（不含扩展名的文件名）*会被用来引用该内容。

此外，这些 `content//*` 目录中的文件可以任意嵌套进任何名称的子目录，以便进一步整理，例如：

- `content/items/metals/iron.hjson`，它会相应地创建一个名为 `iron` 的物品。

这些文件的内容大致如下所示：

```
type: TypeOfThing
name: Name Of Thing
description: Description of thing.
# ... more fields here ...
```

| 字段 | 类型 | 备注 |
|---|---|---|
| type | String | 此对象的内容类型。 |
| name | String | 内容的显示名称。 |
| description | String | 内容的显示描述。 |

其余包含的字段将是该类型自身的字段。

顺便提一下，`name` 和 `description` 并非必须写在 json 结构中。你可以用[语言包](#bundles)为任何语言定义它们。不过，如果两者中都没有定义，名称将默认为 `.-.name`，描述则为空。

## 类型

类型拥有众多字段，但重要的是 `type`；这是内容解析器使用的一个特殊字段，它决定你的对象属于哪个类型。*`Router` 类型不可能是 `Turret` 类型*，因为二者完全不同。

类型之间会相互*继承*，因此如果 `MissileBulletType` 继承 `BasicBulletType`，你就能在 `MissileBulletType` 中使用 `BasicBulletType` 的所有字段，如 `damage`、`lifetime` 和 `speed`。字段区分大小写：`hitSize =/= hitsize`。

某个字段的作用取决于具体的类型；有些类型完全不使用自己的字段，主要作为其他类型继承的基类。`Block` 就是这样一个类型。

在这个单位示例中，单位的类型是 `flying`。`bullet` 的类型是 `BulletType`，因此你可以使用 `MissileBulletType`，因为 `MissileBulletType` 继承自 `BulletType`。

其他单位类型包括 `mech`、`legs`、`naval`、`payload`、`tank`、`hover`、`crawl`、`missile` 和 `tether`。

```
type: flying
weapons: [
  {
    bullet: {
      type: MissileBulletType
      damage: 9000
    }
  }
]
```

## 科技树

与 `type` 类似，还有一个名为 `research` 的字段，它可以放在任何内容对象的根部，用于将其放入科技树。

```
research: duo
```

这会把你的方块放在科技树中 `duo` 之后；若要放在自己模组的方块之后，则写你的 ``，仅当使用其他模组的内容时才需要模组名前缀。

研究成本：

| 类型 | 成本 | 备注 |
|---|---|---|
| blocks | `60 * researchCostMultiplier + requirements ^ 1.11 * 20 * researchCostMultiplier` | `researchCostMultiplier` 是可在方块上设置的属性，默认为 `1` |
| units | `requirements * researchCostMultiplier` | 在 `UnitType` 上 `researchCostMultiplier` 默认为 `50` |

随后会根据成本的大小，将其取整到最接近的 10、100、1k 或 100k（取整并不总是向下）。

`requirements` 是方块或单位的成本。单位使用其建造成本/升级成本进行计算。

如果你想设置自定义的研究需求，可以用这个对象代替单纯的名称：

```
research: {
  parent: duo
  requirements: [
    copper/100
  ]
}
```

这可用于覆盖方块或单位的成本，或让资源需要被研究，而不仅仅是生产出来即可。

## 精灵图

制作精灵图只需要一个支持透明通道的图像编辑器*（也就是说：不是画图工具）*。方块精灵图的尺寸应为 `32 * size`，因此 `2x2` 的方块需要 `64x64` 的图像。图像必须是 32 位 RGBA 像素格式的 PNG 文件。
**任何其他像素格式（例如 16 位 RGBA）都可能导致 Mindustry 因「Pixmap decode error」而崩溃。** 你可以使用命令行工具 `file` 来查看精灵图的信息：

```
file sprites/**.png
```

如果其中任何一个不是 32 位 RGBA 格式，请修正它们。

把精灵图直接放进 `sprites/` 子目录即可，内容解析器会递归查找。
图片会被打包进「图集」以提高渲染效率。`sprites/` 下的第一层目录（例如 `sprites/blocks`）决定精灵图进入图集的哪一页。把方块的精灵图放进 `units` 页很可能导致严重卡顿，因此建议参照[原版游戏的组织方式](https://github.com/Anuken/Mindustry/tree/master/core/assets-raw/sprites)。

内容会依据自身名称查找精灵图。`content/blocks/my-hail.json` 的名称为 `my-hail`，同样 `sprites/my-hail.png` 的名称也是 `my-hail`，因此会被该内容使用。

内容可能查找多张精灵图。例如 `my-hail` 是炮塔时，它会查找 `-heat` 后缀，也就是查找 `my-hail-heat`。

你可以在这里找到全部原版精灵图：

- [https://github.com/Anuken/Mindustry/tree/master/core/assets-raw/sprites](https://github.com/Anuken/Mindustry/tree/master/core/assets-raw/sprites)

关于精灵图还有一点需要了解：其中一些会被游戏修改。尤其是炮塔会被加上深灰色边框，因此制作精灵图时必须考虑到这一点，例如在炮塔周围留出透明空间：[Ripple](https://raw.githubusercontent.com/Anuken/Mindustry/master/core/assets-raw/sprites/blocks/turrets/ripple.png)

若要覆盖游戏内内容的精灵图，只需把它们放进 `sprites-override/`。
这会去掉其 id 的 `-` 前缀，从而能够覆盖原版乃至其他模组的精灵图。

## 音效

通过模组系统添加自定义音效，只需把文件放进 `sounds/` 子目录。支持两种格式：`ogg` 与 `mp3`。注意 `mp3` 无法无缝循环，因此尽量使用 `ogg`。

与其他素材一样，引用时使用文件名的主干部分，因此 `pewpew.ogg` 与 `pewpew.mp3` 都可以在 `Sound` 类型字段中通过 `pewpew` 引用。

以下是内置音效列表：

`acceleratorCharge` `acceleratorConstruct` `acceleratorLaunch` `acceleratorLightning1` `acceleratorLightning2` `beamHeal` `beamLustre` `beamMeltdown` `beamParallax` `beamPlasma` `beamPlasmaSmall` `blockBreak1` `blockBreak2` `blockBreak3` `blockExplode1` `blockExplode1Alt` `blockExplode2` `blockExplode2Alt` `blockExplode3` `blockExplodeElectric` `blockExplodeElectricBig` `blockExplodeExplosive` `blockExplodeExplosiveAlt` `blockExplodeFlammable` `blockExplodeWall` `blockHeal` `blockPlace1` `blockPlace2` `blockPlace3` `blockRepair` `blockRotate` `chargeCorvus` `chargeLancer` `chargeVela` `click` `coreLand` `coreLaunch` `door` `drillCharge` `drillImpact` `explosion` `explosionAfflict` `explosionArtillery` `explosionArtilleryShock` `explosionArtilleryShockBig` `explosionCleroi` `explosionCore` `explosionCrawler` `explosionDull` `explosionMissile` `explosionNavanax` `explosionObviate` `explosionPlasmaSmall` `explosionQuad` `explosionReactor` `explosionReactor2` `explosionReactorNeoplasm` `explosionTitan` `healWave` `loopBio` `loopBuild` `loopCircuit` `loopCombustion` `loopConveyor` `loopCultivator` `loopCutter` `loopDifferential` `loopDrill` `loopElectricHum` `loopExtract` `loopFire` `loopFlux` `loopGlow` `loopGrind` `loopHover` `loopHover2` `loopHum` `loopMachine` `loopMachine2` `loopMachineSpin` `loopMalign` `loopMineBeam` `loopMissileTrail` `loopPulse` `loopRegen` `loopShield` `loopSmelter` `loopSpray` `loopSteam` `loopTech` `loopThoriumReactor` `loopThruster` `loopUnitBuilding` `massdriver` `massdriverReceive` `mechStep` `mechStepHeavy` `mechStepSmall` `padLand` `padLaunch` `payloadDrop1` `payloadDrop2` `payloadDrop3` `payloadPickup` `plantBreak` `rain` `rockBreak` `shieldBreak` `shieldBreakSmall` `shieldHit` `shieldWave` `shipMove` `shipMoveBig` `shockBullet` `shockwaveTower` `shoot` `shootAfflict` `shootAlpha` `shootArc` `shootArtillery` `shootArtillerySap` `shootArtillerySapBig` `shootArtillerySmall` `shootAtrax` `shootAvert` `shootBeamPlasma` `shootBeamPlasmaSmall` `shootBreach` `shootBreachCarbide` `shootCleroi` `shootCollaris` `shootConquer` `shootCorvus` `shootCyclone` `shootDiffuse` `shootDisperse` `shootDuo` `shootEclipse` `shootElude` `shootEnergyField` `shootFlame` `shootFlamePlasma` `shootForeshadow` `shootFuse` `shootHorizon` `shootLancer` `shootLaser` `shootLocus` `shootMalign` `shootMeltdown` `shootMerui` `shootMissile` `shootMissileLarge` `shootMissileLong` `shootMissilePlasma` `shootMissilePlasmaShort` `shootMissileShort` `shootMissileSmall` `shootNavanax` `shootOmura` `shootPayload` `shootPulsar` `shootQuad` `shootReign` `shootRetusa` `shootRipple` `shootSalvo` `shootSap` `shootScathe` `shootScatter` `shootScepter` `shootScepterSecondary` `shootSegment` `shootSmite` `shootSpectre` `shootStell` `shootSublimate` `shootTank` `shootToxopidShotgun` `stepMud` `stepWater` `tankMove` `tankMoveHeavy` `tankMoveSmall` `uiBack` `uiButton` `uiChat` `uiFavorite` `uiNotify` `uiUnlock` `unitCreate` `unitCreateBig` `unitExplode1` `unitExplode2` `unitExplode3` `walkerStep` `walkerStepSmall` `walkerStepTiny` `waveSpawn` `wind` `wind2` `wind3` `windHowl` `wreckFall` `wreckFallBig` `none` `unset`

## 依赖

只需在 `mod.json` 中加入其他模组的名称，即可为你的模组添加依赖：

```
dependencies: [
  other-mod-name
  not-a-mod
]
```

依赖名称会转为小写，并把空格替换为 `-` 连字符。例如 `Other MOD NamE` 会变成 `other-mod-name`。

要引用其他模组的素材，必须在素材前加上该模组的名称作为前缀：

- `other-mod-name-not-copper` 会引用 `other-mod-name` 中的 `not-copper`

- `other-mod-name-angry-dagger` 会引用 `other-mod-name` 中的 `angry-dagger`

- `not-a-mod-angry-dagger` 会引用 `not-a-mod` 中的 `angry-dagger`

## 语言包

模组还可以选用「语言包（bundles）」。语言包主要用于提供内容的翻译，但你完全也可以用它处理英文。它们是纯文本文件，放在 `bundles/` 子目录中，命名形如 `bundle_ru.properties`（表示俄语）。

该文件的内容非常简单：

```
block.example-mod-silver-wall.name = Серебряная Стена
block.example-mod-silver-wall.description = Стена из серебра.
```

如果你读过本指南的前几节，一眼就能看懂：

- `.-.name`

- `.-.description`

若要为脚本编写自定义语言包条目，键名可以随你取：

- `message.egg = Eat your eggs`

- `randomline = Random Line`

备注：

- 模组/内容名称会转为小写并以连字符分隔。

内容类型列表：

`item` `block` `bullet` `liquid` `status` `unit` `weather` `sector` `error` `planet` `team` `unitCommand` `unitStance`

各语言对应的语言包后缀列表：

`en` `be` `bg` `ca` `cs` `da` `de` `es` `et` `eu` `fi` `fil` `fr` `hu` `id_ID` `it` `ja` `ko` `lt` `nl` `nl_BE` `pl` `pt_BR` `pt_PT` `ro` `ru` `sr` `sv` `th` `tk` `tr` `uk_UA` `vi` `zh_CN` `zh_TW`

## GitHub

做出模组之后，你自然会想把它分享出去，甚至与他人协作开发，这时可以使用 [GitHub](https://github.com/)。如果你完全不了解 Git（或 GitHub），建议先了解 [GitHub Desktop](https://desktop.github.com/)；否则直接使用你惯用的命令行工具或编辑器插件即可。

你只需掌握：在 GitHub 上打开仓库、在本地仓库暂存并提交改动、以及把改动推送到 GitHub 仓库。项目放到 GitHub 后，有三种分享方式：

- 使用端点（endpoint），例如 `Anuken/MindustryJavaModTemplate`，在游戏内的 GitHub 界面中输入它即可下载；

- 使用 zip 文件，例如 `https://github.com/Anuken/MindustryJavaModTemplate/archive/master.zip`，它会把仓库下载为 zip 文件，放进模组目录即可（无需解压）；

- 在仓库上添加 `mindustry-mod` 话题/标签，这会让它进入话题搜索与 [模组抓取器](https://github.com/Anuken/MindustryMods)。

## 模组发布

Mindustry 下载模组的规则如下：

- 如果模组基于 Java，则需要有一个包含有效 JAR 文件的发行版。

- 优先选择与游戏版本匹配的最新 Github 发行版。

- 可通过在发行版名称中用方括号标注目标游戏版本来进行设置。

- 例如，写作 `Frog Mod [v160]` 会让该发行版面向 Build 160 及其任意修订版本（如 160.3）。

- 写作 `[v160.3]`（指定修订版本）会使其**仅**面向该修订版本，不会面向 160.1 或 160.4。

- 如果没有面向该游戏版本的发行版，则下载最新的发行版。

- 对于 JS 与 JSON 模组，会下载主分支上的最新提交。

- 这让新手更容易下载与管理这类模组。

- 建议为活跃开发单独开一个分支。

- 对于非 Java 模组，标题中不含匹配目标游戏版本标签的发行版会被忽略。

- 例如，如果你的模组是 JSON/JS 类型，而用户使用 Mindustry `Build 160`，则只有当发行版标题末尾带有 `[v160]` 时才会下载；否则将下载主分支上的最新提交。

实际示例：假设我想要一个同时提供 v8 与 v9 版本的模组，可以这样做：
- 创建一个 v8 分支，放入你希望仅用于 v8 的代码。
- 确认该分支的 `mod.hjson` 中含有 `minGameVersion: 160`。
- 创建名为 `My Spectacular Mod [v160]` 的发行版，上传由 v8 源码构建的 JAR，并指向 v8 分支。
  - 所有运行 Mindustry v8（`build 160`）的用户都会下载该发行版，而非最新版。
- 对于 v9 发行版，只需像平常一样创建发行版，标题中不加版本标签，并在 `mod.hjson` 中写上 `minGameVersion: 161`（或你目标的那个构建版本）
  - 而不在 `build 160` 上的用户，在安装时会自动改下载该版本。

关于更新：

- 如果你的发行版与游戏当前运行的 Mindustry 版本匹配，游戏会依据发行版标签处仓库中 `mod.hjson` 里的 `version` 来检查更新。

- 否则，如果没有完全匹配的发行版，它会依据*你仓库最新提交*中 `mod.hjson` 里的 `version` 来检查。

- 版本字符串应遵循合法的 [semver](https://semver.org/) 规范，即三个以句点分隔的数字，例如 `1.3.5`。若使用其他格式，更新检查器可能会判断失误。无论如何都**不要**写成 `build-123-1.5.6 beta-3` 这类怪异格式。

- 如果发布时没有更新 `mod.hjson` 中的版本字符串，游戏就无法得知有新版本可用。

## 常见问题

- 游戏中的 `time` 通过 `ticks` 计算；`ticks`*（有时也叫 `frames`）*是 1/60 秒；

- `tilesize` 在内部为 8 个世界单位；大多数数值（例如碰撞箱尺寸）都以这些世界单位计量；

- 要用 `lifetime` 和 `speed` 计算射程，可以这样算：`lifetime * speed = range`；

- `NullPointerException` 是一条错误信息，表示某个字段为 null 而它不应为 null，意味着可能缺少了某个必需字段；

- *bleeding-edge* 指 Mindustry 最新的开发版本，具体来说是 Github master 分支上的最新提交。bleeding-edge 上的改动通常会在下一个正式版本中进入 Mindustry。
