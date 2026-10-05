# CoreBlock

## CoreBlock

*继承自 StorageBlock*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| thruster1 | TextureRegion | null |  |
| thruster2 | TextureRegion | null |  |
| thrusterLength | float | 3.5 |  |
| thrusterOffset | float | 0.0 |  |
| isFirstTier | boolean | false |  |
| allowSpawn | boolean | true | 为 false 时玩家无法在该核心重生。 |
| requiresCoreZone | boolean | false | 为 true 时，该核心类型需要核心区才能升级。 |
| incinerateNonBuildable | boolean | false |  |
| unitType | UnitType | alpha |  |
| landDuration | float | 160.0 |  |
| landMusic | Music | land |  |
| launchSoundVolume | float | 1.0 |  |
| landSoundVolume | float | 1.0 |  |
| launchSound | Sound | coreLaunch |  |
| landSound | Sound | coreLand |  |
| launchEffect | Effect | launch |  |
| landZoomInterp | Interp | pow3 |  |
| landZoomFrom | float | 0.02 |  |
| landZoomTo | float | 4.0 |  |
| captureInvicibility | float | 900.0 |  |
