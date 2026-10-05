# AttributeCrafter

## AttributeCrafter

*extends GenericCrafter*

A crafter that gains efficiency from attribute tiles.

| field | type | default | notes |
|---|---|---|---|
| attribute | Attribute | heat |  |
| baseEfficiency | float | 1.0 | Base efficiency of the crafter. |
| maxBoost | float | 1.0 | Maximum efficiency/output boost from attributes. |
| minEfficiency | float | -1.0 | Minimum efficiency required to place this block. |
| displayEfficiency | boolean | true | Whether to show this bar in the UI. |
| displayScaledOutput | boolean | true | Whether to show this bar in the UI. |
| scaleLiquidConsumption | boolean | false | Whether liquid consumption scales with efficiency. |
| outputScale | float | 0.0 | Scaled output (yield) multiplier, scales with attribute. <=0 to disable. |
| boostScale | float | 1.0 | Scaled efficiency (speed) multiplier, scales with attribute. <=0 to disable. |
