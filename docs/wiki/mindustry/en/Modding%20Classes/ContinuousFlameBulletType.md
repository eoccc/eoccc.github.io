# ContinuousFlameBulletType

Built-in constants:

`placeholder` `spaceLiquid` `damageLightning` `damageLightningGround` `damageLightningAir` `fireball`

## ContinuousFlameBulletType

*extends ContinuousBulletType*

| field | type | default | notes |
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
| lengthWidthPans | float[] | [1.12, 1.3, 0.32, 1.0, 1.0, 0.3, 0.8, 0.9, 0.2, 0.5, 0.8, 0.15, 0.25, 0.7, 0.1] | Lengths, widths, ellipse panning, and offsets, all as fractions of the base width and length. Stored as an 'interleaved' array of values: LWPO1 LWPO2 LWPO3... |
| colors | Color[] | [eb7abe8c, e189f5b2, 907ef7cc, 91a4ffff, ffffffff] |  |
