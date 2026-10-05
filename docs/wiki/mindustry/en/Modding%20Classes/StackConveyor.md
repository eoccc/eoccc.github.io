# StackConveyor

## StackConveyor

*extends Block*

| field | type | default | notes |
|---|---|---|---|
| regions | TextureRegion[] | null |  |
| edgeRegion | TextureRegion | null |  |
| stackRegion | TextureRegion | null |  |
| glowRegion | TextureRegion | null | requires power to work properly |
| edgeGlowRegion | TextureRegion | null |  |
| glowAlpha | float | 1.0 |  |
| glowColor | Color | feb380ff |  |
| baseEfficiency | float | 0.0 |  |
| speed | float | 0.0 |  |
| outputRouter | boolean | true |  |
| recharge | float | 2.0 | (minimum) amount of loading docks needed to fill a line. |
| loadEffect | Effect | conveyorPoof |  |
| unloadEffect | Effect | conveyorPoof |  |
