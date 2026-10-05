# GenericCrafter

## GenericCrafter

*extends Block*

| field | type | default | notes |
|---|---|---|---|
| outputItem | ItemStack | null | Written to outputItems as a single-element array if outputItems is null. |
| outputItems | ItemStack[] | null | Overwrites outputItem if not null. |
| outputLiquid | LiquidStack | null | Written to outputLiquids as a single-element array if outputLiquids is null. |
| outputLiquids | LiquidStack[] | null | Overwrites outputLiquid if not null. |
| liquidOutputDirections | int[] | { -1 } | Liquid output directions, specified in the same order as outputLiquids. Use -1 to dump in every direction. Rotations are relative to block. |
| dumpExtraLiquid | boolean | true | if true, crafters with multiple liquid outputs will dump excess when there's still space for at least one liquid type |
| ignoreLiquidFullness | boolean | false |  |
| craftTime | float | 80.0 |  |
| craftEffect | Effect | none |  |
| updateEffect | Effect | none |  |
| updateEffectChance | float | 0.04 |  |
| updateEffectSpread | float | 4.0 |  |
| warmupSpeed | float | 0.019 |  |
| legacyReadWarmup | boolean | false | Only used for legacy cultivator blocks. |
| drawer | DrawBlock | new DrawDefault() |  |
