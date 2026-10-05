# WallCrafter

## WallCrafter

*继承自 Block*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| topRegion | TextureRegion | null |  |
| rotatorBottomRegion | TextureRegion | null |  |
| rotatorRegion | TextureRegion | null |  |
| drillTime | float | 150.0 | 以 100% 效率生产一个物品所需的时间。 |
| liquidBoostIntensity | float | 1.6 | 被液体增益时，钻头进度的加速倍数。 |
| updateEffect | Effect | mineWallSmall | 钻探时随机播放的效果。 |
| updateEffectChance | float | 0.02 |  |
| rotateSpeed | float | 2.0 |  |
| attribute | Attribute | sand | 用于检查墙体产出的属性。 |
| output | Item | sand |  |
| boostItemUseTime | float | 120.0 |  |
| itemBoostIntensity | float | 1.6 | 被物品加速时钻头推进速度加快多少倍。注意：不支持同时使用物品和液体加速器。 |
| itemConsumer | Consume | null |  |
| hasLiquidBooster | boolean | false |  |
| timerUse | int | 1 |  |
