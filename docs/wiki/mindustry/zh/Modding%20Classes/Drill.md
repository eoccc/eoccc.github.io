# Drill

## Drill

*继承自 Block*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| hardnessDrillMultiplier | float | 50.0 |  |
| tier | int | 0 | 该钻头可开采的最高方块等级。 |
| drillTime | float | 300.0 | 钻取一份矿石的基础耗时（帧）。 |
| liquidBoostIntensity | float | 1.6 | 被液体增益时，钻头进度的加速倍数。 |
| warmupSpeed | float | 0.015 | 钻头加速的速度。 |
| blockedItem | Item | null | 该钻头无法开采的特例物品。 |
| blockedItems | Seq of Item | null | 该钻头无法开采的特例物品。 |
| drawMineItem | boolean | true | 是否绘制该钻头正在开采的物品。 |
| drillEffect | Effect | mine | 产出物品时播放的效果。带颜色。 |
| drillEffectRnd | float | -1.0 | 钻探效果的随机程度。默认取方块尺寸。 |
| drillEffectChance | float | 0.02 | 显示该效果的概率，对极高速钻头很有用。 |
| rotateSpeed | float | 2.0 | 钻头旋转的速度。 |
| updateEffect | Effect | pulverizeSmall | 钻探时随机播放的效果。 |
| updateEffectChance | float | 0.02 | 更新效果出现的概率。 |
| drillMultipliers | ObjectFloatMap of Item | new ObjectFloatMap<>() | 各物品对应的钻速倍率。默认为 1。 |
| drawRim | boolean | false |  |
| drawSpinSprite | boolean | true |  |
| heatColor | Color | ff5512ff |  |
| rimRegion | TextureRegion | null |  |
| rotatorRegion | TextureRegion | null |  |
| topRegion | TextureRegion | null |  |
| itemRegion | TextureRegion | null |  |
