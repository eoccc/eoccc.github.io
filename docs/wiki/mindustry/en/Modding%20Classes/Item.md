# Item

## Item

*extends UnlockableContent*

| field | type | default | notes |
|---|---|---|---|
| color | Color | 000000ff |  |
| explosiveness | float | 0.0 | how explosive this item is. |
| flammability | float | 0.0 | flammability above 0.3 makes this eligible for item burners. |
| radioactivity | float | 0.0 | how radioactive this item is. |
| charge | float | 0.0 | how electrically potent this item is. |
| hardness | int | 0 | drill hardness of the item |
| cost | float | 1.0 | base material cost of this item, used for calculating place times 1 cost = 1 tick added to build time |
| healthScaling | float | 0.0 | When this item is present in the build cost, a block's default health is multiplied by 1 + scaling, where 'scaling' is summed together for all item requirement types. |
| lowPriority | boolean | false | if true, this item is of the lowest priority to drills. |
| frames | int | 0 | If >0, this item is animated. |
| transitionFrames | int | 0 | Number of generated transition frames between each frame |
| frameTime | float | 5.0 | Ticks in-between animation frames. |
| buildable | boolean | true | If true, this material is used by buildings. If false, this material will be incinerated in certain cores. |
| hidden | boolean | false |  |
