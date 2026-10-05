# ParticleEffect

内置常量：

`rand` `v` `none` `blockCrash` `trailFade` `unitSpawn` `unitCapKill` `unitEnvKill` `unitControl` `unitDespawn` `unitSpirit` `itemTransfer` `pointBeam` `pointHit` `hitScepterSecondary` `lightning` `coreBuildShockwave` `coreBuildBlock` `pointShockwave` `moveCommand` `attackCommand` `commandSend` `upgradeCore` `upgradeCoreBloom` `placeBlock` `coreLaunchConstruct` `tapBlock` `breakBlock` `payloadDeposit` `select` `smoke` `fallSmoke` `unitWreck` `rocketSmoke` `rocketSmokeLarge` `magmasmoke` `spawn` `unitAssemble` `padlaunch` `breakProp` `unitDrop` `unitLand` `unitDust` `unitLandSmall` `unitPickup` `crawlDust` `landShock` `pickup` `sparkExplosion` `titanExplosion` `titanExplosionLarge` `titanExplosionSmall` `titanExplosionFrag` `titanSmoke` `titanSmokeLarge` `titanSmokeSmall` `coreExplosion` `smokeAoeCloud` `missileTrailSmoke` `missileTrailSmokeSmall` `neoplasmSplat` `scatheExplosion` `scatheExplosionSmall` `scatheLight` `scatheLightSmall` `titanLightSmall` `scatheSlash` `dynamicSpikes` `greenBomb` `greenLaserCharge` `greenLaserChargeSmall` `greenCloud` `healWaveDynamic` `healWave` `heal` `dynamicWave` `shieldWave` `shieldApply` `disperseTrail` `hitBulletSmall` `hitBulletColor` `hitSquaresColor` `squareWaveEffect` `hitFuse` `hitBulletBig` `hitFlameSmall` `hitFlamePlasma` `hitLiquid` `hitLaserBlast` `hitEmpSpark` `hitLancer` `hitLancerLow` `hitBeam` `hitFlameBeam` `hitMeltdown` `hitMeltHeal` `instBomb` `instTrail` `instShoot` `instHit` `hitLaser` `hitLaserColor` `despawn` `airBubble` `flakExplosion` `plasticExplosion` `plasticExplosionFlak` `blastExplosion` `sapExplosion` `massiveExplosion` `artilleryTrail` `incendTrail` `missileTrail` `missileTrailShort` `bulletSparkSmokeTrailSmall` `colorTrail` `absorb` `forceShrink` `flakExplosionBig` `burning` `fireRemove` `fire` `fireHit` `fireSmoke` `neoplasmHeal` `steam` `ventSteam` `drillSteam` `fluxVapor` `corrosionVapor` `vapor` `vaporSmall` `fireballsmoke` `ballfire` `freezing` `melting` `wet` `muddy` `sapped` `electrified` `sporeSlowed` `oily` `overdriven` `overclocked` `dropItem` `shockwave` `shockwaveSmaller` `bigShockwave` `spawnShockwave` `podLandShockwave` `explosion` `dynamicExplosion` `reactorExplosion` `impactReactorExplosion` `blockExplosionSmoke` `steamCoolSmoke` `smokePuff` `shootSmall` `shootSmallColor` `shootHeal` `shootHealYellow` `shootSmallSmoke` `shootBig` `shootBig2` `shootBigColor` `shootScepterSecondary` `shootQuellPulse` `shootTitan` `shootBigSmoke` `shootBigSmoke2` `shootSmokeDisperse` `shootSmokeSquare` `shootSmokeSquareSparse` `shootSmokeSquareBig` `shootSmokeTitan` `shootSmokeSmite` `shootSmokeMissile` `shootSmokeMissileColor` `regenParticle` `regenSuppressParticle` `regenSuppressSeek` `surgeCruciSmoke` `neoplasiaSmoke` `heatReactorSmoke` `circleColorSpark` `colorSpark` `colorSparkBig` `randLifeSpark` `shootPayloadDriver` `shootSmallFlame` `shootPyraFlame` `shootLiquid` `casing1` `casing2` `casing3` `casing4` `casing2Double` `casing3Double` `railShoot` `railTrail` `railHit` `lancerLaserShoot` `lancerLaserShootSmoke` `lancerLaserCharge` `lancerLaserChargeBegin` `lightningCharge` `sparkShoot` `lightningShoot` `thoriumShoot` `reactorsmoke` `redgeneratespark` `turbinegenerate` `generatespark` `fuelburn` `incinerateSlag` `coreBurn` `plasticburn` `conveyorPoof` `pulverize` `pulverizeRed` `pulverizeSmall` `pulverizeMedium` `unitMine` `producesmoke` `artilleryTrailSmoke` `smokeCloud` `smeltsmoke` `coalSmeltsmoke` `formsmoke` `blastsmoke` `lava` `dooropen` `doorclose` `dooropenlarge` `doorcloselarge` `generate` `mineWallSmall` `mineSmall` `mine` `mineBig` `mineHuge` `mineImpact` `mineImpactWave` `payloadReceive` `teleportActivate` `teleport` `teleportOut` `ripple` `bubble` `launchAccelerator` `launch` `launchPod` `healWaveMend` `overdriveWave` `healBlock` `healBlockFull` `rotateBlock` `lightBlock` `overdriveBlockFull` `shieldBreak` `arcShieldBreak` `coreLandDust` `podLandDust` `unitShieldBreak` `chainLightning` `chainEmp` `legDestroy` `debugLine` `debugRect`

