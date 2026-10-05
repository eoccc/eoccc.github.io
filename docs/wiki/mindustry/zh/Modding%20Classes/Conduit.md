# Conduit

## Conduit

*继承自 LiquidBlock*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| timerFlow | int | 1 |  |
| botColor | Color | 565656ff |  |
| topRegions | TextureRegion[] | null |  |
| botRegions | TextureRegion[] | null |  |
| capRegion | TextureRegion | null |  |
| rotateRegions | TextureRegion[][][] | null | 索引：[旋转] [流体类型] [帧] |
| padCorners | boolean | true | 为 true 时，液体区域四角留白，以免外凸。 |
| leaks | boolean | true |  |
| junctionReplacement | Block | null |  |
| bridgeReplacement | Block | null |  |
| rotBridgeReplacement | Block | null |  |
