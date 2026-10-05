# RepairBeamWeapon

## RepairBeamWeapon

*extends Weapon*

Note that this weapon requires a bullet with a positive maxRange.
Rotation must be set to true. Fixed repair points are not supported.

| field | type | default | notes |
|---|---|---|---|
| targetBuildings | boolean | false |  |
| targetUnits | boolean | true |  |
| repairSpeed | float | 0.3 |  |
| fractionRepairSpeed | float | 0.0 |  |
| beamWidth | float | 1.0 |  |
| pulseRadius | float | 6.0 |  |
| pulseStroke | float | 2.0 |  |
| widthSinMag | float | 0.0 |  |
| widthSinScl | float | 4.0 |  |
| recentDamageMultiplier | float | 0.1 |  |
| laser | TextureRegion | null |  |
| laserEnd | TextureRegion | null |  |
| laserTop | TextureRegion | null |  |
| laserTopEnd | TextureRegion | null |  |
| laserColor | Color | 98ffa9ff |  |
| laserTopColor | Color | ffffffff |  |
| healColor | Color | 98ffa9ff |  |
| healEffect | Effect | healBlockFull |  |
