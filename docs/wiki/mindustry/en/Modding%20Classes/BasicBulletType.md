# BasicBulletType

Built-in constants:

`placeholder` `spaceLiquid` `damageLightning` `damageLightningGround` `damageLightningAir` `fireball`

## BasicBulletType

*extends BulletType*

An extended BulletType for most ammo-based bullets shot from turrets and units. Draws 1-2 sprites that can spin or shrink.

| field | type | default | notes |
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
