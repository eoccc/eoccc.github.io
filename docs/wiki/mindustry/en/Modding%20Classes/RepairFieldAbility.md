# RepairFieldAbility

## RepairFieldAbility

*extends Ability*

| field | type | default | notes |
|---|---|---|---|
| amount | float | 1.0 |  |
| reload | float | 100.0 |  |
| range | float | 60.0 |  |
| healPercent | float | 0.0 |  |
| healEffect | Effect | heal |  |
| activeEffect | Effect | healWaveDynamic |  |
| sound | Sound | healWave |  |
| soundVolume | float | 0.5 |  |
| parentizeEffects | boolean | false |  |
| sameTypeHealMult | float | 1.0 | Multiplies healing to units of the same type by this amount. |
| maxTargets | int | -1 | Maximum number of units healed. |
| smartHeal | boolean | false | If true, this ability will consider missing hp, number of targets, cooldowns...etc. |
| smartHealPercent | float | 0.0 | If a damaged unit health % is lower than this heal it as soon as possible. Values close to 1f will likely waste healing potential. |
| smartHealStrength | float | 1.0 | A multiplier on potential healing efficiency. High values -> efficient aoe healing. Low values -> efficient single target healing. |
| smartDowntime | float | 480.0 | If all damaged units havent been hurt for at least this amount of time, force healing them, regardless of thresholds. |
| smartInterval | float | 20.0 | How often to check for healing when at least 1 damaged unit is found. |
| randDesync | float | -1.0 | Random initial reload multiplier to check for damaged units. Useful for desyncing healer timers once. |
