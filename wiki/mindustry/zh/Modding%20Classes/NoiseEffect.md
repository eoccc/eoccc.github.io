# NoiseEffect

内置常量：

`rand` `v` `none` `blockCrash` `trailFade` `unitSpawn` `unitCapKill` `unitEnvKill` `unitControl` `unitDespawn` `unitSpirit` `itemTransfer` `pointBeam` `pointHit` `hitScepterSecondary` `lightning` `coreBuildShockwave` `coreBuildBlock` `pointShockwave` `moveCommand` `attackCommand` `commandSend` `upgradeCore` `upgradeCoreBloom` `placeBlock` `coreLaunchConstruct` `tapBlock` `breakBlock` `payloadDeposit` `select` `smoke` `fallSmoke` `unitWreck` `rocketSmoke` `rocketSmokeLarge` `magmasmoke` `spawn` `unitAssemble` `padlaunch` `breakProp` `unitDrop` `unitLand` `unitDust` `unitLandSmall` `unitPickup` `crawlDust` `landShock` `pickup` `sparkExplosion` `titanExplosion` `titanExplosionLarge` `titanExplosionSmall` `titanExplosionFrag` `titanSmoke` `titanSmokeLarge` `titanSmokeSmall` `coreExplosion` `smokeAoeCloud` `missileTrailSmoke` `missileTrailSmokeSmall` `neoplasmSplat` `scatheExplosion` `scatheExplosionSmall` `scatheLight` `scatheLightSmall` `titanLightSmall` `scatheSlash` `dynamicSpikes` `greenBomb` `greenLaserCharge` `greenLaserChargeSmall` `greenCloud` `healWaveDynamic` `healWave` `heal` `dynamicWave` `shieldWave` `shieldApply` `disperseTrail` `hitBulletSmall` `hitBulletColor` `hitSquaresColor` `squareWaveEffect` `hitFuse` `hitBulletBig` `hitFlameSmall` `hitFlamePlasma` `hitLiquid` `hitLaserBlast` `hitEmpSpark` `hitLancer` `hitLancerLow` `hitBeam` `hitFlameBeam` `hitMeltdown` `hitMeltHeal` `instBomb` `instTrail` `instShoot` `instHit` `hitLaser` `hitLaserColor` `despawn` `airBubble` `flakExplosion` `plasticExplosion` `plasticExplosionFlak` `blastExplosion` `sapExplosion` `massiveExplosion` `artilleryTrail` `incendTrail` `missileTrail` `missileTrailShort` `bulletSparkSmokeTrailSmall` `colorTrail` `absorb` `forceShrink` `flakExplosionBig` `burning` `fireRemove` `fire` `fireHit` `fireSmoke` `neoplasmHeal` `steam` `ventSteam` `drillSteam` `fluxVapor` `corrosionVapor` `vapor` `vaporSmall` `fireballsmoke` `ballfire` `freezing` `melting` `wet` `muddy` `sapped` `electrified` `sporeSlowed` `oily` `overdriven` `overclocked` `dropItem` `shockwave` `shockwaveSmaller` `bigShockwave` `spawnShockwave` `podLandShockwave` `explosion` `dynamicExplosion` `reactorExplosion` `impactReactorExplosion` `blockExplosionSmoke` `steamCoolSmoke` `smokePuff` `shootSmall` `shootSmallColor` `shootHeal` `shootHealYellow` `shootSmallSmoke` `shootBig` `shootBig2` `shootBigColor` `shootScepterSecondary` `shootQuellPulse` `shootTitan` `shootBigSmoke` `shootBigSmoke2` `shootSmokeDisperse` `shootSmokeSquare` `shootSmokeSquareSparse` `shootSmokeSquareBig` `shootSmokeTitan` `shootSmokeSmite` `shootSmokeMissile` `shootSmokeMissileColor` `regenParticle` `regenSuppressParticle` `regenSuppressSeek` `surgeCruciSmoke` `neoplasiaSmoke` `heatReactorSmoke` `circleColorSpark` `colorSpark` `colorSparkBig` `randLifeSpark` `shootPayloadDriver` `shootSmallFlame` `shootPyraFlame` `shootLiquid` `casing1` `casing2` `casing3` `casing4` `casing2Double` `casing3Double` `railShoot` `railTrail` `railHit` `lancerLaserShoot` `lancerLaserShootSmoke` `lancerLaserCharge` `lancerLaserChargeBegin` `lightningCharge` `sparkShoot` `lightningShoot` `thoriumShoot` `reactorsmoke` `redgeneratespark` `turbinegenerate` `generatespark` `fuelburn` `incinerateSlag` `coreBurn` `plasticburn` `conveyorPoof` `pulverize` `pulverizeRed` `pulverizeSmall` `pulverizeMedium` `unitMine` `producesmoke` `artilleryTrailSmoke` `smokeCloud` `smeltsmoke` `coalSmeltsmoke` `formsmoke` `blastsmoke` `lava` `dooropen` `doorclose` `dooropenlarge` `doorcloselarge` `generate` `mineWallSmall` `mineSmall` `mine` `mineBig` `mineHuge` `mineImpact` `mineImpactWave` `payloadReceive` `teleportActivate` `teleport` `teleportOut` `ripple` `bubble` `launchAccelerator` `launch` `launchPod` `healWaveMend` `overdriveWave` `healBlock` `healBlockFull` `rotateBlock` `lightBlock` `overdriveBlockFull` `shieldBreak` `arcShieldBreak` `coreLandDust` `podLandDust` `unitShieldBreak` `chainLightning` `chainEmp` `legDestroy` `debugLine` `debugRect`

## NoiseEffect

*继承自 Effect*

在相机视野上渲染噪声层的效果。

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| noisePath | String | png" |  |
| color | Color | null |  |
| noiseScl | float | 1000.0 |  |
| opacity | float | 0.3 |  |
| baseSpeed | float | 0.4 |  |
| intensity | float | 1.0 |  |
| windX | float | 1.0 |  |
| windY | float | 0.0 |  |
| layers | int | 4 |  |
| layerSpeedMul | float | -1.3 |  |
| layerAlphaMul | float | 0.7 |  |
| layerSclMul | float | 0.8 |  |
| layerColorMul | float | 0.9 |  |
| tex | Texture | null |  |
