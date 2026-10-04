# BeamDrill

## BeamDrill

*继承自 Block*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| laser | TextureRegion | null |  |
| laserEnd | TextureRegion | null |  |
| laserCenter | TextureRegion | null |  |
| laserBoost | TextureRegion | null |  |
| laserEndBoost | TextureRegion | null |  |
| laserCenterBoost | TextureRegion | null |  |
| topRegion | TextureRegion | null |  |
| glowRegion | TextureRegion | null |  |
| drillTime | float | 200.0 |  |
| range | int | 5 |  |
| tier | int | 1 |  |
| laserWidth | float | 0.65 |  |
| optionalBoostIntensity | float | 2.5 | 被可选消耗器增益时，钻头进度的加速倍数。 |
| drillMultipliers | ObjectFloatMap of Item | new ObjectFloatMap<>() | 各物品对应的钻速倍率。默认为 1。 |
| blockedItem | Item | null | 该钻头无法开采的特例物品。 |
| blockedItems | Seq of Item | null | 该钻头无法开采的特例物品。 |
| sparkColor | Color | fd9e81ff |  |
| glowColor | Color | ffffffff |  |
| glowIntensity | float | 0.2 |  |
| pulseIntensity | float | 0.07 |  |
| glowScl | float | 3.0 |  |
| sparks | int | 7 |  |
| sparkRange | float | 10.0 |  |
| sparkLife | float | 27.0 |  |
| sparkRecurrence | float | 4.0 |  |
| sparkSpread | float | 45.0 |  |
| sparkSize | float | 3.5 |  |
| boostHeatColor | Color | 75b3ccff |  |
| heatColor | Color | ff5959e5 |  |
| heatPulse | float | 0.3 |  |
| heatPulseScl | float | 7.0 |  |
