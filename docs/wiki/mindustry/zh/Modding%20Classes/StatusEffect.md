# StatusEffect

内置常量：

`none` `burning` `freezing` `unmoving` `slow` `fast` `wet` `muddy` `melting` `sapped` `tarred` `overdrive` `overclock` `shielded` `shocked` `blasted` `corroded` `boss` `sporeSlowed` `disarmed` `electrified` `invincible` `dynamic`

## StatusEffect

*继承自 UnlockableContent*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| damageMultiplier | float | 1.0 | 带有该效果的单位造成的伤害。 |
| healthMultiplier | float | 1.0 | 单位生命值倍率。 |
| speedMultiplier | float | 1.0 | 单位速度倍率。 |
| reloadMultiplier | float | 1.0 | 单位装填速度倍率。 |
| buildSpeedMultiplier | float | 1.0 | 单位建造速度倍率。 |
| dragMultiplier | float | 1.0 | 单位阻力倍率。 |
| transitionDamage | float | 0.0 | 转变为亲和时造成的伤害。 |
| disarm | boolean | false | 单位武器被禁用。 |
| damage | float | 0.0 | 每帧伤害。 |
| intervalDamageTime | float | 0.0 | 间隔伤害之间的间隔（刻）；小于等于 0 表示禁用。 |
| intervalDamage | float | 0.0 | 间隔伤害造成的伤害。 |
| intervalDamagePierce | boolean | false | 为 true 时，间隔伤害可穿透护甲。 |
| effectChance | float | 0.15 | 出现视觉效果的概率。 |
| parentizeEffect | boolean | false | 该效果是否应指定父对象。 |
| permanent | boolean | false | 为 true 时，该效果永不消失。 |
| reactive | boolean | false | 为 true 时，该效果仅与其他效果反应，无法被施加。 |
| dynamic | boolean | false | 用于带自定义属性的动态效果类型的特殊标记——请勿使用。 |
| show | boolean | true | 是否在数据库中显示该效果。 |
| color | Color | ffffffff | 效果的着色。 |
| effect | Effect | none | 在受影响单位上随机出现的效果。 |
| applyEffect | Effect | none | 施加到单位时仅显示一次的效果。 |
| applyExtend | boolean | false | 即使单位已带有该效果，是否仍显示施加效果。 |
| applyColor | Color | ffffffff | 施加效果的着色。 |
| parentizeApplyEffect | boolean | false | 施加效果是否应指定父对象。 |
| affinities | ObjectSet of StatusEffect | [] | 用于属性显示的亲和值与对立值。 |
| opposites | ObjectSet of StatusEffect | [] | 用于属性显示的亲和值与对立值。 |
| outline | boolean | true | 设为 false 以禁用轮廓生成。 |
