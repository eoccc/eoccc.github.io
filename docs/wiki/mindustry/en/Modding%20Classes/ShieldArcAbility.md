# ShieldArcAbility

## ShieldArcAbility

*extends Ability*

| field | type | default | notes |
|---|---|---|---|
| radius | float | 60.0 | Shield radius. |
| regen | float | 0.1 | Shield regen speed in damage/tick. |
| max | float | 200.0 | Maximum shield. |
| cooldown | float | 300.0 | Cooldown after the shield is broken, in ticks. |
| angle | float | 80.0 | Angle of shield arc. |
| angleOffset | float | 0.0 | Offset parameters for shield. |
| x | float | 0.0 | Offset parameters for shield. |
| y | float | 0.0 | Offset parameters for shield. |
| whenShooting | boolean | true | If true, only activates when shooting. |
| width | float | 6.0 | Width of shield line. |
| chanceDeflect | float | -1.0 | Bullet deflection chance. -1 to disable |
| reflectBuildingDamage | float | 1.0 | Multiplier for reflected bullet building damage. -1 to disable |
| reflectVel | float | 1.0 | Velocity multiplier for reflected bullets on the opposite axis. Negative values = concave, positive values = convex |
| reflectTime | float | 0.5 | Time multiplier for reflected bullets. |
| deflectSound | Sound | none | Deflection sound. |
| breakSound | Sound | shieldBreakSmall |  |
| hitSound | Sound | shieldHit |  |
| hitSoundVolume | float | 0.12 |  |
| missileUnitMultiplier | float | 2.0 | Multiplier for shield damage taken from missile units. |
| drawArc | boolean | true | Whether to draw the arc line. |
| region | String | null | If not null, will be drawn on top. |
| color | Color | null | Color override of the shield. Uses unit shield colour by default. |
| offsetRegion | boolean | false | If true, sprite position will be influenced by x/y. |
| pushUnits | boolean | true | If true, enemy units are pushed out. |
| pushDiffLayer | boolean | true | If pushUnits is true, allow ground units to push air or air units to push ground |
| pushEffect | Effect | circleColorSpark |  |
