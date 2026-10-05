# ArmorPlateAbility

## ArmorPlateAbility

*extends Ability*

| field | type | default | notes |
|---|---|---|---|
| plateRegion | TextureRegion | null |  |
| shineRegion | TextureRegion | null |  |
| plateSuffix | String | "-armor" |  |
| shineSuffix | String | "-shine" |  |
| color | Color | null | Color of the shine. If null, uses team color. |
| shineSpeed | float | 1.0 |  |
| z | float | -1.0 |  |
| drawPlate | boolean | true | Whether to draw the plate region. |
| drawShine | boolean | true | Whether to draw the shine over the plate region. |
| healthMultiplier | float | 0.2 |  |
