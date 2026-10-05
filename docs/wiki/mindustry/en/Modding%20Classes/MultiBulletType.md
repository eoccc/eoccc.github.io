# MultiBulletType

Built-in constants:

`placeholder` `spaceLiquid` `damageLightning` `damageLightningGround` `damageLightningAir` `fireball`

## MultiBulletType

*extends BulletType*

A fake bullet type that spawns multiple sub-bullets when "fired".

| field | type | default | notes |
|---|---|---|---|
| bullets | BulletType[] | [] |  |
| repeat | int | 1 | Amount of times the bullet array is repeated. |
