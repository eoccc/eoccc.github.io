# Pump

## Pump

*继承自 LiquidBlock*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| pumpAmount | float | 0.2 | 每格抽取量。 |
| consumeTime | float | 300.0 | 物品消耗之间的间隔（若适用）。 |
| warmupSpeed | float | 0.019 |  |
| drawer | DrawBlock | new DrawMulti(new DrawDefault(), new DrawPumpLiquid()) |  |
