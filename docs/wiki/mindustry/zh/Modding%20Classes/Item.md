# Item

## Item

*继承自 UnlockableContent*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| color | Color | 000000ff |  |
| explosiveness | float | 0.0 | 该物品的爆炸性有多强。 |
| flammability | float | 0.0 | 可燃性高于 0.3 会使其可用于物品燃烧器。 |
| radioactivity | float | 0.0 | 该物品的放射性有多强。 |
| charge | float | 0.0 | 该物品的导电能力有多强。 |
| hardness | int | 0 | 该物品的钻头硬度 |
| cost | float | 1.0 | 该物品的基础材料成本，用于计算放置时间；1 成本 = 建造时间增加 1 刻 |
| healthScaling | float | 0.0 | 当该物品出现在建造成本中时，方块的默认生命值会乘以 1 + scaling，其中 'scaling' 会对所有物品需求类型求和。 |
| lowPriority | boolean | false | 若为 true，该物品对钻头而言优先级最低。 |
| frames | int | 0 | 大于 0 时，该物品带动画。 |
| transitionFrames | int | 0 | 每帧之间生成的过渡帧数 |
| frameTime | float | 5.0 | 动画帧之间的间隔（刻）。 |
| buildable | boolean | true | 若为 true，该材料会被建筑使用。若为 false，该材料会在某些核心中被焚毁。 |
| hidden | boolean | false |  |
