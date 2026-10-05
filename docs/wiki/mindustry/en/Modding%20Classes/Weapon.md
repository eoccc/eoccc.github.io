# Weapon

## Weapon

| field | type | default | notes |
|---|---|---|---|
| name | String | Weapon Name | displayed weapon region |
| bullet | BulletType | placeholder | bullet shot |
| ejectEffect | Effect | none | shell ejection effect |
| display | boolean | true | whether weapon should appear in the stats of a unit with this weapon |
| mirror | boolean | true | whether to create a flipped copy of this weapon upon initialization. default: true |
| flipSprite | boolean | false | whether to flip the weapon's sprite when rendering. internal use only - do not set! |
| alternate | boolean | true | whether to shoot the weapons in different arms one after another, rather than all at once; only valid when mirror = true |
| rotate | boolean | false | whether to rotate toward the target independently of unit |
| showStatSprite | boolean | true | Whether to show the sprite of the weapon in the database. |
| baseRotation | float | 0.0 | rotation at which this weapon starts at. |
| top | boolean | true | whether to draw the outline on top. |
| continuous | boolean | false | whether to hold the bullet in place while firing; it will still require reload. |
| alwaysContinuous | boolean | false | whether this weapon uses continuous fire without reloading; implies continuous = true |
| aimChangeSpeed | float | Infinity | Speed at which the turret can change its bullet "aim" distance. This is only used for point laser bullets. |
| controllable | boolean | true | whether this weapon can be aimed manually by players |
| aiControllable | boolean | true | whether this weapon can be automatically aimed by the unit |
| alwaysShooting | boolean | false | whether this weapon is always shooting, regardless of targets ore cone |
| autoTarget | boolean | false | whether to automatically target relevant units in update(); only works when controllable = false. |
| predictTarget | boolean | true | whether to perform target trajectory prediction |
| useAttackRange | boolean | true | if true, this weapon is used for attack range calculations |
| targetInterval | float | 40.0 | ticks to wait in-between targets |
| targetSwitchInterval | float | 70.0 | ticks to wait in-between targets |
| rotateSpeed | float | 20.0 | rotation speed of weapon when rotation is enabled, in degrees/t |
| reload | float | 1.0 | weapon reload in frames |
| inaccuracy | float | 0.0 | inaccuracy of degrees of each shot |
| shake | float | 0.0 | intensity and duration of each shot's screen shake |
| recoil | float | 1.5 | visual weapon knockback. |
| recoils | int | -1 | Number of additional counters for recoil. |
| recoilTime | float | -1.0 | time taken for weapon to return to starting position in ticks. uses reload time by default |
| recoilPow | float | 1.8 | power curve applied to visual recoil |
| cooldownTime | float | 20.0 | ticks to cool down the heat region |
| shootX | float | 0.0 | projectile/effect offsets from center of weapon |
| shootY | float | 3.0 | projectile/effect offsets from center of weapon |
| x | float | 5.0 | offsets of weapon position on unit |
| y | float | 0.0 | offsets of weapon position on unit |
| xRand | float | 0.0 | Random spread on the X/Y axis. |
| yRand | float | 0.0 | Random spread on the X/Y axis. |
| shoot | ShootPattern | new ShootPattern() | pattern used for bullets |
| shadow | float | -1.0 | radius of shadow drawn under the weapon; <0 to disable |
| velocityRnd | float | 0.0 | fraction of velocity that is random |
| extraVelocity | float | 0.0 | extra velocity that is added as a fraction |
| lifeRnd | float | 0.0 | fraction of lifetime that is random |
| extraLife | float | 0.0 | extra lifetime that is added as a fraction |
| shootCone | float | 5.0 | The half-radius of the cone in which shooting will start. |
| rotationLimit | float | 361.0 | Cone in which the weapon can rotate relative to its mount. |
| minWarmup | float | 0.0 | minimum weapon warmup before firing (this is not linear, do NOT use 1!) |
| shootWarmupSpeed | float | 0.1 | lerp speed for shoot warmup, only used for parts |
| smoothReloadSpeed | float | 0.15 | lerp speed for shoot warmup, only used for parts |
| linearWarmup | boolean | false | If true, shoot warmup is linear instead of a curve. |
| soundPitchMin | float | 0.8 | random sound pitch range |
| soundPitchMax | float | 1.0 | random sound pitch range |
| ignoreRotation | boolean | false | whether shooter rotation is ignored when shooting. |
| noAttack | boolean | false | If true, this weapon cannot be used to attack targets. |
| minShootVelocity | float | -1.0 | min velocity required for this weapon to shoot. -1 to disable the limit. |
| maxShootVelocity | float | -1.0 | max velocity at which this weapon to shoot. -1 to disable the limit. |
| parentizeEffects | boolean | false | should the shoot effects follow the unit (effects need followParent set to true for this to work) |
| otherSide | int | -1 | internal value used for alternation - do not change! |
| layerOffset | float | 0.0 | draw Z offset relative to the default value |
| activeSound | Sound | none | sound looped when shooting |
| activeSoundVolume | float | 1.0 | volume of active sound |
| shootSound | Sound | shoot | sound used for shooting |
| shootSoundVolume | float | 1.0 | volume of the shoot sound |
| initialShootSound | Sound | none | sound used when this weapon first fires; for continuous weapons only |
| chargeSound | Sound | none | sound used for weapons that have a delay |
| region | TextureRegion | null | displayed region (autoloaded) |
| heatRegion | TextureRegion | null | heat region, must be same size as region (optional) |
| cellRegion | TextureRegion | null | cell region, must be same size as region (optional) |
| outlineRegion | TextureRegion | null | outline region to display if top is false |
| heatColor | Color | ab3400ff | heat region tint |
| shootStatus | StatusEffect | none | status effect applied when shooting |
| mountType | Func of Weapon, WeaponMount | WeaponMount::new | type of weapon mount to be used |
| shootStatusDuration | float | 300.0 | status effect duration when shot |
| shootOnDeath | boolean | false | whether this weapon should fire when its owner dies |
| shootOnDeathEffect | Effect | null | If not null and shootOnDeath == true, overrides the weapon's shoot effect only when its owner dies. |
| parts | Seq of DrawPart | [] | extra animated parts |
