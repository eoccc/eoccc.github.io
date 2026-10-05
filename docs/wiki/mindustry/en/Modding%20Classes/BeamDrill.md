# BeamDrill

## BeamDrill

*extends Block*

| field | type | default | notes |
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
| optionalBoostIntensity | float | 2.5 | How many times faster the drill will progress when boosted by an optional consumer. |
| drillMultipliers | ObjectFloatMap of Item | new ObjectFloatMap<>() | Multipliers of drill speed for each item. Defaults to 1. |
| blockedItem | Item | null | Special exemption item that this drill can't mine. |
| blockedItems | Seq of Item | null | Special exemption items that this drill can't mine. |
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
