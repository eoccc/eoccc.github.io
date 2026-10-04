# AttributeCrafter

## AttributeCrafter

*继承自 GenericCrafter*

从属性地块获得效率的制作机。

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| attribute | Attribute | heat |  |
| baseEfficiency | float | 1.0 | 制造器的基础效率。 |
| maxBoost | float | 1.0 | 来自属性的最大效率/产出增益。 |
| minEfficiency | float | -1.0 | 放置该方块所需的最低效率。 |
| displayEfficiency | boolean | true | 是否在界面中显示该状态条。 |
| displayScaledOutput | boolean | true | 是否在界面中显示该状态条。 |
| scaleLiquidConsumption | boolean | false | 液体消耗是否随效率缩放。 |
| outputScale | float | 0.0 | 随属性缩放的产出（产量）倍率。<=0 表示禁用。 |
| boostScale | float | 1.0 | 随属性缩放的效率（速度）倍率。<=0 表示禁用。 |
