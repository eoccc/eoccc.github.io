# 数据补丁

数据补丁是一个强大的工具，可按地图或按服务器修改方块、单位与物品的属性。其应用场景包括平衡性调整、自定义游戏模式，或改变游戏进程。

数据补丁**可以**做到的事情：

- 让工厂多消耗或少消耗某种资源

- 更改方块的资源需求

- 完全更改单位的武器与弹药

- 更改单位工厂可用的配方

- 将方块或单位显示的贴图更改为游戏内的其他纹理

- 更改任意方块或单位的建造速度、生命值、护甲等

- 更改单位的类型（例如把地面单位变成飞行单位）

数据补丁**无法**做到的事情：

- 引入原版中不存在的新机制

- 更改现有方块的类型（例如把墙变成炮塔）

平衡性补丁*并非*模组的替代品，它只能微调现有内容与机制。

# 关于添加新内容的说明

如果你的目标是用 Build 159 引入的系统*新增*内容，那么该系统与数据*补丁*略有不同。

目前还没有完整的指南，但这里简要介绍一下它的工作方式：

- 内容格式与 JSON 模组相同，但存在一些限制。

- 不支持的特性：
星球（在地图/服务器中无用）

- 区块，原因同上

- 科技树的新增/修改

- 无法直接重新指定贴图区域，贴图会根据内容名称自动加载。
例如，你无法像使用补丁那样为方块设置 `uiIcon: "cat"`。

- 你改为需要导入一张与方块同名的图片作为素材。

- 例如，如果你新增了名为 "cat" 的方块或物品，就需要在图片标签页导入 "cat.png"，它会被自动加载为该方块的图标/精灵图。

- 不同方块的图片命名规则各不相同，可能相当复杂，目前尚无文档说明。

- 由于你定义的是*新*内容而非补丁，因此不支持字段选择器。
这包括尝试赋值 `weapons.0.name`、`weapons.+` 之类的写法。你一次只能直接赋值*一个*字段。

- 所有素材与内容都带有 `dp-` 前缀。
例如：如果你导入名为 "cat-weapon" 的 PNG，那么在贴图标记与武器名称中，其精灵图名会是 "dp-cat-weapon"。音效同理。

# Writing A Trivial Data Patch

数据补丁使用 JSON 或 HJSON（JSON 的超集）编写。你需要用文本编辑器来写，目前游戏内没有补丁编辑器。

为简洁起见，本指南只演示如何用 HJSON 编写补丁。

首先，新建名为 `mypatch.hjson` 的文本文件，内容如下：

```
//naming a patch is optional, but helps identify it in the UI
name: My Patch

//makes all conveyors have 50 max health
block.conveyor.health: 50
```

# Applying Data Patches

## 在地图上应用补丁

在地图编辑器中打开你的地图，然后打开左上角菜单（桌面端可按 ESC）。依次进入 *地图信息 → 数据补丁 → 添加*，再指定上一步保存的补丁文件。点击 ⚠️ 图标可查看补丁产生的错误，点击 🔁 按钮可重新加载文件。

## 在专用服务器上应用补丁

打开你的服务器目录（其中应已包含 plugins、maps、saves 等文件夹），找到 `patches` 目录，把补丁文件放进去即可。补丁文件必须使用 `hjson/json/json5` 扩展名才会被加载。
它们会自动应用，且在地图自身已含的其他数据补丁*之后*生效。

如果一切操作正确，服务器启动时应会记录已加载的补丁文件数量。任何警告或错误也会打印到控制台。
若要在服务器运行期间重新加载补丁，请使用 `reloadpatches` 命令。

# Data Patch Basics

数据补丁遵循层级结构。第一层定义要修改的内容类型：`block`、`liquid`、`item`、`unit`、`weather` 等。

*第二*层定义要编辑的内容名称，例如 `conveyor`、`copper`、`copper-wall-large`。这些名称*区分大小写*；若你启用了控制台，它们会显示在核心数据库中对应内容的名称下方。

*第三*层定义你要修改的属性及其对应取值。示例如下：

```
block: {
  conveyor: {
    health: 50
    //other properties of the conveyor go here...
  }
  //other blocks here...
}
//other types of content here...
```

另外，如果你只修改单个属性，使用简写语法可能更方便：

```
block.conveyor.health: 50
```

