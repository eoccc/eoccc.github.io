# BulletType

Built-in constants:

`placeholder` `spaceLiquid` `damageLightning` `damageLightningGround` `damageLightningAir` `fireball`

## BulletType

| field | type | default | notes |
|---|---|---|---|
| lifetime | float | 40.0 | Lifetime in ticks. |
| lifeScaleRandMin | float | 1.0 | Min/max multipliers for lifetime applied to this bullet when spawned. |
| lifeScaleRandMax | float | 1.0 | Min/max multipliers for lifetime applied to this bullet when spawned. |
| speed | float | 1.0 | Speed in units/tick. |
| velocityScaleRandMin | float | 1.0 | Min/max multipliers for velocity applied to this bullet when spawned. |
| velocityScaleRandMax | float | 1.0 | Min/max multipliers for velocity applied to this bullet when spawned. |
| damage | float | 1.0 | Direct damage dealt on hit. |
| hitSize | float | 4.0 | Hitbox size. |
| drawSize | float | 40.0 | Clipping hitbox. |
| angleOffset | float | 0.0 | Angle offset applied to bullet when spawned each time. |
| randomAngleOffset | float | 0.0 | Angle offset applied to bullet when spawned each time. |
| drag | float | 0.0 | Drag as fraction of velocity. |
| accel | float | 0.0 | Acceleration per frame. |
| pierce | boolean | false | Whether to pierce units. |
| pierceBuilding | boolean | false | Whether to pierce buildings. |
| pierceCap | int | -1 | Maximum # of pierced objects. |
| pierceDamageFactor | float | 0.0 | Multiplier of damage decreased per health pierced. |
| maxDamageFraction | float | -1.0 | If positive, limits non-splash damage dealt to a fraction of the target's maximum health. |
| removeAfterPierce | boolean | true | If false, this bullet isn't removed after pierceCap is exceeded. Expert usage only. |
| laserAbsorb | boolean | true | For piercing lasers, setting this to true makes it get absorbed by plastanium walls. |
| laserBullet | boolean | false | Whether this bullet is considered a laser bullet and thus absorbed by plastanium walls. |
| optimalLifeFract | float | 0.0 | Life fraction at which this bullet has the best range/damage/etc. Used for lasers and continuous turrets. |
| layer | float | 100.0 | Z layer to drawn on. |
| hitEffect | Effect | hitBulletSmall | Effect shown on direct hit. |
| despawnEffect | Effect | hitBulletSmall | Effect shown when bullet despawns. |
| shootEffect | Effect | shootSmall | Effect created when shooting. |
| shootPattern | ShootPattern | null | Pattern used to shoot this bullet. If null, uses turret's default pattern. |
| chargeEffect | Effect | none | Effect created when charging starts; only usable in single-shot weapons with a firstShotDelay / shotDelay. |
| smokeEffect | Effect | shootSmallSmoke | Extra smoke effect created when shooting. |
| shootSound | Sound | none | Overrides the shoot sound in turrets if set. Does nothing in units, as they can't have multiple ammo types. |
| hitSound | Sound | none | Sound made when hitting something or getting removed. |
| despawnSound | Sound | none | Sound made when hitting something or getting removed. |
| hitSoundPitch | float | 1.0 | Pitch of the sound made when hitting something |
| hitSoundPitchRange | float | 0.1 | Pitch of the sound made when hitting something |
| hitSoundVolume | float | 1.0 | Volume of the sound made when hitting something |
| inaccuracy | float | 0.0 | Extra inaccuracy when firing. |
| ammoMultiplier | float | 2.0 | How many bullets get created per ammo item/liquid. |
| reloadMultiplier | float | 1.0 | Multiplied by turret reload speed to get final shoot speed. |
| buildingDamageMultiplier | float | 1.0 | Multiplier of how much base damage is done to tiles. |
| shieldDamageMultiplier | float | 1.0 | Multiplier of how much base damage is done to force shields. |
| recoil | float | 0.0 | Recoil from shooter entities. |
| killShooter | boolean | false | Whether to kill the shooter when this is shot. For suicide bombers. |
| instantDisappear | boolean | false | Whether to instantly make the bullet disappear. |
| splashDamage | float | 0.0 | Damage dealt in splash. 0 to disable. |
| scaledSplashDamage | boolean | false | If true, splash damage is "correctly" affected by unit hitbox size. Used for projectiles that do not collide / have splash as their main source of damage. |
| knockback | float | 0.0 | Knockback in velocity. |
| impact | boolean | false | Should knockback follow the bullet's direction |
| status | StatusEffect | none | Status effect applied on hit. |
| statusDuration | float | 480.0 | Intensity of applied status effect in terms of duration. |
| unitSort | Sortf | closest | Turret only. Function for choosing which unit to target. Overrides turret sorting |
| statusChance | float | 1.0 | Chance for this bullet to apply a status effect |
| targetBlocks | boolean | true | Turret only. If false, blocks will not be targeted. |
| targetMissiles | boolean | true | Turret only. If false, missiles will not be targeted. |
| collidesTiles | boolean | true | Whether this bullet type collides with tiles. |
| collidesTeam | boolean | false | Whether this bullet type collides with tiles that are of the same team. |
| collidesAir | boolean | true | Whether this bullet type collides with air/ground units. |
| collidesGround | boolean | true | Whether this bullet type collides with air/ground units. |
| collides | boolean | true | Whether this bullet types collides with anything at all. |
| collideFloor | boolean | false | If true, this projectile collides with non-surface floors. |
| collideTerrain | boolean | false | If true, this projectile collides with static walls |
| keepVelocity | boolean | true | Whether velocity is inherited from the shooter. |
| scaleKeepVelocity | boolean | false | If keepVelocity = true, whether to reduce lifetime proportionally to the added speed, making range consistent. |
| scaleLife | boolean | false | Whether to scale lifetime (not actually velocity!) to disappear at the target position. Used for artillery. |
| hittable | boolean | true | Whether this bullet can be hit by point defense. |
| reflectable | boolean | true | Whether this bullet can be reflected. |
| absorbable | boolean | true | Whether this projectile can be absorbed by shields. |
| ignoreSpawnAngle | boolean | false | If true, the angle param in create is ignored. |
| createChance | float | 1.0 | Chance for this bullet to be created. |
| maxRange | float | -1.0 | Bullet range positive override. |
| rangeOverride | float | -1.0 | When > 0, overrides range even if smaller than base range. |
| rangeChange | float | 0.0 | When used in a turret with multiple ammo types, this can be set to a non-zero value to influence range. |
| extraRangeMargin | float | 0.0 | When used in turrets with limitRange() applied, this adds extra range to the bullets that extends past targeting range. Only particularly relevant in vanilla. |
| range | float | 0.0 | Range initialized in init(). |
| minRangeChange | float | 0.0 | When used in a turret with multiple ammo types, this can be set to a non-zero value to influence minRange |
| healPercent | float | 0.0 | % of block health healed * |
| healAmount | float | 0.0 | flat amount of block health healed |
| healSound | Sound | blockHeal | sound played when a block is healed |
| healSoundVolume | float | 0.9 | volume of heal sound |
| lifesteal | float | 0.0 | Fraction of bullet damage that heals that shooter. |
| makeFire | boolean | false | Whether to make fire on impact |
| hitUnder | boolean | false | Whether this bullet will always hit blocks under it. |
| despawnHit | boolean | false | Whether to create hit effects on despawn. Forced to true if this bullet has any special effects like splash damage. Disable setDefaults to avoid override |
| fragOnHit | boolean | true | If true, this bullet will create bullets when it hits anything |
| fragOnDespawn | boolean | true | If true, this bullet will create bullets when it despawns |
| fragOnAbsorb | boolean | true | If false, this bullet will not create frags when absorbed by a shield. |
| pierceArmor | boolean | false | If true, unit armor is ignored in damage calculations. |
| armorMultiplier | float | 1.0 | Multiplies the unit/building armor used in damage calculations. Used for armor weakness, armor piercing, and anti-armor. |
| blockArmorMultiplier | float | 1.0 | Multiplies only the building armor used in damage calculations. |
| sticky | boolean | false | If true, the bullet will "stick" to enemies and get deactivated on collision. |
| stickyExtraLifetime | float | 0.0 | Extra time added to bullet when it sticks to something. |
| setDefaults | boolean | true | Whether status and despawnHit should automatically be set. |
| hitShake | float | 0.0 | Amount of shaking produced when this bullet hits something or despawns. |
| despawnShake | float | 0.0 | Amount of shaking produced when this bullet hits something or despawns. |
| fragBullet | BulletType | null | Bullet type that is created when this bullet expires. |
| delayFrags | boolean | false | If true, frag bullets are delayed to the next frame. Fixes obscure bugs with piercing bullet types spawning frags immediately and screwing up the Damage temporary variables. |
| fragRandomSpread | float | 360.0 | Degree spread range of fragmentation bullets. |
| fragSpread | float | 0.0 | Uniform spread between each frag bullet in degrees. |
| fragAngle | float | 0.0 | Angle offset of fragmentation bullets. |
| fragBullets | int | 9 | Number of fragmentation bullets created. |
| fragVelocityMin | float | 0.2 | Random range of frag velocity as a multiplier. |
| fragVelocityMax | float | 1.0 | Random range of frag velocity as a multiplier. |
| fragLifeMin | float | 1.0 | Random range of frag lifetime as a multiplier. |
| fragLifeMax | float | 1.0 | Random range of frag lifetime as a multiplier. |
| fragOffsetMin | float | 1.0 | Random offset of frag bullets from the parent bullet. |
| fragOffsetMax | float | 7.0 | Random offset of frag bullets from the parent bullet. |
| pierceFragCap | int | -1 | How many times this bullet can release frag bullets, if pierce = true. |
| intervalBullet | BulletType | null | Bullet that is created at a fixed interval. |
| bulletInterval | float | 20.0 | Interval, in ticks, between which bullet spawn. |
| intervalBullets | int | 1 | Number of bullet spawned per interval. |
| intervalRandomSpread | float | 360.0 | Random angle added to interval bullets. |
| intervalSpread | float | 0.0 | Angle spread between individual interval bullets. |
| intervalAngle | float | 0.0 | Angle offset for interval bullets. |
| intervalDelay | float | -1.0 | Use a negative value to disable interval bullet delay. |
| underwater | boolean | false | If true, this bullet is rendered underwater. Highly experimental! |
| hitColor | Color | ffffffff | Color used for hit/despawn effects. |
| healColor | Color | 98ffa9ff | Color used for block heal effects. |
| healEffect | Effect | healBlockFull | Effect emitted upon blocks that are healed. |
| spawnBullets | Seq of BulletType | [] | Bullets spawned when this bullet is created. Rarely necessary, used for visuals. |
| showStats | boolean | false | Whether to display the stats of the spawned bullet. |
| spawnBulletRandomSpread | float | 0.0 | Random angle spread of spawn bullets. |
| spawnUnit | UnitType | null | Unit spawned *instead of* this bullet. Useful for missiles. |
| despawnUnit | UnitType | null | Unit spawned when this bullet hits something or despawns due to it hitting the end of its lifetime. |
| despawnUnitChance | float | 1.0 | The chance for despawn units to spawn. |
| despawnUnitCount | int | 1 | Amount of units spawned when this bullet despawns. |
| despawnUnitRadius | float | 0.1 | Random offset distance from the original bullet despawn/hit coordinate. |
| faceOutwards | boolean | false | If true, units spawned when this bullet despawns face away from the bullet instead of the same direction as the bullet. |
| parts | Seq of DrawPart | [] | Extra visual parts for this bullet. |
| trailColor | Color | e58956ff | Color of trail behind bullet. |
| trailChance | float | -1.0E-4 | Chance of trail effect spawning on bullet per tick. |
| trailInterval | float | 0.0 | Uniform interval in which trail effect is spawned. |
| trailMinVelocity | float | 0.0 | Min velocity required for trail effect to spawn. |
| trailEffect | Effect | missileTrail | Trail effect that is spawned. |
| trailSpread | float | 0.0 | Random offset of trail effect. |
| trailParam | float | 2.0 | Rotation/size parameter that is passed to trail. Usually, this controls size. |
| trailRotation | boolean | false | Whether the parameter passed to the trail is the bullet rotation, instead of a flat value. |
| trailInterp | Interp | one | Interpolation for trail width as function of bullet lifetime |
| trailLength | int | -1 | Length of trail quads. Any value  0 |
| trailSinMag | float | 0.0 | If trailSinMag > 0, these values are applied as a sine curve to trail width. |
| trailSinScl | float | 3.0 | If trailSinMag > 0, these values are applied as a sine curve to trail width. |
| circleShooter | boolean | false | If true, the bullet will attempt to circle around its shooting entity. |
| circleShooterRadius | float | 13.0 | Radius that the bullet attempts to circle at. |
| circleShooterRadiusSmooth | float | 10.0 | Smooth extra radius value for circling. |
| circleShooterRotateSpeed | float | 0.3 | Multiplier of speed that is used to adjust velocity when circling. |
| splashDamageRadius | float | -1.0 | Use a negative value to disable splash damage. |
| splashDamagePierce | boolean | false | If true, splash damage pierces through tiles. |
| incendAmount | int | 0 | Amount of fires attempted around bullet. |
| incendSpread | float | 8.0 | Spread of fires around bullet. |
| incendChance | float | 1.0 | Chance of fire being created. |
| homingPower | float | 0.0 | Power of bullet ability. Usually a number between 0 and 1; try 0.1 as a starting point. |
| homingRange | float | 50.0 | Range of homing effect around bullet. |
| homingDelay | float | -1.0 | Use a negative value to disable homing delay. |
| followAimSpeed | float | 0.0 | Speed at which bullet rotates to follow cursor.  less vibration. |
| weaveMag | float | 0.0 | Intensity of bullet weaving. Note that this may make bullets inaccurate. |
| weaveRandom | boolean | true | If true, the bullet weave will randomly switch directions on spawn. |
| rotateSpeed | float | 0.0 | Rotation speed of the bullet velocity as it travels. |
| puddles | int | 0 | Number of individual puddles created. |
| puddleRange | float | 0.0 | Range of puddles around bullet position. |
| puddleAmount | float | 5.0 | Liquid count of each puddle created. |
| puddleLiquid | Liquid | water | Liquid that puddles created are made of. |
| displayAmmoMultiplier | boolean | true | Whether to display the ammo multiplayer for this bullet type in its stats. |
| statLiquidConsumed | float | 0.0 | If >0, this is displayed divided by the ammo multiplier. |
| lightRadius | float | -1.0 | Radius of light emitted by this bullet; <0 to use defaults. |
| lightOpacity | float | 0.3 | Opacity of light color. |
| lightColor | Color | fbd367ff | Color of light emitted by this bullet. |
