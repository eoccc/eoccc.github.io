# BasicBulletType

内置常量：

`placeholder` `spaceLiquid` `damageLightning` `damageLightningGround` `damageLightningAir` `fireball`

## BasicBulletType

*继承自 BulletType*

用于从炮塔和单位发射的大多数弹药型弹药的一种扩展 BulletType。绘制 1-2 个可旋转或缩小的贴图。

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| backColor | Color | f9c27aff |  |
| frontColor | Color | fff8e8ff |  |
| mixColorFrom | Color | ffffff00 |  |
| mixColorTo | Color | ffffff00 |  |
| width | float | 5.0 |  |
| height | float | 7.0 |  |
| shrinkX | float | 0.0 |  |
| shrinkY | float | 0.5 |  |
| shrinkInterp | Interp | linear |  |
| spin | float | 0.0 |  |
| rotationOffset | float | 0.0 |  |
| sprite | String | bullet |  |
| backSprite | String | null |  |
| backRegion | TextureRegion | null |  |
| frontRegion | TextureRegion | null |  |
