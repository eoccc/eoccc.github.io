# SolidPump

## SolidPump

*extends Pump*

Pump that makes liquid from solids and takes in power. Only works on solid floor blocks.

| field | type | default | notes |
|---|---|---|---|
| result | Liquid | water |  |
| updateEffect | Effect | none |  |
| updateEffectChance | float | 0.02 |  |
| rotateSpeed | float | 1.0 |  |
| baseEfficiency | float | 1.0 |  |
| attribute | Attribute | null | Attribute that is checked when calculating output. |
| rotatorRegion | TextureRegion | null |  |
