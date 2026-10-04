# RepairFieldAbility

## RepairFieldAbility

*继承自 Ability*

| 字段 | 类型 | 默认值 | 备注 |
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
| sameTypeHealMult | float | 1.0 | 对同类型单位的治疗量乘以该数值。 |
| maxTargets | int | -1 | 可治疗的单位数量上限。 |
| smartHeal | boolean | false | 若为 true，该能力会考虑缺失生命值、目标数量、冷却时间……等。 |
| smartHealPercent | float | 0.0 | 若受伤单位的生命值百分比低于此值，就尽快治疗它。接近 1f 的值很可能浪费治疗潜力。 |
| smartHealStrength | float | 1.0 | 潜在治疗效率的倍率。数值高则群体治疗更高效，数值低则单体治疗更高效。 |
| smartDowntime | float | 480.0 | 若所有受伤单位至少在这么长时间内未被伤害，则无视阈值强制治疗它们。 |
| smartInterval | float | 20.0 | 发现至少一个受损单位时的治疗检查频率。 |
| randDesync | float | -1.0 | 用于检查受伤单位的随机初始装填倍率。便于一次性错开治疗者的计时器。 |
