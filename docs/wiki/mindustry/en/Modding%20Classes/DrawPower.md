# DrawPower

## DrawPower

*extends DrawBlock*

| field | type | default | notes |
|---|---|---|---|
| emptyRegion | TextureRegion | null |  |
| fullRegion | TextureRegion | null |  |
| suffix | String | "-power" |  |
| drawPlan | boolean | true |  |
| mixcol | boolean | true | If false, fades between emptyRegion and fullRegion instead of mixcol between empty and full colors. |
| emptyLightColor | Color | f8c266ff |  |
| fullLightColor | Color | fb9567ff |  |
| layer | float | -1.0 | Any number <=0 disables layer changes. |
