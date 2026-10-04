# PowerGenerator

## PowerGenerator

*继承自 PowerDistributor*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| powerProduction | float | 0.0 | 效率为 1.0（即 100%）时每刻产生的电力。 |
| generationType | Stat | basePowerGeneration |  |
| drawer | DrawBlock | new DrawDefault() |  |
| explosionRadius | int | 12 |  |
| explosionDamage | int | 0 |  |
| explodeEffect | Effect | none |  |
| explodeSound | Sound | none |  |
| explosionPuddles | int | 10 |  |
| explosionPuddleRange | float | 16.0 |  |
| explosionPuddleAmount | float | 100.0 |  |
| explosionPuddleLiquid | Liquid | null |  |
| explosionMinWarmup | float | 0.0 |  |
| explosionShake | float | 0.0 |  |
| explosionShakeDuration | float | 6.0 |  |
| explosionBreaksProps | boolean | true |  |
| explosionScorchSize | int | 0 | 爆炸后地面焦痕的大小，取值 1-9；小于 1 表示禁用。 |
| explosionIgnitionChance | float | 0.0 | 爆炸半径内每格起火的概率。 |
| explosionScaleIgnitionChance | boolean | true | 为 true 时，点火概率随距离递减。 |
| explosionSpeed | float | 0.4 | 火势蔓延的速度。 |
| explosionFireballs | int | 0 | 爆炸额外生成的火球数量。 |
