# Weather

## Weather

*继承自 UnlockableContent*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| duration | float | 36000.0 | 该天气事件的默认持续时间（刻）。 |
| opacityMultiplier | float | 1.0 |  |
| attrs | Attributes | new Attributes() |  |
| sound | Sound | none |  |
| soundVol | float | 0.1 |  |
| soundVolMin | float | 0.0 |  |
| soundVolOscMag | float | 0.0 |  |
| soundVolOscScl | float | 20.0 |  |
| hidden | boolean | false |  |
| type | Prov of WeatherState | WeatherState::create |  |
| status | StatusEffect | none |  |
| statusDuration | float | 120.0 |  |
| statusAir | boolean | true |  |
| statusGround | boolean | true |  |
