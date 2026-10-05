# StaticWall

## StaticWall

*继承自 Prop*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| large | TextureRegion | null |  |
| split | TextureRegion[][] | null |  |
| autotile | boolean | false | 若为 true，该墙使用自动拼接；不支持变体。参见 https://github.com/GglLfr/tile-gen |
| autotileMidVariants | int | 1 | 大于 1 时，自动拼接的中部区域带随机变体。 |
