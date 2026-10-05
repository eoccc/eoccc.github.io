# ItemBridge

## ItemBridge

*extends Block*

| field | type | default | notes |
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
| linkSameType | boolean | true | If true, only allows this bridge to link with the same block type. Otherwise this can link with any ItemBridge. |
| arrowSpacing | float | 4.0 |  |
| arrowOffset | float | 2.0 |  |
| arrowPeriod | float | 0.4 |  |
| arrowTimeScl | float | 6.2 |  |
| bridgeWidth | float | 6.5 |  |
| noAcceptDisabled | boolean | false | If true, this bridge will not accept items or liquids when disabled. |
| lastBuild | ItemBridgeBuild | null |  |
