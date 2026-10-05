# ContinuousBulletType

Built-in constants:

`placeholder` `spaceLiquid` `damageLightning` `damageLightningGround` `damageLightningAir` `fireball`

## ContinuousBulletType

*extends BulletType*

Basic continuous (line) bullet type that does not draw itself. Essentially abstract.

| field | type | default | notes |
|---|---|---|---|
| length | float | 220.0 |  |
| shake | float | 0.0 |  |
| damageInterval | float | 5.0 |  |
| largeHit | boolean | false |  |
| continuous | boolean | true |  |
| timescaleDamage | boolean | false | If a building fired this, whether to multiply damage by its timescale. |
