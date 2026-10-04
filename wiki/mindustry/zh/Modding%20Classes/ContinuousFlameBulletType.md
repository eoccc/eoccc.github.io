# ContinuousFlameBulletType

内置常量：

`placeholder` `spaceLiquid` `damageLightning` `damageLightningGround` `damageLightningAir` `fireball`

## ContinuousFlameBulletType

*继承自 ContinuousBulletType*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| lightStroke | float | 40.0 |  |
| width | float | 3.7 |  |
| oscScl | float | 1.2 |  |
| oscMag | float | 0.02 |  |
| divisions | int | 25 |  |
| drawFlare | boolean | true |  |
| flareColor | Color | e189f5ff |  |
| flareWidth | float | 3.0 |  |
| flareInnerScl | float | 0.5 |  |
| flareLength | float | 40.0 |  |
| flareInnerLenScl | float | 0.5 |  |
| flareLayer | float | 99.9999 |  |
| flareRotSpeed | float | 1.2 |  |
| rotateFlare | boolean | false |  |
| lengthInterp | Interp | slope |  |
| lengthWidthPans | float[] | [1.12, 1.3, 0.32, 1.0, 1.0, 0.3, 0.8, 0.9, 0.2, 0.5, 0.8, 0.15, 0.25, 0.7, 0.1] | 长度、宽度、椭圆平移和偏移，全部作为基础宽度与长度的比例。存储为“交错”的值数组：LWPO1 LWPO2 LWPO3... |
| colors | Color[] | [eb7abe8c, e189f5b2, 907ef7cc, 91a4ffff, ffffffff] |  |
