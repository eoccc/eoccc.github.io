# ConsumeGenerator

## ConsumeGenerator

*继承自 PowerGenerator*

只接收特定物品或液体的发生器。

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| itemDuration | float | 120.0 | 单个物品可产生电力的刻数。 |
| warmupSpeed | float | 0.05 |  |
| effectChance | float | 0.01 |  |
| generateEffect | Effect | none |  |
| consumeEffect | Effect | none |  |
| generateEffectRange | float | 3.0 |  |
| baseLightRadius | float | 65.0 |  |
| outputLiquid | LiquidStack | null |  |
| explodeOnFull | boolean | false | 为 true 时，输出液体超过容量会使该方块爆炸。 |
| filterItem | ConsumeItemFilter | null |  |
| filterLiquid | ConsumeLiquidFilter | null |  |
| itemDurationMultipliers | ObjectFloatMap of Item | new ObjectFloatMap<>() | 乘以指定物品的 itemDuration。 |
