# DrawTurret

## DrawTurret

*extends DrawBlock*

Extend to implement custom drawing behavior for a turret.

| field | type | default | notes |
|---|---|---|---|
| parts | Seq of DrawPart | [] |  |
| ammoParts | ObjectMap of UnlockableContent, DrawPart[] | {} |  |
| basePrefix | String | "" | Prefix to use when loading base region. |
| liquidDraw | Liquid | null | Overrides the liquid to draw in the liquid region. |
| turretLayer | float | 50.0 |  |
| shadowLayer | float | 49.5 |  |
| heatLayer | float | 50.1 |  |
| base | TextureRegion | null |  |
| liquid | TextureRegion | null |  |
| top | TextureRegion | null |  |
| heat | TextureRegion | null |  |
| preview | TextureRegion | null |  |
| outline | TextureRegion | null |  |
