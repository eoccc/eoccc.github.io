# GenericCrafter

## GenericCrafter

*继承自 Block*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| outputItem | ItemStack | null | 若 outputItems 为 null，则作为单元素数组写入 outputItems。 |
| outputItems | ItemStack[] | null | 非 null 时覆写 outputItem。 |
| outputLiquid | LiquidStack | null | 若 outputLiquids 为 null，则作为单元素数组写入 outputLiquids。 |
| outputLiquids | LiquidStack[] | null | 非 null 时覆写 outputLiquid。 |
| liquidOutputDirections | int[] | { -1 } | 液体输出方向，按与 outputLiquids 相同的顺序指定。使用 -1 表示向所有方向倾倒。旋转相对于方块。 |
| dumpExtraLiquid | boolean | true | 若为 true，具有多个液体输出的制作机在有至少一种液体类型的空间时，会倾倒多余部分 |
| ignoreLiquidFullness | boolean | false |  |
| craftTime | float | 80.0 |  |
| craftEffect | Effect | none |  |
| updateEffect | Effect | none |  |
| updateEffectChance | float | 0.04 |  |
| updateEffectSpread | float | 4.0 |  |
| warmupSpeed | float | 0.019 |  |
| legacyReadWarmup | boolean | false | 仅用于旧版培育器方块。 |
| drawer | DrawBlock | new DrawDefault() |  |
