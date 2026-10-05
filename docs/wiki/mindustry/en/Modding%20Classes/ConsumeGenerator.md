# ConsumeGenerator

## ConsumeGenerator

*extends PowerGenerator*

A generator that just takes in certain items or liquids.

| field | type | default | notes |
|---|---|---|---|
| itemDuration | float | 120.0 | The time in number of ticks during which a single item will produce power. |
| warmupSpeed | float | 0.05 |  |
| effectChance | float | 0.01 |  |
| generateEffect | Effect | none |  |
| consumeEffect | Effect | none |  |
| generateEffectRange | float | 3.0 |  |
| baseLightRadius | float | 65.0 |  |
| outputLiquid | LiquidStack | null |  |
| explodeOnFull | boolean | false | If true, this block explodes when outputLiquid exceeds capacity. |
| filterItem | ConsumeItemFilter | null |  |
| filterLiquid | ConsumeLiquidFilter | null |  |
| itemDurationMultipliers | ObjectFloatMap of Item | new ObjectFloatMap<>() | Multiplies the itemDuration for a given item. |
