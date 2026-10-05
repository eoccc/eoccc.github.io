# 类型

*注意：* 此处未列出已弃用的内容类，且强烈不建议使用它们。请尽快迁移到未弃用的等效类。

在 [Mindustry Javadoc](https://mindustrygame.github.io/docs/deprecated-list.html) 中查看所有已弃用的类和方法的列表。

所有 JSON 示例均自动取自 *BlueWolf3682* 的 [Exotic Mod](https://github.com/BlueWolf3682/Exotic-Mod)。这些示例*仅*应作为字段的参考——不要直接复制粘贴到你的模组中，它们**不会**生效！

## BuildVisibility

游戏用于改变某些特殊情况的一个标志。它可以是以下字符串之一：

- `hidden`

- `shown`

- `debugOnly`

- `editorOnly`

- `coreZoneOnly`

- `worldProcessorOnly`

- `sandboxOnly`

- `campaignOnly`

- `legacyLaunchPadOnly`

- `notLegacyLaunchPadOnly`

- `lightingOnly`

- `fogOnly`

## BlockGroup

方块相互堆叠建造的分组：

- `none`

- `walls`

- `projectors`

- `turrets`

- `transportation`

- `power`

- `liquids`

- `drills`

- `units`

- `logic`

- `payloads`

- `heat`

## ItemStack

`ItemStack` 可以是字符串或对象。它用于描述提供给机器的物品类型和数量。

作为 `string`：

```
copper/5
```

作为 `object`：

```
item: copper
amount: 5
```

| 字段 | 类型 | 备注 |
|---|---|---|
| item | string | [物品](#item)的名称。 |
| amount | int | 该物品的数量。 |

## LiquidStack

`LiquidStack` 可以是字符串或对象。它用于描述提供给机器的液体类型和数量。

作为 `string`：

```
water/0.5
```

作为 `object`：

```
liquid: water
amount: 0.5
```

| 字段 | 类型 | 备注 |
|---|---|---|
| liquid | string | [液体](#liquid)的名称。 |
| amount | float | 该液体的数量。 |

## Category

建造菜单的分类：

- `turret` 攻击性炮塔；

- `production` 生产原材料的方块，例如钻头；

- `distribution` 搬运物品的方块；

- `liquid` 搬运液体的方块；

- `power` 发电或输电的方块；

- `defense` 墙体及其他防御建筑；

- `crafting` 合成物品的方块；

- `units` 制造单位的方块；

- `effect` 用于储存或被动效果的东西；

- `logic` 与逻辑运算相关的方块。

## Color

颜色是一个十六进制字符串，`` 例如：

- `ff0000` 是红色，

- `00ff00` 是绿色，

- `0000ff` 是蓝色，

- `ffff00` 是黄色，

- `00ffff` 是青色，

- 等等。

## CacheLayer

用于缓存渲染的图层，按绘制顺序排列：

- `water` 水面图层，为地块添加水面着色器，并产生波浪倒影；

- `mud` 泥浆图层，与水面类似，但用于泥浆地块；

- `cryofluid` 冷冻液图层，赋予冷冻液池所用的冰蓝色着色器；

- `tar` 焦油图层，添加焦油着色器，使其更暗并产生一些气泡倒影；

- `slag` 熔渣图层，赋予熔融熔渣发光着色器；

- `arkycite` arkycite 图层，用于 Erekir 上的 arkycite 液体；

- `space` 太空图层，用于背景的太空地块；

- `normal` 普通图层，大多数地板的默认图层；

- `walls` 墙体图层；

`CacheLayer` 是一个类而非枚举，因此模组可以用 `CacheLayer.add` 注册自己的图层。

## TargetPriority

一组浮点常量；值越高表示优先级越高。优先级更高的方块总会优先于优先级更低的方块被选为目标，无论距离远近。

| 优先级 | 值 | 备注 |
|---|---|---|
| `wall` | -3 | 没人在意墙 |
| `under` | -2 | 用于带 `underBullets` 的方块 |
| `transport` | -1 | 传送带及其他运输设施 |
| `base` | 0 | 大多数方块 |
| `turret` | 1 | 炮塔，因为它们会造成伤害 |
| `core` | 2 | 核心永远是最优先的目标 |
