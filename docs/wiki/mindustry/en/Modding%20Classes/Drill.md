# Drill

## Drill

*extends Block*

| field | type | default | notes |
|---|---|---|---|
| hardnessDrillMultiplier | float | 50.0 |  |
| tier | int | 0 | Maximum tier of blocks this drill can mine. |
| drillTime | float | 300.0 | Base time to drill one ore, in frames. |
| liquidBoostIntensity | float | 1.6 | How many times faster the drill will progress when boosted by liquid. |
| warmupSpeed | float | 0.015 | Speed at which the drill speeds up. |
| blockedItem | Item | null | Special exemption item that this drill can't mine. |
| blockedItems | Seq of Item | null | Special exemption items that this drill can't mine. |
| drawMineItem | boolean | true | Whether to draw the item this drill is mining. |
| drillEffect | Effect | mine | Effect played when an item is produced. This is colored. |
| drillEffectRnd | float | -1.0 | Drill effect randomness. Block size by default. |
| drillEffectChance | float | 0.02 | Chance of displaying the effect. Useful for extremely fast drills. |
| rotateSpeed | float | 2.0 | Speed the drill bit rotates at. |
| updateEffect | Effect | pulverizeSmall | Effect randomly played while drilling. |
| updateEffectChance | float | 0.02 | Chance the update effect will appear. |
| drillMultipliers | ObjectFloatMap of Item | new ObjectFloatMap<>() | Multipliers of drill speed for each item. Defaults to 1. |
| drawRim | boolean | false |  |
| drawSpinSprite | boolean | true |  |
| heatColor | Color | ff5512ff |  |
| rimRegion | TextureRegion | null |  |
| rotatorRegion | TextureRegion | null |  |
| topRegion | TextureRegion | null |  |
| itemRegion | TextureRegion | null |  |
