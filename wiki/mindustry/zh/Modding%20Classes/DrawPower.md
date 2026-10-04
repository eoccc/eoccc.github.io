# DrawPower

## DrawPower

*继承自 DrawBlock*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| emptyRegion | TextureRegion | null |  |
| fullRegion | TextureRegion | null |  |
| suffix | String | "-power" |  |
| drawPlan | boolean | true |  |
| mixcol | boolean | true | 若为 false，则在 emptyRegion 与 fullRegion 之间淡入淡出，而不是在空色与满色之间做 mixcol。 |
| emptyLightColor | Color | f8c266ff |  |
| fullLightColor | Color | fb9567ff |  |
| layer | float | -1.0 | 小于等于 0 的数值都会禁用图层切换。 |
