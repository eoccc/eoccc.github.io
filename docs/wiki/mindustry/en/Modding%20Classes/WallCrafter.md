# WallCrafter

## WallCrafter

*extends Block*

| field | type | default | notes |
|---|---|---|---|
| topRegion | TextureRegion | null |  |
| rotatorBottomRegion | TextureRegion | null |  |
| rotatorRegion | TextureRegion | null |  |
| drillTime | float | 150.0 | Time to produce one item at 100% efficiency. |
| liquidBoostIntensity | float | 1.6 | How many times faster the drill will progress when boosted by liquid. |
| updateEffect | Effect | mineWallSmall | Effect randomly played while drilling. |
| updateEffectChance | float | 0.02 |  |
| rotateSpeed | float | 2.0 |  |
| attribute | Attribute | sand | Attribute to check for wall output. |
| output | Item | sand |  |
| boostItemUseTime | float | 120.0 |  |
| itemBoostIntensity | float | 1.6 | How many times faster the drill will progress when boosted by items. Note: Using item and liquid boosters at once is not supported. |
| itemConsumer | Consume | null |  |
| hasLiquidBooster | boolean | false |  |
| timerUse | int | 1 |  |
