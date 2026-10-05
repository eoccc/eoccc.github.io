# SectorPreset

## SectorPreset

*extends UnlockableContent*

| field | type | default | notes |
|---|---|---|---|
| generator | FileMapGenerator | mindustry.maps.generators.FileMapGenerator@3631bac6 |  |
| planet | Planet | serpulo |  |
| sector | Sector | serpulo#5 (sectorName) |  |
| captureWave | int | 0 |  |
| rules | Cons of Rules | winWave = captureWave |  |
| difficulty | float | 0.0 | Difficulty, 0-10. |
| startWaveTimeMultiplier | float | 2.0 |  |
| addStartingItems | boolean | false |  |
| noLighting | boolean | false |  |
| isLastSector | boolean | false | If true, this is the last sector in its planetary campaign. |
| requireUnlock | boolean | true | If true, this sector must be unlocked before landing is permitted. |
| showHidden | boolean | false | If true, the icon and name is shown, even when it's a 'hidden' always-unlocked sector. TODO: this field may be changed, not sure how it should work |
| showSectorLandInfo | boolean | true |  |
| overrideLaunchDefaults | boolean | false | If true, uses this sector's launch fields instead |
| allowLaunchSchematics | boolean | false | Whether to allow users to specify a custom launch schematic for this map. |
| allowLaunchLoadout | boolean | false | Whether to allow users to specify the resources they take to this map. |
| attackAfterWaves | boolean | false | If true, switches to attack mode after waves end. |
| originalPosition | int | 5 | The original position of this sector; used for migration. Internal use for vanilla campaign only! |
| shieldSectors | Seq of Sector | [] | Sectors that prevent this sector from being landed on until they are completed. |
| outline | boolean | true | Set to false to disable outline generation. |
| outlineRadius | int | 5 |  |
| outlineColor | Color | 454545ff |  |
