# Liquid

## Liquid

*extends UnlockableContent*

A better name for this class would be "fluid", but it's too late for that.

| field | type | default | notes |
|---|---|---|---|
| gas | boolean | false | If true, this fluid is treated as a gas (and does not create puddles) |
| color | Color | 000000ff | Color used in pipes and on the ground. |
| gasColor | Color | bfbfbfff | Color of this liquid in gas form. |
| barColor | Color | null | Color used in bars. |
| lightColor | Color | 00000000 | Color used to draw lights. Note that the alpha channel is used to dictate brightness. |
| flammability | float | 0.0 | 0-1, 0 is completely not flammable, anything above that may catch fire when exposed to heat, 0.5+ is very flammable. |
| temperature | float | 0.5 | temperature: 0.5 is 'room' temperature, 0 is very cold, 1 is molten hot |
| heatCapacity | float | 0.5 | how much heat this liquid can store. 0.4=water (decent), anything lower is probably less dense and bad at cooling. |
| viscosity | float | 0.5 | how thick this liquid is. 0.5=water (relatively viscous), 1 would be something like tar (very slow). |
| explosiveness | float | 0.0 | how prone to exploding this liquid is, when heated. 0 = nothing, 1 = nuke |
| blockReactive | boolean | true | whether this fluid reacts in blocks at all (e.g. slag with water) |
| coolant | boolean | true | if false, this liquid cannot be a coolant |
| moveThroughBlocks | boolean | false | if true, this liquid can move through blocks as a puddle. |
| incinerable | boolean | true | if true, this liquid can be incinerated in the incinerator block. |
| effect | StatusEffect | none | The associated status effect. |
| particleEffect | Effect | none | Effect shown in puddles. |
| particleSpacing | float | 60.0 | Particle effect rate spacing in ticks. |
| boilPoint | float | 2.0 | Temperature at which this liquid vaporizes. This isn't just boiling. |
| capPuddles | boolean | true | If true, puddle size is capped. |
| vaporEffect | Effect | vapor | Effect when this liquid vaporizes. |
| hidden | boolean | false | If true, this liquid is hidden in most UI. |
| canStayOn | ObjectSet of Liquid | [] | Liquids this puddle can stay on, e.g. oil on water. |
