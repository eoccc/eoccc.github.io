# ParticleEffect

Built-in constants:

`rand` `v` `none` `blockCrash` `trailFade` `unitSpawn` `unitCapKill` `unitEnvKill` `unitControl` `unitDespawn` `unitSpirit` `itemTransfer` `pointBeam` `pointHit` `hitScepterSecondary` `lightning` `coreBuildShockwave` `coreBuildBlock` `pointShockwave` `moveCommand` `attackCommand` `commandSend` `upgradeCore` `upgradeCoreBloom` `placeBlock` `coreLaunchConstruct` `tapBlock` `breakBlock` `payloadDeposit` `select` `smoke` `fallSmoke` `unitWreck` `rocketSmoke` `rocketSmokeLarge` `magmasmoke` `spawn` `unitAssemble` `padlaunch` `breakProp` `unitDrop` `unitLand` `unitDust` `unitLandSmall` `unitPickup` `crawlDust` `landShock` `pickup` `sparkExplosion` `titanExplosion` `titanExplosionLarge` `titanExplosionSmall` `titanExplosionFrag` `titanSmoke` `titanSmokeLarge` `titanSmokeSmall` `coreExplosion` `smokeAoeCloud` `missileTrailSmoke` `missileTrailSmokeSmall` `neoplasmSplat` `scatheExplosion` `scatheExplosionSmall` `scatheLight` `scatheLightSmall` `titanLightSmall` `scatheSlash` `dynamicSpikes` `greenBomb` `greenLaserCharge` `greenLaserChargeSmall` `greenCloud` `healWaveDynamic` `healWave` `heal` `dynamicWave` `shieldWave` `shieldApply` `disperseTrail` `hitBulletSmall` `hitBulletColor` `hitSquaresColor` `squareWaveEffect` `hitFuse` `hitBulletBig` `hitFlameSmall` `hitFlamePlasma` `hitLiquid` `hitLaserBlast` `hitEmpSpark` `hitLancer` `hitLancerLow` `hitBeam` `hitFlameBeam` `hitMeltdown` `hitMeltHeal` `instBomb` `instTrail` `instShoot` `instHit` `hitLaser` `hitLaserColor` `despawn` `airBubble` `flakExplosion` `plasticExplosion` `plasticExplosionFlak` `blastExplosion` `sapExplosion` `massiveExplosion` `artilleryTrail` `incendTrail` `missileTrail` `missileTrailShort` `bulletSparkSmokeTrailSmall` `colorTrail` `absorb` `forceShrink` `flakExplosionBig` `burning` `fireRemove` `fire` `fireHit` `fireSmoke` `neoplasmHeal` `steam` `ventSteam` `drillSteam` `fluxVapor` `corrosionVapor` `vapor` `vaporSmall` `fireballsmoke` `ballfire` `freezing` `melting` `wet` `muddy` `sapped` `electrified` `sporeSlowed` `oily` `overdriven` `overclocked` `dropItem` `shockwave` `shockwaveSmaller` `bigShockwave` `spawnShockwave` `podLandShockwave` `explosion` `dynamicExplosion` `reactorExplosion` `impactReactorExplosion` `blockExplosionSmoke` `steamCoolSmoke` `smokePuff` `shootSmall` `shootSmallColor` `shootHeal` `shootHealYellow` `shootSmallSmoke` `shootBig` `shootBig2` `shootBigColor` `shootScepterSecondary` `shootQuellPulse` `shootTitan` `shootBigSmoke` `shootBigSmoke2` `shootSmokeDisperse` `shootSmokeSquare` `shootSmokeSquareSparse` `shootSmokeSquareBig` `shootSmokeTitan` `shootSmokeSmite` `shootSmokeMissile` `shootSmokeMissileColor` `regenParticle` `regenSuppressParticle` `regenSuppressSeek` `surgeCruciSmoke` `neoplasiaSmoke` `heatReactorSmoke` `circleColorSpark` `colorSpark` `colorSparkBig` `randLifeSpark` `shootPayloadDriver` `shootSmallFlame` `shootPyraFlame` `shootLiquid` `casing1` `casing2` `casing3` `casing4` `casing2Double` `casing3Double` `railShoot` `railTrail` `railHit` `lancerLaserShoot` `lancerLaserShootSmoke` `lancerLaserCharge` `lancerLaserChargeBegin` `lightningCharge` `sparkShoot` `lightningShoot` `thoriumShoot` `reactorsmoke` `redgeneratespark` `turbinegenerate` `generatespark` `fuelburn` `incinerateSlag` `coreBurn` `plasticburn` `conveyorPoof` `pulverize` `pulverizeRed` `pulverizeSmall` `pulverizeMedium` `unitMine` `producesmoke` `artilleryTrailSmoke` `smokeCloud` `smeltsmoke` `coalSmeltsmoke` `formsmoke` `blastsmoke` `lava` `dooropen` `doorclose` `dooropenlarge` `doorcloselarge` `generate` `mineWallSmall` `mineSmall` `mine` `mineBig` `mineHuge` `mineImpact` `mineImpactWave` `payloadReceive` `teleportActivate` `teleport` `teleportOut` `ripple` `bubble` `launchAccelerator` `launch` `launchPod` `healWaveMend` `overdriveWave` `healBlock` `healBlockFull` `rotateBlock` `lightBlock` `overdriveBlockFull` `shieldBreak` `arcShieldBreak` `coreLandDust` `podLandDust` `unitShieldBreak` `chainLightning` `chainEmp` `legDestroy` `debugLine` `debugRect`

