# RepairBeamWeapon

## RepairBeamWeapon

*继承自 Weapon*

注意该武器需要一枚 maxRange 为正的弹药。
旋转必须设为 true。不支持固定维修点。

| 字段 | 类型 | 默认值 | 备注 |
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
