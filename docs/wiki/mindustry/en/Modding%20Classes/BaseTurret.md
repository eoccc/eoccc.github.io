# BaseTurret

## BaseTurret

*extends Block*

| field | type | default | notes |
|---|---|---|---|
| range | float | 80.0 |  |
| placeOverlapMargin | float | 56.0 |  |
| rotateSpeed | float | 5.0 |  |
| fogRadiusMultiplier | float | 1.0 |  |
| disableOverlapCheck | boolean | false |  |
| activationTime | float | 0.0 | How much time to start shooting after placement. |
| coolEffect | Effect | fuelburn | Effect displayed when coolant is used. |
| coolantMultiplier | float | 5.0 | How much reload is lowered by for each unit of liquid of heat capacity. |
| coolant | ConsumeLiquidBase | null | If not null, this consumer will be used for coolant. |