## ParticleEffect

*extends Effect*

The most essential effect class. Can create particles in various shapes.

| field | type | default | notes |
|---|---|---|---|
| colorFrom | Color | ffffffff | Particle color. |
| colorTo | Color | ffffffff | Particle color. |
| particles | int | 6 | Number of particles created. |
| randLength | boolean | true | If true, the particle's length is set in a random range from 0 to length. |
| casingFlip | boolean | false | Gives the effect flipping compatability like casing effects. |
| cone | float | 180.0 |  |
| length | float | 20.0 |  |
| baseLength | float | 0.0 |  |
| interp | Interp | linear | Particle size/length/radius interpolation. |
| sizeInterp | Interp | null | Particle size interpolation. Null to use interp. |
| colorInterp | Interp | null | Particle color interpolation. Null to use interp. |
| offsetX | float | 0.0 | Offset position of the particle. |
| offsetY | float | 0.0 | Offset position of the particle. |
| lightScl | float | 2.0 | Particle light properties. |
| lightOpacity | float | 0.6 | Particle light properties. |
| lightColor | Color | null | Color of the light each particle emits. |
| spin | float | 0.0 | Spin in degrees per tick. |
| sizeFrom | float | 2.0 | Controls the initial and final sprite sizes. |
| sizeTo | float | 0.0 | Controls the initial and final sprite sizes. |
| sizeChangeStart | float | 0.0 | Controls the amount of ticks the effect waits before changing size. |
| widthChangeStart | float | 0.0 | Controls the amount of ticks the effect waits before changing width. |
| heightChangeStart | float | 0.0 | Controls the amount of ticks the effect waits before changing height. |
| useRotation | boolean | true | Whether the rotation adds with the parent |
| offset | float | 0.0 | Rotation offset. |
| region | String | "circle" | Sprite to draw. |
| widthFrom | float | 1.0 | Particle width and height properties as a ratio of its radius. Does nothing to line particles. |
| widthTo | float | 1.0 | Particle width and height properties as a ratio of its radius. Does nothing to line particles. |
| heightFrom | float | 1.0 | Particle width and height properties as a ratio of its radius. Does nothing to line particles. |
| heightTo | float | 1.0 | Particle width and height properties as a ratio of its radius. Does nothing to line particles. |
| widthInterp | Interp | null | Particle width interpolation. Null to use sizeInterp. |
| heightInterp | Interp | null | Particle height interpolation. Null to use sizeInterp. |
| line | boolean | false |  |
| strokeFrom | float | 2.0 |  |
| strokeTo | float | 0.0 |  |
| lenFrom | float | 4.0 |  |
| lenTo | float | 2.0 |  |
| cap | boolean | true |  |
