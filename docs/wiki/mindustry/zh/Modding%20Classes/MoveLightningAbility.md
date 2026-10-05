# MoveLightningAbility

## MoveLightningAbility

*继承自 Ability*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| damage | float | 35.0 | 闪电伤害 |
| chance | float | 0.15 | 每刻触发的概率。设为 >= 1 时每刻都以最高速度触发闪电 |
| length | int | 12 | 闪电长度。小于等于 0 表示禁用 |
| minSpeed | float | 0.8 | 开始触发闪电与停止加速的速度阈值 |
| maxSpeed | float | 1.2 | 开始触发闪电与停止加速的速度阈值 |
| color | Color | a9d8ffff | 闪电颜色 |
| y | float | 0.0 | 闪电生成位置沿 Y 轴的偏移 |
| x | float | 0.0 | 沿 X 轴的偏移 |
| alternate | boolean | true | 生成侧是否交替 |
| heatRegion | String | "error" | 类似 v5 标枪护盾的热量精灵抖动效果 |
| bullet | BulletType | null | 发射的子弹类型。可为 null |
| bulletAngle | float | 0.0 | 子弹角度参数 |
| bulletSpread | float | 0.0 | 子弹角度参数 |
| shootEffect | Effect | sparkShoot |  |
| parentizeEffects | boolean | false |  |
| shootSound | Sound | shootArc |  |
