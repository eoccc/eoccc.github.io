# Liquid

## Liquid

*继承自 UnlockableContent*

这个类更好的名字应该是 "fluid"，但已经来不及了。

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| gas | boolean | false | 为 true 时，该流体按气体处理（不形成液洼） |
| color | Color | 000000ff | 管道与地面使用的颜色。 |
| gasColor | Color | bfbfbfff | 该液体呈气态时的颜色。 |
| barColor | Color | null | 条形图使用的颜色。 |
| lightColor | Color | 00000000 | 绘制灯光使用的颜色。注意 alpha 通道表示亮度。 |
| flammability | float | 0.0 | 0-1，0 表示完全不可燃；高于 0 的值受热时可能起火，0.5 以上极易燃。 |
| temperature | float | 0.5 | 温度：0.5 为“室温”，0 为极冷，1 为熔融高温 |
| heatCapacity | float | 0.5 | 该液体可储存多少热量。0.4=水（尚可），更低的值可能密度更小、冷却更差。 |
| viscosity | float | 0.5 | 该液体的黏稠程度。0.5=水（相对黏稠），1 则类似焦油（非常缓慢）。 |
| explosiveness | float | 0.0 | 该液体受热时爆炸的倾向。0 = 无，1 = 核弹 |
| blockReactive | boolean | true | 该流体是否会在方块中反应（例如熔渣与水） |
| coolant | boolean | true | 若为 false，该液体不能作为冷却液 |
| moveThroughBlocks | boolean | false | 若为 true，该液体可以水洼形式穿过方块。 |
| incinerable | boolean | true | 若为 true，该液体可在焚化炉方块中焚毁。 |
| effect | StatusEffect | none | 关联的状态效果。 |
| particleEffect | Effect | none | 在液洼中显示的效果。 |
| particleSpacing | float | 60.0 | 粒子效果的触发间隔（刻）。 |
| boilPoint | float | 2.0 | 该液体的汽化温度（不单指沸腾）。 |
| capPuddles | boolean | true | 为 true 时，液洼尺寸有上限。 |
| vaporEffect | Effect | vapor | 该液体汽化时的效果。 |
| hidden | boolean | false | 为 true 时，该液体在大多数界面中被隐藏。 |
| canStayOn | ObjectSet of Liquid | [] | 该液洼可停留的液体，例如水面上的油。 |
