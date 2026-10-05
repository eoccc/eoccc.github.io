# StaticWall

## StaticWall

*extends Prop*

| field | type | default | notes |
|---|---|---|---|
| large | TextureRegion | null |  |
| split | TextureRegion[][] | null |  |
| autotile | boolean | false | If true, this wall uses autotiling; variants are not supported. See https://github.com/GglLfr/tile-gen |
| autotileMidVariants | int | 1 | If >1, the middle region of the autotile has random variants. |
