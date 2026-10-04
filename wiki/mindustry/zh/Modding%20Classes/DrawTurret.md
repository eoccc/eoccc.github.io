# DrawTurret

## DrawTurret

*继承自 DrawBlock*

扩展以实现炮塔的自定义绘制行为。

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| parts | Seq of DrawPart | [] |  |
| ammoParts | ObjectMap of UnlockableContent, DrawPart[] | {} |  |
| basePrefix | String | "" | 加载基础区域时使用的前缀。 |
| liquidDraw | Liquid | null | 覆盖液体区域所绘制的液体。 |
| turretLayer | float | 50.0 |  |
| shadowLayer | float | 49.5 |  |
| heatLayer | float | 50.1 |  |
| base | TextureRegion | null |  |
| liquid | TextureRegion | null |  |
| top | TextureRegion | null |  |
| heat | TextureRegion | null |  |
| preview | TextureRegion | null |  |
| outline | TextureRegion | null |  |
