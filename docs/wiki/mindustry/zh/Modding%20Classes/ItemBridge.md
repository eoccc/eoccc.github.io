# ItemBridge

## ItemBridge

*继承自 Block*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| timerCheckMoved | int | 1 |  |
| range | int | 0 |  |
| transportTime | float | 0.0 |  |
| endRegion | TextureRegion | null |  |
| bridgeRegion | TextureRegion | null |  |
| arrowRegion | TextureRegion | null |  |
| fadeIn | boolean | true |  |
| moveArrows | boolean | true |  |
| pulse | boolean | false |  |
| linkSameType | boolean | true | 若为 true，只允许该桥与相同方块类型连接。否则可与任意 ItemBridge 连接。 |
| arrowSpacing | float | 4.0 |  |
| arrowOffset | float | 2.0 |  |
| arrowPeriod | float | 0.4 |  |
| arrowTimeScl | float | 6.2 |  |
| bridgeWidth | float | 6.5 |  |
| noAcceptDisabled | boolean | false | 为 true 时，该桥接在被禁用时不接收物品或液体。 |
| lastBuild | ItemBridgeBuild | null |  |