## 查看内容的全部字段

如果你熟悉 Java，可以查看相关内容的源文件，例如方块的 [Block.java](https://github.com/Anuken/Mindustry/blob/master/core/src/mindustry/world/Block.java)。

如果不熟悉，你可以在游戏设置中启用控制台，然后在数据库里针对某个方块、单位或液体点击「查看内容字段」按钮。

注意，这里只显示*该类自身*的字段；若想查看父类的字段，请点击该页面上紧跟在 "extends" 之后的链接。

例如，[传送带](https://mindustrygame.github.io/wiki/Modding%20Classes/Conveyor/)页面会显示其全部字段，以及 [Block](https://mindustrygame.github.io/wiki/Modding%20Classes/Block/) 父类中的所有内容。

## 访问数组/序列

当需要访问数组（T[]）或序列（Seq）时，可以这样写：

```
//greatly offsets one of dagger's two weapons
unit.dagger.weapons.0.x: 100
```

注意，修改*镜像*武器的子弹会同时影响两侧，因为它们共用同一种子弹类型：

```
//this wall make *both* dagger weapons deal 55 damage
unit.dagger.weapons.0.bullet.damage: 55
```

## 数组/序列的追加与覆写

有时可能需要向序列中*追加*而非覆写，写法如下：

```
//adds a ridiculously overpowered laser to flare's weapons, keeping the others intact
//note the .+ before the field assignment; this adds the element
//also note that it can be a single element, not an array!
unit.flare.weapons.+: {
  x: 0
  y: 0
  reload: 10
  bullet: {
    type: LaserBulletType
    damage: 100
  }
}
```

或者，你也可以覆写整个数组：

```
//flare will *only* have this weapon now, its old ones will be overwritten
//also note that, when overwriting, you *have* to use the array brackets [], since you are assigning a new value
unit.flare.weapons: [
  {
    x: 0
    y: 0
    reload: 10
    bullet: {
      type: LaserBulletType
      damage: 100
    }
  }
]
```

该语法适用于 `T[]`、`Seq` 与 `ObjectSet` 类型的字段。

# General Information

- 时间值通常以*刻*（ticks，有时也称「帧」）计量，1 刻为 1/60 秒（60 刻 = 1 秒）。如果某字段描述的是持续时间，其单位多半是刻；如果描述的是消耗速率，则多半是「每刻单位数」。

- 距离、位置与尺寸通常以「世界单位」计量，1 世界单位为 1/8 格。这是因为 Mindustry 早期使用 8x8 的精灵图，当时 1 世界单位等于 1 像素。这*确实*很不直观，但出于历史原因一直沿用至今。

- 通过逻辑处理器处理坐标时，系统会*在内部*进行世界单位的换算。而补丁直接修改字段，没有这层转换。

- 物品与液体堆叠可写作「名称/数量」。例如 `ItemStack` 字段的取值可以是 `thorium/100`。

# Caveats & Limitations

- 为单位的武器设置 `mirror: true` 不会生效，因为单位不会重新执行初始化。你需要手动创建镜像版本并设置 `x/shootX/flipSprite`。

- 即使你提高了单位子弹的存活时间或速度，单位的 `range` 与 `maxRange` 也不会更新，这些值必须手动赋值。

- 同理，重新指定单位类型后其字段也不会更新。例如被重新指定的海军单位仍会淹死。

- 即使让方块或单位绘制更大的精灵图，`clipSize` 也不会更新，需要手动赋值。

- 许多消耗器类型对并非为其设计的方块不生效。一般而言，原版中未使用的组合多半支持不佳。

- 方块尺寸无法重新指定，否则会严重破坏存档，且对大多数运输类方块完全不生效。

- 依赖其他值的数值不会被重新计算。例如，修改方块的物品建造需求*不会*像模组那样同时改变其建造耗时。

- 环境（静态）方块无法使用环境图集页之外的贴图。也就是说，你可以让草地使用雪的精灵图，但不能让草地使用路由器的精灵图，否则游戏内会显示错误贴图。

- 补丁应用后贴图不会被重新加载。例如，修改 `DrawRegion` 的 `suffix` 或 `name` 不会产生任何效果，因为 `load` 不会再次被调用。此时应改为创建一个全新的对象。

- 重新指定单位/方块的生命值不会更新现有单位/方块的当前生命值。若你提高某方块的最大生命值，地图上该类型的*现有*建筑都会显示为受损状态。

- 补丁很可能导致游戏崩溃或卡死。若发生这种情况请反馈，但请注意我未必能修复*所有*问题——请保持合理。诸如「我让这个单位发射了 9 万亿颗子弹，游戏卡死了」这类报告将不予处理。

# Extra Examples

## 「双联化」

```
//once again, names are optional, but help identify a patchset in the list
name: Duofication

item: {
  //fissile-matter is an unused item, so use it for demonstration
  fissile-matter: {
    //change the display name of the item to 'Duo'
    localizedName: Duo
    //unhide it
    hidden: false
    //change the in-game icon to 'duo-preview', which is used by the duo turret
    fullIcon: duo-preview
    //change the in-ui icon to 'block-duo-ui', which is also used by the duo turret in UI
    uiIcon: block-duo-ui
  }
}

block: {
  //edit the pulverizer
  pulverizer: {
    //change its name
    localizedName: Duo Factory
    //rewrite the things it consumes
    consumes: {
      //remove all previous consumers - without this line, it would retain its old consumption of scrap
      //you can also remove *only* item consumers by writing `remove: items`
      remove: all
      //consume 1 copper item per craft
      item: copper
    }
    //change the UI display icon
    uiIcon: block-duo-ui
    //change the region
    region: block-duo-full
    //output 1 fissile matter, which was previously patched to have the name 'Duo'
    //note that outputItems is an array, so its contents have to be written as a list with [ and ]
    outputItems: [fissile-matter/1]
    //define the drawers, which define how the block is rendered. they can be defined as an array with []
    drawer: [
      {
        //the first drawer is a simple DrawRegion, which draws the sprite 'block-1', which is the base for 1x1 Serpulo turrets
        type: DrawRegion
        name: block-1
      }
      {
        //the second drawer draws the 'duo-preview' region and rotates it at speed 1
        type: DrawRegion
        rotateSpeed: 1
        name: duo-preview
      }
    ]
  }

}

unit: {
  //patch the dagger unit
  dagger: {
    //change its body region to duo-preview
    region: duo-preview
    //re-define the weapon array (note: this clears all previous weapons)
    weapons: [
      //all weapons in the array are objects of their own, so they need to be encased in {} braces
      {
        //the weapon is centered on the unit
        x: 0
        y: 0
        //reload of 20 ticks (1 second = 60 ticks)
        reload: 20
        //alternate left and right with a spread of 3.5 world units (1 tile = 8 world units)
        shoot: {
          type: ShootAlternate
          spread: 3.5
        }

        //define the bullet the weapon shoots
        bullet: {
          //width and height of the sprite in world units
          width: 7
          height: 9
          //lifetime in ticks (1 second)
          lifetime: 60
          //colors of the bullet as a hex code
          frontColor: eac1a8
          backColor: d39169
        }
      }
    ]
  }
}
```

## 修改炮塔弹药

```
block.fuse.ammoTypes: {
  //remove titanium ammo from the ammo map by using the special "-" value
  titanium: "-"
  //add surge alloy ammo that shoots a laser
  surge-alloy: {
    type: LaserBulletType
    //make it produce 1 shot per ammo item
    ammoMultiplier: 1
    //make it shoot half as fast
    reloadMultiplier: 0.5
    damage: 100
    //make it look awful!
    colors: ["000000", "ff0000", "ffffff"]
  }
}
```

## 添加单位能力

```
//add a new ability to pulsar (note the .+)
unit.pulsar.abilities.+: [
  {
    type: ForceFieldAbility
    //set the maximum health of of the force field to 1000
    max: 1000
  }
]
```

## 添加单位方案

```
//make the ground factory produce flares
block.ground-factory.plans.+: {
  unit: flare
  //require 10 surge alloy to build
  requirements: [surge-alloy/10]
  //take 100 ticks to build
  time: 100
}
```

## 修改单位工厂方案

```
//make daggers (the first plan of the ground factory, or index 0) take 60 ticks to build, or 1 second
block.ground-factory.plans.0.time: 60
```

## 修改方块需求

```
//make duo cost 5 titanium and 20 surge alloy
block.duo.requirements: [titanium/5, surge-alloy/20]
```
