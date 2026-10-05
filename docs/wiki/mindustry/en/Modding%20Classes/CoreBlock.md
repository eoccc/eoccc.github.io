# CoreBlock

## CoreBlock

*extends StorageBlock*

| field | type | default | notes |
|---|---|---|---|
| thruster1 | TextureRegion | null |  |
| thruster2 | TextureRegion | null |  |
| thrusterLength | float | 3.5 |  |
| thrusterOffset | float | 0.0 |  |
| isFirstTier | boolean | false |  |
| allowSpawn | boolean | true | If false, players can't respawn at this core. |
| requiresCoreZone | boolean | false | If true, this core type requires a core zone to upgrade. |
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
