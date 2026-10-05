# Weather

## Weather

*extends UnlockableContent*

| field | type | default | notes |
|---|---|---|---|
| duration | float | 36000.0 | Default duration of this weather event in ticks. |
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
