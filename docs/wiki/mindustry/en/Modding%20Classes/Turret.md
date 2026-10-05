# Turret

## Turret

*extends ReloadTurret*

| field | type | default | notes |
|---|---|---|---|
| timerTarget | int | 1 |  |
| targetInterval | float | 20.0 | Ticks between attempt at finding a target. |
| newTargetInterval | float | -1.0 | Target interval for when this turret already has a valid target. -1 = targetInterval |
| maxAmmo | int | 30 | Maximum ammo units stored. |
| ammoPerShot | int | 1 | Ammo units used per shot. |
| consumeAmmoOnce | boolean | true | If true, ammo is only consumed once per shot regardless of bullet count. |
| heatRequirement | float | -1.0 | Minimum input heat required to fire. |
| maxHeatEfficiency | float | 3.0 | Maximum efficiency possible, if this turret uses heat. |
| inaccuracy | float | 0.0 | Bullet angle randomness in degrees. |
| velocityRnd | float | 0.0 | Fraction of bullet velocity that is random. |
| extraVelocity | float | 0.0 | extra velocity that is added as a fraction |
| lifeRnd | float | 0.0 | fraction of lifetime that is random |
| extraLife | float | 0.0 | extra lifetime that is added as a fraction |
| scaleLifetimeOffset | float | 0.0 | Fraction of lifetime that is added to bullets with lifeScale. |
| shootCone | float | 8.0 | Maximum angle difference in degrees at which turret will still try to shoot. |
| shootX | float | 0.0 | Turret shoot point. |
| shootY | float | -Infinity | Turret shoot point. |
| xRand | float | 0.0 | Random spread on the X axis. |
| drawMinRange | boolean | false | If true, a range ring is also drawn for minRange. |
| trackingRange | float | 0.0 | Range at which it finds and locks on to the target, but does not shoot. |
| minRange | float | 0.0 | Minimum bullet range. Used for artillery only. |
| minWarmup | float | 0.0 | Minimum warmup needed to fire. |
| accurateDelay | boolean | true | If true, this turret will accurately target moving targets with respect to shoot.firstShotDelay. |
| moveWhileCharging | boolean | true | If false, this turret can't move while charging. |
| reloadWhileCharging | boolean | true | If false, this turret can't reload while charging |
| warmupMaintainTime | float | 0.0 | How long warmup is maintained even if this turret isn't shooting. |
| shoot | ShootPattern | new ShootPattern() | pattern used for bullets |
| targetAir | boolean | true | If true, this block targets air units. |
| targetGround | boolean | true | If true, this block targets ground units and structures. |
| targetBlocks | boolean | true | If true, this block targets blocks. |
| targetHealing | boolean | false | If true, this block targets friend blocks, to heal them. |
| playerControllable | boolean | true | If true, this turret can be controlled by players. |
| displayAmmoMultiplier | boolean | true | If true, this block will display ammo multipliers in its stats (irrelevant for certain types of turrets). |
| targetUnderBlocks | boolean | true | If false, 'under' blocks like conveyors are not targeted. |
| alwaysShooting | boolean | false | If true, the turret will always shoot when it has ammo, regardless of targets in range or any control. |
| predictTarget | boolean | true | Whether this turret predicts unit movement. |
| unitSort | Sortf | closest | Function for choosing which unit to target. |
| unitFilter | Boolf of Unit | {code} | Filter for types of units to attack. |
| buildingFilter | Boolf of Building | underBullets | Filter for types of buildings to attack. |
| heatColor | Color | ab3400ff | Color of heat region drawn on top (if found) |
| shootEffect | Effect | null | Optional override for all shoot effects. |
| smokeEffect | Effect | null | Optional override for all smoke effects. |
| ammoUseEffect | Effect | none | Effect created when ammo is used. Not optional. |
| shootSound | Sound | shootDuo | Sound emitted when a single bullet is shot. |
| shootSoundVolume | float | 1.0 | Volume of shooting sound. |
| chargeSound | Sound | none | Sound emitted when shoot.firstShotDelay is >0 and shooting begins. |
| loopSound | Sound | none | The sound that this block makes while active. One sound loop. Do not overuse. |
| loopSoundVolume | float | 0.5 | Active sound base volume. |
| soundPitchMin | float | 0.9 | Range for pitch of shoot sound. |
| soundPitchMax | float | 1.1 | Range for pitch of shoot sound. |
| ammoEjectBack | float | 1.0 | Backwards Y offset of ammo eject effect. |
| shootWarmupSpeed | float | 0.1 | Lerp speed of turret warmup. |
| linearWarmup | boolean | false | If true, turret warmup is linear instead of a curve. |
| recoil | float | 1.0 | Visual amount by which the turret recoils back per shot. |
| recoils | int | -1 | Number of additional counters for recoil. |
| recoilTime | float | -1.0 | ticks taken for turret to return to starting position in ticks. uses reload time by default |
| recoilPow | float | 1.8 | power curve applied to visual recoil |
| cooldownTime | float | 20.0 | ticks to cool down the heat region |
| elevation | float | -1.0 | Visual elevation of turret shadow, -1 to use defaults. |
| shake | float | 0.0 | How much the screen shakes per shot. |
| drawer | DrawBlock | new DrawTurret() | Defines drawing behavior for this turret. |
