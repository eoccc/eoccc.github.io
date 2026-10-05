# TriangleEffect

内置常量：

`rand` `v` `none` `blockCrash` `trailFade` `unitSpawn` `unitCapKill` `unitEnvKill` `unitControl` `unitDespawn` `unitSpirit` `itemTransfer` `pointBeam` `pointHit` `hitScepterSecondary` `lightning` `coreBuildShockwave` `coreBuildBlock` `pointShockwave` `moveCommand` `attackCommand` `commandSend` `upgradeCore` `upgradeCoreBloom` `placeBlock` `coreLaunchConstruct` `tapBlock` `breakBlock` `payloadDeposit` `select` `smoke` `fallSmoke` `unitWreck` `rocketSmoke` `rocketSmokeLarge` `magmasmoke` `spawn` `unitAssemble` `padlaunch` `breakProp` `unitDrop` `unitLand` `unitDust` `unitLandSmall` `unitPickup` `crawlDust` `landShock` `pickup` `sparkExplosion` `titanExplosion` `titanExplosionLarge` `titanExplosionSmall` `titanExplosionFrag` `titanSmoke` `titanSmokeLarge` `titanSmokeSmall` `coreExplosion` `smokeAoeCloud` `missileTrailSmoke` `missileTrailSmokeSmall` `neoplasmSplat` `scatheExplosion` `scatheExplosionSmall` `scatheLight` `scatheLightSmall` `titanLightSmall` `scatheSlash` `dynamicSpikes` `greenBomb` `greenLaserCharge` `greenLaserChargeSmall` `greenCloud` `healWaveDynamic` `healWave` `heal` `dynamicWave` `shieldWave` `shieldApply` `disperseTrail` `hitBulletSmall` `hitBulletColor` `hitSquaresColor` `squareWaveEffect` `hitFuse` `hitBulletBig` `hitFlameSmall` `hitFlamePlasma` `hitLiquid` `hitLaserBlast` `hitEmpSpark` `hitLancer` `hitLancerLow` `hitBeam` `hitFlameBeam` `hitMeltdown` `hitMeltHeal` `instBomb` `instTrail` `instShoot` `instHit` `hitLaser` `hitLaserColor` `despawn` `airBubble` `flakExplosion` `plasticExplosion` `plasticExplosionFlak` `blastExplosion` `sapExplosion` `massiveExplosion` `artilleryTrail` `incendTrail` `missileTrail` `missileTrailShort` `bulletSparkSmokeTrailSmall` `colorTrail` `absorb` `forceShrink` `flakExplosionBig` `burning` `fireRemove` `fire` `fireHit` `fireSmoke` `neoplasmHeal` `steam` `ventSteam` `drillSteam` `fluxVapor` `corrosionVapor` `vapor` `vaporSmall` `fireballsmoke` `ballfire` `freezing` `melting` `wet` `muddy` `sapped` `electrified` `sporeSlowed` `oily` `overdriven` `overclocked` `dropItem` `shockwave` `shockwaveSmaller` `bigShockwave` `spawnShockwave` `podLandShockwave` `explosion` `dynamicExplosion` `reactorExplosion` `impactReactorExplosion` `blockExplosionSmoke` `steamCoolSmoke` `smokePuff` `shootSmall` `shootSmallColor` `shootHeal` `shootHealYellow` `shootSmallSmoke` `shootBig` `shootBig2` `shootBigColor` `shootScepterSecondary` `shootQuellPulse` `shootTitan` `shootBigSmoke` `shootBigSmoke2` `shootSmokeDisperse` `shootSmokeSquare` `shootSmokeSquareSparse` `shootSmokeSquareBig` `shootSmokeTitan` `shootSmokeSmite` `shootSmokeMissile` `shootSmokeMissileColor` `regenParticle` `regenSuppressParticle` `regenSuppressSeek` `surgeCruciSmoke` `neoplasiaSmoke` `heatReactorSmoke` `circleColorSpark` `colorSpark` `colorSparkBig` `randLifeSpark` `shootPayloadDriver` `shootSmallFlame` `shootPyraFlame` `shootLiquid` `casing1` `casing2` `casing3` `casing4` `casing2Double` `casing3Double` `railShoot` `railTrail` `railHit` `lancerLaserShoot` `lancerLaserShootSmoke` `lancerLaserCharge` `lancerLaserChargeBegin` `lightningCharge` `sparkShoot` `lightningShoot` `thoriumShoot` `reactorsmoke` `redgeneratespark` `turbinegenerate` `generatespark` `fuelburn` `incinerateSlag` `coreBurn` `plasticburn` `conveyorPoof` `pulverize` `pulverizeRed` `pulverizeSmall` `pulverizeMedium` `unitMine` `producesmoke` `artilleryTrailSmoke` `smokeCloud` `smeltsmoke` `coalSmeltsmoke` `formsmoke` `blastsmoke` `lava` `dooropen` `doorclose` `dooropenlarge` `doorcloselarge` `generate` `mineWallSmall` `mineSmall` `mine` `mineBig` `mineHuge` `mineImpact` `mineImpactWave` `payloadReceive` `teleportActivate` `teleport` `teleportOut` `ripple` `bubble` `launchAccelerator` `launch` `launchPod` `healWaveMend` `overdriveWave` `healBlock` `healBlockFull` `rotateBlock` `lightBlock` `overdriveBlockFull` `shieldBreak` `arcShieldBreak` `coreLandDust` `podLandDust` `unitShieldBreak` `chainLightning` `chainEmp` `legDestroy` `debugLine` `debugRect`

## TriangleEffect

*继承自 Effect*

创建一个参数高度可定制的三角形。

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| colorFrom | Color | ffffffff | 三角形颜色。 |
| colorTo | Color | ffffffff | 三角形颜色。 |
| flippable | boolean | false | 使该效果可像弹壳效果一样翻转。 |
| interp | Interp | linear | 三角形的位置插值，同时用作回退值。 |
| widthInterp | Interp | null | 宽度插值。Null 表示使用 interp。 |
| heightInterp | Interp | null | 高度插值。为 null 时使用 interp。 |
| colorInterp | Interp | null | 三角形的颜色插值。为 null 时使用 interp。 |
| startX | float | 0.0 | 控制三角形的起始与结束位置。 |
| startY | float | 0.0 | 控制三角形的起始与结束位置。 |
| endX | float | 0.0 | 控制三角形的起始与结束位置。 |
| endY | float | 0.0 | 控制三角形的起始与结束位置。 |
| lightScl | float | 8.0 | 三角形的光照属性。 |
| lightOpacityFrom | float | 0.6 | 三角形的光照属性。 |
| lightOpacityTo | float | 0.0 | 三角形的光照属性。 |
| lightColor | Color | null | 三角形发出光的颜色。 |
| widthFrom | float | 4.0 | 控制三角形各点的起始与结束位置。 |
| widthTo | float | 0.0 | 控制三角形各点的起始与结束位置。 |
| heightFrom | float | 4.0 | 控制三角形各点的起始与结束位置。 |
| heightTo | float | 4.0 | 控制三角形各点的起始与结束位置。 |
| use旋转 | boolean | true | 旋转是否与父对象叠加 |
| spin | int | 0 | 旋转角度（度/刻）。 |
| offset | float | 0.0 | 旋转偏移。 |
