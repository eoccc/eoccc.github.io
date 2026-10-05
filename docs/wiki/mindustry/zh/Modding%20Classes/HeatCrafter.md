# HeatCrafter

## HeatCrafter

*继承自 GenericCrafter*

需要接触加热方块才能制作的制作机。

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| heatRequirement | float | 10.0 | 达到 100% 效率所需的基础热量。 |
| overheatScale | float | 1.0 | 热量达到该需求后，多余热量将按此数值缩放。 |
| maxEfficiency | float | 4.0 | 过热后的最高可能效率。 |
