# ContinuousBulletType

内置常量：

`placeholder` `spaceLiquid` `damageLightning` `damageLightningGround` `damageLightningAir` `fireball`

## ContinuousBulletType

*继承自 BulletType*

基础的连续（线）弹药类型，不绘制自身。本质上是抽象类。

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| length | float | 220.0 |  |
| shake | float | 0.0 |  |
| damageInterval | float | 5.0 |  |
| largeHit | boolean | false |  |
| continuous | boolean | true |  |
| timescaleDamage | boolean | false | 若由建筑发射，是否按其时间倍率放大伤害。 |