## ParticleEffect

*继承自 Effect*

最核心的效果类。可以创建各种形状的粒子。

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| colorFrom | Color | ffffffff | 粒子颜色。 |
| colorTo | Color | ffffffff | 粒子颜色。 |
| particles | int | 6 | 生成的粒子数量。 |
| randLength | boolean | true | 为 true 时，粒子长度在 0 到 length 之间随机取值。 |
| casingFlip | boolean | false | 使该效果可像弹壳效果一样翻转。 |
| cone | float | 180.0 |  |
| length | float | 20.0 |  |
| baseLength | float | 0.0 |  |
| interp | Interp | linear | 粒子尺寸/长度/半径的插值方式。 |
| sizeInterp | Interp | null | 粒子尺寸插值。为 null 时使用 interp。 |
| colorInterp | Interp | null | 粒子颜色插值。为 null 时使用 interp。 |
| offsetX | float | 0.0 | 粒子的偏移位置。 |
| offsetY | float | 0.0 | 粒子的偏移位置。 |
| lightScl | float | 2.0 | 粒子的光照属性。 |
| lightOpacity | float | 0.6 | 粒子的光照属性。 |
| lightColor | Color | null | 每个粒子发出光的颜色。 |
| spin | float | 0.0 | 每秒刻的旋转角度。 |
| sizeFrom | float | 2.0 | 控制精灵图的起始与结束尺寸。 |
| sizeTo | float | 0.0 | 控制精灵图的起始与结束尺寸。 |
| sizeChangeStart | float | 0.0 | 控制效果在改变尺寸前等待的刻数。 |
| widthChangeStart | float | 0.0 | 控制效果在改变宽度前等待的刻数。 |
| heightChangeStart | float | 0.0 | 控制效果在改变高度前等待的刻数。 |
| use旋转 | boolean | true | 旋转是否与父对象叠加 |
| offset | float | 0.0 | 旋转偏移。 |
| region | String | "circle" | 要绘制的精灵图。 |
| widthFrom | float | 1.0 | 粒子宽高相对其半径的比例属性，对线状粒子无效。 |
| widthTo | float | 1.0 | 粒子宽高相对其半径的比例属性，对线状粒子无效。 |
| heightFrom | float | 1.0 | 粒子宽高相对其半径的比例属性，对线状粒子无效。 |
| heightTo | float | 1.0 | 粒子宽高相对其半径的比例属性，对线状粒子无效。 |
| widthInterp | Interp | null | 粒子宽度插值。为 null 时使用 sizeInterp。 |
| heightInterp | Interp | null | 粒子高度插值。为 null 时使用 sizeInterp。 |
| line | boolean | false |  |
| strokeFrom | float | 2.0 |  |
| strokeTo | float | 0.0 |  |
| lenFrom | float | 4.0 |  |
| lenTo | float | 2.0 |  |
| cap | boolean | true |  |
