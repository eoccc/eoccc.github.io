# SpawnDeathAbility

## SpawnDeathAbility

*继承自 Ability*

死亡时生成一定数量的单位。

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| unit | UnitType | null |  |
| amount | int | 1 |  |
| randAmount | int | 0 |  |
| spread | float | 8.0 | 所生成单位向外散开的随机范围。 |
| faceOutwards | boolean | true | 为 true 时，生成的单位朝中间向外的方向。 |
