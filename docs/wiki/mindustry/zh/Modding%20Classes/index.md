# 模组类文档

Mindustry 的模组内容由一系列 Java 类定义。本页收录全部 **262** 个类的字段、类型与默认值说明，按用途分类整理。

类名保留英文原样，以便与源码和 API 对照。

## 分类总览

| 分类 | 类数 | 说明 |
|---|---|---|
| [方块](#方块) | 18 | 方块基类与各类变体 |
| [生产与加工](#生产与加工) | 19 | 钻头、泵、制造机与加工设备 |
| [物流与载荷](#物流与载荷) | 28 | 传送带、管道、桥梁与载荷搬运 |
| [电力](#电力) | 16 | 发电、储能与电力分配 |
| [液体](#液体) | 9 | 液体容器与导管 |
| [武器与炮塔](#武器与炮塔) | 20 | 炮塔与武器定义 |
| [子弹与弹药](#子弹与弹药) | 25 | 各类子弹行为 |
| [单位](#单位) | 5 | 单位类型定义 |
| [能力](#能力) | 17 | 单位能力 |
| [效果](#效果) | 12 | 特效与视觉表现 |
| [绘制](#绘制) | 36 | 方块与单位的外观绘制 |
| [地形与贴图](#地形与贴图) | 13 | 地板、墙体与贴片 |
| [环境装饰](#环境装饰) | 6 | 树木、灌木与喷口 |
| [天气](#天气) | 3 | 天气效果 |
| [其他基础类型](#其他基础类型) | 35 | 内容与元数据基础类 |

## 使用方式

每个类的页面包含：字段名、类型、默认值与备注说明。字段名与类型名均为英文原样，便于直接对照源码。

> 需要了解这些类如何组合成完整内容，见[模组开发入门](../modding/1-modding/)；需要了解配置文件的书写格式，见[编程语言与数据格式](../../../langs/)。

## 方块

方块基类与各类变体，共 18 个类。

- [AirBlock](AirBlock.md)
- [Block](Block.md)
- [CanvasBlock](CanvasBlock.md)
- [CoreBlock](CoreBlock.md)
- [LightBlock](LightBlock.md)
- [LiquidBlock](LiquidBlock.md)
- [LogicBlock](LogicBlock.md)
- [MemoryBlock](MemoryBlock.md)
- [MessageBlock](MessageBlock.md)
- [OreBlock](OreBlock.md)
- [PayloadBlock](PayloadBlock.md)
- [PowerBlock](PowerBlock.md)
- [SpawnBlock](SpawnBlock.md)
- [StorageBlock](StorageBlock.md)
- [SwitchBlock](SwitchBlock.md)
- [TallBlock](TallBlock.md)
- [TreeBlock](TreeBlock.md)
- [UnitBlock](UnitBlock.md)

## 生产与加工

钻头、泵、制造机与加工设备，共 19 个类。

- [AttributeCrafter](AttributeCrafter.md)
- [BeamDrill](BeamDrill.md)
- [BurstDrill](BurstDrill.md)
- [Constructor](Constructor.md)
- [Drill](Drill.md)
- [GenericCrafter](GenericCrafter.md)
- [HeatCrafter](HeatCrafter.md)
- [HeatProducer](HeatProducer.md)
- [Incinerator](Incinerator.md)
- [ItemIncinerator](ItemIncinerator.md)
- [ItemSource](ItemSource.md)
- [ItemVoid](ItemVoid.md)
- [Pump](Pump.md)
- [Separator](Separator.md)
- [SingleBlockProducer](SingleBlockProducer.md)
- [SolidPump](SolidPump.md)
- [UnitAssembler](UnitAssembler.md)
- [UnitFactory](UnitFactory.md)
- [WallCrafter](WallCrafter.md)

## 物流与载荷

传送带、管道、桥梁与载荷搬运，共 28 个类。

- [ArmoredConveyor](ArmoredConveyor.md)
- [BufferedItemBridge](BufferedItemBridge.md)
- [Conveyor](Conveyor.md)
- [DirectionBridge](DirectionBridge.md)
- [DirectionalUnloader](DirectionalUnloader.md)
- [Duct](Duct.md)
- [DuctBridge](DuctBridge.md)
- [DuctJunction](DuctJunction.md)
- [DuctRouter](DuctRouter.md)
- [ItemBridge](ItemBridge.md)
- [Junction](Junction.md)
- [LandingPad](LandingPad.md)
- [LaunchPad](LaunchPad.md)
- [OverflowDuct](OverflowDuct.md)
- [OverflowGate](OverflowGate.md)
- [PayloadConveyor](PayloadConveyor.md)
- [PayloadDeconstructor](PayloadDeconstructor.md)
- [PayloadLoader](PayloadLoader.md)
- [PayloadMassDriver](PayloadMassDriver.md)
- [PayloadRouter](PayloadRouter.md)
- [PayloadSource](PayloadSource.md)
- [PayloadUnloader](PayloadUnloader.md)
- [PayloadVoid](PayloadVoid.md)
- [Router](Router.md)
- [Sorter](Sorter.md)
- [StackConveyor](StackConveyor.md)
- [StackRouter](StackRouter.md)
- [Unloader](Unloader.md)

## 电力

发电、储能与电力分配，共 16 个类。

- [Battery](Battery.md)
- [BeamNode](BeamNode.md)
- [ConsumeGenerator](ConsumeGenerator.md)
- [HeaterGenerator](HeaterGenerator.md)
- [ImpactReactor](ImpactReactor.md)
- [LongPowerNode](LongPowerNode.md)
- [NuclearReactor](NuclearReactor.md)
- [PowerDiode](PowerDiode.md)
- [PowerDistributor](PowerDistributor.md)
- [PowerGenerator](PowerGenerator.md)
- [PowerNode](PowerNode.md)
- [PowerSource](PowerSource.md)
- [PowerVoid](PowerVoid.md)
- [SolarGenerator](SolarGenerator.md)
- [ThermalGenerator](ThermalGenerator.md)
- [VariableReactor](VariableReactor.md)

## 液体

液体容器与导管，共 9 个类。

- [CellLiquid](CellLiquid.md)
- [DirectionLiquidBridge](DirectionLiquidBridge.md)
- [Liquid](Liquid.md)
- [LiquidBridge](LiquidBridge.md)
- [LiquidJunction](LiquidJunction.md)
- [LiquidRouter](LiquidRouter.md)
- [LiquidSource](LiquidSource.md)
- [LiquidVoid](LiquidVoid.md)
- [ShallowLiquid](ShallowLiquid.md)

## 武器与炮塔

炮塔与武器定义，共 20 个类。

- [BaseTurret](BaseTurret.md)
- [BuildTurret](BuildTurret.md)
- [BuildWeapon](BuildWeapon.md)
- [ContinuousLiquidTurret](ContinuousLiquidTurret.md)
- [ContinuousTurret](ContinuousTurret.md)
- [ItemTurret](ItemTurret.md)
- [LaserTurret](LaserTurret.md)
- [LiquidTurret](LiquidTurret.md)
- [MineWeapon](MineWeapon.md)
- [PayloadAmmoTurret](PayloadAmmoTurret.md)
- [PointDefenseBulletWeapon](PointDefenseBulletWeapon.md)
- [PointDefenseTurret](PointDefenseTurret.md)
- [PointDefenseWeapon](PointDefenseWeapon.md)
- [PowerTurret](PowerTurret.md)
- [ReloadTurret](ReloadTurret.md)
- [RepairBeamWeapon](RepairBeamWeapon.md)
- [RepairTurret](RepairTurret.md)
- [TractorBeamTurret](TractorBeamTurret.md)
- [Turret](Turret.md)
- [Weapon](Weapon.md)

## 子弹与弹药

各类子弹行为，共 25 个类。

- [ArtilleryBulletType](ArtilleryBulletType.md)
- [BasicBulletType](BasicBulletType.md)
- [BombBulletType](BombBulletType.md)
- [BulletType](BulletType.md)
- [ContinuousBulletType](ContinuousBulletType.md)
- [ContinuousFlameBulletType](ContinuousFlameBulletType.md)
- [ContinuousLaserBulletType](ContinuousLaserBulletType.md)
- [EmpBulletType](EmpBulletType.md)
- [EmptyBulletType](EmptyBulletType.md)
- [ExplosionBulletType](ExplosionBulletType.md)
- [FireBulletType](FireBulletType.md)
- [FlakBulletType](FlakBulletType.md)
- [InterceptorBulletType](InterceptorBulletType.md)
- [LaserBoltBulletType](LaserBoltBulletType.md)
- [LaserBulletType](LaserBulletType.md)
- [LightningBulletType](LightningBulletType.md)
- [LiquidBulletType](LiquidBulletType.md)
- [MissileBulletType](MissileBulletType.md)
- [MultiBulletType](MultiBulletType.md)
- [PointBulletType](PointBulletType.md)
- [PointLaserBulletType](PointLaserBulletType.md)
- [RailBulletType](RailBulletType.md)
- [SapBulletType](SapBulletType.md)
- [ShrapnelBulletType](ShrapnelBulletType.md)
- [SpaceLiquidBulletType](SpaceLiquidBulletType.md)

## 单位

单位类型定义，共 5 个类。

- [ErekirUnitType](ErekirUnitType.md)
- [MissileUnitType](MissileUnitType.md)
- [NeoplasmUnitType](NeoplasmUnitType.md)
- [TankUnitType](TankUnitType.md)
- [UnitType](UnitType.md)

## 能力

单位能力，共 17 个类。

- [Ability](Ability.md)
- [ArmorPlateAbility](ArmorPlateAbility.md)
- [EmptyDataAbility](EmptyDataAbility.md)
- [EnergyFieldAbility](EnergyFieldAbility.md)
- [ForceFieldAbility](ForceFieldAbility.md)
- [LiquidExplodeAbility](LiquidExplodeAbility.md)
- [LiquidRegenAbility](LiquidRegenAbility.md)
- [MoveEffectAbility](MoveEffectAbility.md)
- [MoveLightningAbility](MoveLightningAbility.md)
- [RegenAbility](RegenAbility.md)
- [RepairFieldAbility](RepairFieldAbility.md)
- [ShieldArcAbility](ShieldArcAbility.md)
- [ShieldRegenFieldAbility](ShieldRegenFieldAbility.md)
- [SpawnDeathAbility](SpawnDeathAbility.md)
- [StatusFieldAbility](StatusFieldAbility.md)
- [SuppressionFieldAbility](SuppressionFieldAbility.md)
- [UnitSpawnAbility](UnitSpawnAbility.md)

## 效果

特效与视觉表现，共 12 个类。

- [Effect](Effect.md)
- [ExplosionEffect](ExplosionEffect.md)
- [MultiEffect](MultiEffect.md)
- [NoiseEffect](NoiseEffect.md)
- [ParticleEffect](ParticleEffect.md)
- [RadialEffect](RadialEffect.md)
- [SeqEffect](SeqEffect.md)
- [SoundEffect](SoundEffect.md)
- [StatusEffect](StatusEffect.md)
- [TriangleEffect](TriangleEffect.md)
- [WaveEffect](WaveEffect.md)
- [WrapEffect](WrapEffect.md)

## 绘制

方块与单位的外观绘制，共 36 个类。

- [DrawArcSmelt](DrawArcSmelt.md)
- [DrawBlock](DrawBlock.md)
- [DrawBlockParts](DrawBlockParts.md)
- [DrawBlurSpin](DrawBlurSpin.md)
- [DrawBubbles](DrawBubbles.md)
- [DrawCells](DrawCells.md)
- [DrawCircles](DrawCircles.md)
- [DrawCrucibleFlame](DrawCrucibleFlame.md)
- [DrawCultivator](DrawCultivator.md)
- [DrawDefault](DrawDefault.md)
- [DrawFade](DrawFade.md)
- [DrawFlame](DrawFlame.md)
- [DrawFrames](DrawFrames.md)
- [DrawGlowRegion](DrawGlowRegion.md)
- [DrawHeatInput](DrawHeatInput.md)
- [DrawHeatOutput](DrawHeatOutput.md)
- [DrawHeatRegion](DrawHeatRegion.md)
- [DrawLiquidOutputs](DrawLiquidOutputs.md)
- [DrawLiquidRegion](DrawLiquidRegion.md)
- [DrawLiquidTile](DrawLiquidTile.md)
- [DrawMulti](DrawMulti.md)
- [DrawMultiWeave](DrawMultiWeave.md)
- [DrawParticles](DrawParticles.md)
- [DrawPistons](DrawPistons.md)
- [DrawPlasma](DrawPlasma.md)
- [DrawPower](DrawPower.md)
- [DrawPulseShape](DrawPulseShape.md)
- [DrawPumpLiquid](DrawPumpLiquid.md)
- [DrawRegion](DrawRegion.md)
- [DrawShape](DrawShape.md)
- [DrawSideRegion](DrawSideRegion.md)
- [DrawSoftParticles](DrawSoftParticles.md)
- [DrawSpikes](DrawSpikes.md)
- [DrawTurret](DrawTurret.md)
- [DrawWarmupRegion](DrawWarmupRegion.md)
- [DrawWeave](DrawWeave.md)

## 地形与贴图

地板、墙体与贴片，共 13 个类。

- [CharacterOverlay](CharacterOverlay.md)
- [ColoredFloor](ColoredFloor.md)
- [ColoredWall](ColoredWall.md)
- [EmptyFloor](EmptyFloor.md)
- [Floor](Floor.md)
- [OverlayFloor](OverlayFloor.md)
- [RemoveWall](RemoveWall.md)
- [RuneOverlay](RuneOverlay.md)
- [ShieldWall](ShieldWall.md)
- [StaticWall](StaticWall.md)
- [TiledFloor](TiledFloor.md)
- [TiledWall](TiledWall.md)
- [Wall](Wall.md)

## 环境装饰

树木、灌木与喷口，共 6 个类。

- [Prop](Prop.md)
- [SeaBush](SeaBush.md)
- [StaticProp](StaticProp.md)
- [StaticTree](StaticTree.md)
- [SteamVent](SteamVent.md)
- [WobbleProp](WobbleProp.md)

## 天气

天气效果，共 3 个类。

- [ParticleWeather](ParticleWeather.md)
- [RainWeather](RainWeather.md)
- [Weather](Weather.md)

## 其他基础类型

内容与元数据基础类，共 35 个类。

- [Accelerator](Accelerator.md)
- [ArmoredConduit](ArmoredConduit.md)
- [AutoDoor](AutoDoor.md)
- [BaseShield](BaseShield.md)
- [Cliff](Cliff.md)
- [Conduit](Conduit.md)
- [Door](Door.md)
- [ForceProjector](ForceProjector.md)
- [Fracker](Fracker.md)
- [HeatConductor](HeatConductor.md)
- [Item](Item.md)
- [LogicDisplay](LogicDisplay.md)
- [MagneticStorm](MagneticStorm.md)
- [MappableContent](MappableContent.md)
- [MassDriver](MassDriver.md)
- [MassDriverBolt](MassDriverBolt.md)
- [MendProjector](MendProjector.md)
- [OverdriveProjector](OverdriveProjector.md)
- [Radar](Radar.md)
- [Reconstructor](Reconstructor.md)
- [RegenProjector](RegenProjector.md)
- [RemoveOre](RemoveOre.md)
- [RepairTower](RepairTower.md)
- [Seaweed](Seaweed.md)
- [SectorPreset](SectorPreset.md)
- [ShockMine](ShockMine.md)
- [ShockwaveTower](ShockwaveTower.md)
- [SolarFlare](SolarFlare.md)
- [TargetDummy](TargetDummy.md)
- [Thruster](Thruster.md)
- [TileableLogicDisplay](TileableLogicDisplay.md)
- [UnitAssemblerModule](UnitAssemblerModule.md)
- [UnitCargoLoader](UnitCargoLoader.md)
- [UnitCargoUnloadPoint](UnitCargoUnloadPoint.md)
- [UnlockableContent](UnlockableContent.md)

