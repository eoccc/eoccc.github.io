# Conduit

## Conduit

*extends LiquidBlock*

| field | type | default | notes |
|---|---|---|---|
| timerFlow | int | 1 |  |
| botColor | Color | 565656ff |  |
| topRegions | TextureRegion[] | null |  |
| botRegions | TextureRegion[] | null |  |
| capRegion | TextureRegion | null |  |
| rotateRegions | TextureRegion[][][] | null | indices: [rotation] [fluid type] [frame] |
| padCorners | boolean | true | If true, the liquid region is padded at corners, so it doesn't stick out. |
| leaks | boolean | true |  |
| junctionReplacement | Block | null |  |
| bridgeReplacement | Block | null |  |
| rotBridgeReplacement | Block | null |  |
