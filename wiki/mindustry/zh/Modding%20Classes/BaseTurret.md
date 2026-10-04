# BaseTurret

## BaseTurret

*继承自 Block*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| range | float | 80.0 |  |
| placeOverlapMargin | float | 56.0 |  |
| rotateSpeed | float | 5.0 |  |
| fogRadiusMultiplier | float | 1.0 |  |
| disableOverlapCheck | boolean | false |  |
| activationTime | float | 0.0 | 放置后开始射击所需的等待时间。 |
| coolEffect | Effect | fuelburn | 使用冷却液时显示的效果。 |
| coolantMultiplier | float | 5.0 | 每单位热容液体可降低的装填时间。 |
| coolant | ConsumeLiquidBase | null | 非 null 时，该消耗器将用于冷却液。 |
