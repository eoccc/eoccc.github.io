# ShieldArcAbility

## ShieldArcAbility

*继承自 Ability*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| radius | float | 60.0 | 护盾半径。 |
| regen | float | 0.1 | 护盾回复速度（伤害/刻）。 |
| max | float | 200.0 | 护盾上限。 |
| cooldown | float | 300.0 | 护盾破碎后的冷却时间（刻）。 |
| angle | float | 80.0 | 护盾弧的角度。 |
| angleOffset | float | 0.0 | 护盾的偏移参数。 |
| x | float | 0.0 | 护盾的偏移参数。 |
| y | float | 0.0 | 护盾的偏移参数。 |
| whenShooting | boolean | true | 为 true 时，仅在射击时激活。 |
| width | float | 6.0 | Width of shield line. |
| chanceDeflect | float | -1.0 | 子弹偏转概率。-1 表示禁用 |
| reflectBuildingDamage | float | 1.0 | 反弹子弹对建筑伤害的倍率。-1 表示禁用 |
| reflectVel | float | 1.0 | 被反射弹药在相反轴上的速度倍率。负值 = 凹，正值 = 凸 |
| reflectTime | float | 0.5 | 反弹子弹的时间倍率。 |
| deflectSound | Sound | none | 偏转音效。 |
| breakSound | Sound | shieldBreakSmall |  |
| hitSound | Sound | shieldHit |  |
| hitSoundVolume | float | 0.12 |  |
| missileUnitMultiplier | float | 2.0 | 受到导弹单位护盾伤害的倍率。 |
| drawArc | boolean | true | 是否绘制弧线。 |
| region | String | null | 非 null 时绘制在顶层。 |
| color | Color | null | 护盾颜色的覆盖值，默认使用单位护盾颜色。 |
| offsetRegion | boolean | false | 为 true 时，精灵图位置会受 x/y 影响。 |
| pushUnits | boolean | true | 为 true 时，敌方单位会被推出。 |
| pushDiffLayer | boolean | true | 当 pushUnits 为 true 时，允许地面单位推动空中单位，或空中单位推动地面单位 |
| pushEffect | Effect | circleColorSpark |  |
