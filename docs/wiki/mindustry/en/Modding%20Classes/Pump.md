# Pump

## Pump

*extends LiquidBlock*

| field | type | default | notes |
|---|---|---|---|
| pumpAmount | float | 0.2 | Pump amount per tile. |
| consumeTime | float | 300.0 | Interval in-between item consumptions, if applicable. |
| warmupSpeed | float | 0.019 |  |
| drawer | DrawBlock | new DrawMulti(new DrawDefault(), new DrawPumpLiquid()) |  |
