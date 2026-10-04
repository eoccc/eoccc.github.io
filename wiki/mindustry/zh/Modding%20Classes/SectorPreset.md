# SectorPreset

## SectorPreset

*继承自 UnlockableContent*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| generator | FileMapGenerator | mindustry.maps.generators.FileMapGenerator@3631bac6 |  |
| planet | Planet | serpulo |  |
| sector | Sector | serpulo#5 (sectorName) |  |
| captureWave | int | 0 |  |
| rules | Cons of Rules | winWave = captureWave |  |
| difficulty | float | 0.0 | 难度，0-10。 |
| startWaveTimeMultiplier | float | 2.0 |  |
| addStartingItems | boolean | false |  |
| noLighting | boolean | false |  |
| isLastSector | boolean | false | 为 true 时，这是该星球战役的最后一个区块。 |
| requireUnlock | boolean | true | 为 true 时，该区块必须先解锁才能降落。 |
| showHidden | boolean | false | 若为 true，即使它是“隐藏的”始终解锁区块，也会显示图标和名称。TODO：此字段可能会改动，尚不确定它应如何工作 |
| showSectorLandInfo | boolean | true |  |
| overrideLaunchDefaults | boolean | false | 为 true 时，改用该区块的发射场 |
| allowLaunchSchematics | boolean | false | 是否允许用户为该地图指定自定义发射蓝图。 |
| allowLaunchLoadout | boolean | false | 是否允许用户指定他们带入该地图的资源。 |
| attackAfterWaves | boolean | false | 为 true 时，波次结束后切换到攻击模式。 |
| originalPosition | int | 5 | 该区块的原始位置；用于迁移。仅供原版战役内部使用！ |
| shieldSectors | Seq of Sector | [] | 在完成之前会阻止降落至该区块的其它区块。 |
| outline | boolean | true | 设为 false 以禁用轮廓生成。 |
| outlineRadius | int | 5 |  |
| outlineColor | Color | 454545ff |  |
