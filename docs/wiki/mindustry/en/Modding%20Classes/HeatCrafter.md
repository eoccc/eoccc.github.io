# HeatCrafter

## HeatCrafter

*extends GenericCrafter*

A crafter that requires contact from heater blocks to craft.

| field | type | default | notes |
|---|---|---|---|
| heatRequirement | float | 10.0 | Base heat requirement for 100% efficiency. |
| overheatScale | float | 1.0 | After heat meets this requirement, excess heat will be scaled by this number. |
| maxEfficiency | float | 4.0 | Maximum possible efficiency after overheat. |
