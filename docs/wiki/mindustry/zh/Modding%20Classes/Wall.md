# Wall

## Wall

*继承自 Block*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| lightningChance | float | -1.0 | 触发闪电的概率。-1 表示禁用 |
| lightningDamage | float | 20.0 |  |
| lightningLength | int | 17 |  |
| lightningColor | Color | f3e979ff |  |
| lightningSound | Sound | shootArc |  |
| chanceDeflect | float | -1.0 | 子弹偏转概率。-1 表示禁用 |
| flashHit | boolean | false |  |
| flashColor | Color | ffffffff |  |
| deflectSound | Sound | none |  |
| autotile | boolean | false | 若为 true，该方块使用自动拼接；不支持变体。参见 https://github.com/GglLfr/tile-gen |
