# PointLaserBulletType

Built-in constants:

`placeholder` `spaceLiquid` `damageLightning` `damageLightningGround` `damageLightningAir` `fireball`

## PointLaserBulletType

*extends BulletType*

A continuous bullet type that only damages in a point.

| field | type | default | notes |
|---|---|---|---|
| sprite | String | "point-laser" |  |
| laser | TextureRegion | null |  |
| laserEnd | TextureRegion | null |  |
| color | Color | ffffffff |  |
| beamEffect | Effect | colorTrail |  |
| beamEffectInterval | float | 3.0 |  |
| beamEffectSize | float | 3.5 |  |
| oscScl | float | 2.0 |  |
| oscMag | float | 0.3 |  |
| damageInterval | float | 5.0 |  |
| shake | float | 0.0 |  |
