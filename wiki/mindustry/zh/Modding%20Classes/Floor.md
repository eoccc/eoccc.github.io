# Floor

## Floor

*继承自 Block*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| edge | String | "stone" | 边缘回退，主要用于矿石 |
| speedMultiplier | float | 1.0 | 单位在该地板行走时，其速度乘以该数值。 |
| dragMultiplier | float | 1.0 | 单位在该地板行走时，其阻力乘以该数值。 |
| damageTaken | float | 0.0 | 该格每刻受到的伤害。 |
| drownTime | float | 0.0 | 在该地板上淹死所需的刻数。0 表示禁用。 |
| walkEffect | Effect | none | 在该地板上行走时的效果。 |
| walkSound | Sound | none | 行走时播放的音效。 |
| walkSoundVolume | float | 0.1 | 行走音效的音量。 |
| walkSoundPitchMin | float | 0.8 | 行走音效的音量。 |
| walkSoundPitchMax | float | 1.2 | 行走音效的音量。 |
| drownUpdateEffect | Effect | bubble | 在该地板上淹死时显示的效果。 |
| status | StatusEffect | none | 行走于其上时施加的状态效果。 |
| statusDuration | float | 60.0 | 所施加状态效果的强度。 |
| liquidDrop | Liquid | null | 该方块掉落的液体，用于泵。 |
| liquidMultiplier | float | 1.0 | 抽液倍率，用于深水。 |
| isLiquid | boolean | false | 该方块是否为液体。 |
| overlayAlpha | float | 0.65 | 对于液体地板，这是绘制在其上的覆盖层的不透明度。 |
| supportsOverlay | boolean | false | 该地板是否支持覆盖地板 |
| supportsBeingOverlaid | boolean | true | 若为 false，即使所处地板支持，该地板也不能用作覆盖层（液体底层） |
| shallow | boolean | false | 用于生成的浅水标记 |
| blendGroup | Block | this | 该方块不绘制边缘的一组方块。 |
| oreDefault | boolean | false | 该矿石是否默认在地图中生成。 |
| oreScale | float | 24.0 | 矿石生成参数。 |
| oreThreshold | float | 0.828 | 矿石生成参数。 |
| wall | Block | air | 该方块的墙变体。若未找到可能为 Blocks.air。 |
| decoration | Block | air | 装饰方块，通常是岩石，也可能为空气。 |
| canShadow | boolean | true | 单位是否可以在其上绘制阴影。 |
| forceDrawLight | boolean | false | 为 true 时，该地板忽略覆盖层的 obstructsLight 标记。 |
| needsSurface | boolean | true | 该覆盖层是否需要附着在某个表面上。对于漂浮方块（如出生点）为 False。 |
| allowCorePlacement | boolean | false | 为 true 时，可在该地板上放置核心。 |
| wallOre | boolean | false | 为 true 时，该矿石可生成在墙上。 |
| blendId | int | -1 | 用于混合组的实际 ID。内部使用。 |
| tilingVariants | int | 0 | 大于 0 时，该地板按大贴图的局部绘制。 |
| autotile | boolean | false | 若为 true，该地板使用自动拼接；不支持变体。参见 https://github.com/GglLfr/tile-gen |
| autotileMidVariants | int | 1 | 大于 1 时，自动拼接的中部区域带随机变体。 |
| autotileVariants | int | 1 | 主自动拼接精灵图的变体。 |
| drawEdgeIn | boolean | true | 为 true（默认）时，该地板会在自身上绘制其他地板的边缘。 |
| drawEdgeOut | boolean | true | 为 true（默认）时，该地板会把自身边缘绘制到其他地板上。 |
