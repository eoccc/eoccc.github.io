# Turret

## Turret

*继承自 ReloadTurret*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| timerTarget | int | 1 |  |
| targetInterval | float | 20.0 | 尝试寻找目标的间隔（刻）。 |
| newTargetInterval | float | -1.0 | 当该炮塔已有有效目标时的目标间隔。-1 = targetInterval |
| maxAmmo | int | 30 | 可储存的最大弹药量。 |
| ammoPerShot | int | 1 | 每次射击消耗的弹药量。 |
| consumeAmmoOnce | boolean | true | 为 true 时，无论发射多少子弹，每次射击只消耗一次弹药。 |
| heatRequirement | float | -1.0 | 开火所需的最低输入热量。 |
| maxHeatEfficiency | float | 3.0 | 该炮塔使用热量时的最高效率。 |
| inaccuracy | float | 0.0 | 子弹角度的随机范围（度）。 |
| velocityRnd | float | 0.0 | 子弹速度的随机比例。 |
| extraVelocity | float | 0.0 | 以比例形式附加的额外速度 |
| lifeRnd | float | 0.0 | 存活时间中随机取值的比例 |
| extraLife | float | 0.0 | 以比例形式附加的额外存活时间 |
| scaleLifetimeOffset | float | 0.0 | 带 lifeScale 的子弹所增加的存活时间比例。 |
| shootCone | float | 8.0 | 炮塔仍会尝试射击的最大角度差（度）。 |
| shootX | float | 0.0 | 炮塔的射击点。 |
| shootY | float | -Infinity | 炮塔的射击点。 |
| xRand | float | 0.0 | 沿 X 轴的随机散布。 |
| drawMinRange | boolean | false | 为 true 时，还会为 minRange 绘制范围环。 |
| trackingRange | float | 0.0 | 可发现并锁定目标但尚不开火的射程。 |
| minRange | float | 0.0 | 子弹最小射程。仅用于火炮。 |
| minWarmup | float | 0.0 | 开火所需的最低预热。 |
| accurateDelay | boolean | true | 为 true 时，该炮塔会依据 shoot.firstShotDelay 精确瞄准移动目标。 |
| moveWhileCharging | boolean | true | 为 false 时该炮塔蓄能期间无法移动。 |
| reloadWhileCharging | boolean | true | 为 false 时该炮塔蓄能期间无法装填 |
| warmupMaintainTime | float | 0.0 | 即使炮塔未射击，预热状态保持的时间。 |
| shoot | ShootPattern | new ShootPattern() | 子弹使用的发射模式 |
| targetAir | boolean | true | 为 true 时，该方块以空中单位为目标。 |
| targetGround | boolean | true | 为 true 时，该方块以地面单位与建筑为目标。 |
| targetBlocks | boolean | true | 为 true 时，该方块以方块为目标。 |
| targetHealing | boolean | false | 为 true 时，该方块以友方方块为目标并予以治疗。 |
| playerControllable | boolean | true | 为 true 时，该炮塔可由玩家操控。 |
| displayAmmoMultiplier | boolean | true | 为 true 时，该方块会在属性中显示弹药倍率（对某些炮塔类型无意义）。 |
| targetUnderBlocks | boolean | true | 为 false 时，传送带等下压方块不会成为目标。 |
| alwaysShooting | boolean | false | 为 true 时，只要还有弹药，炮塔就会射击，不论范围内是否有目标或控制状态。 |
| predictTarget | boolean | true | 该炮塔是否会预测单位移动。 |
| unitSort | Sortf | closest | 用于选择攻击目标的函数。 |
| unitFilter | Boolf of Unit | {code} | 限定可攻击的单位类型。 |
| buildingFilter | Boolf of Building | underBullets | 限定可攻击的建筑类型。 |
| heatColor | Color | ab3400ff | 绘制在顶层的热量区域颜色（若存在） |
| shootEffect | Effect | null | 所有射击效果的统一可选覆盖值。 |
| smokeEffect | Effect | null | 所有烟雾效果的统一可选覆盖值。 |
| ammoUseEffect | Effect | none | 使用弹药时产生的效果。不可选。 |
| shootSound | Sound | shootDuo | 发射单颗子弹时播放的音效。 |
| shootSoundVolume | float | 1.0 | 射击音效的音量。 |
| chargeSound | Sound | none | 当 shoot.firstShotDelay > 0 且开始射击时播放的音效。 |
| loopSound | Sound | none | 该方块激活时播放的音效，单次循环。请勿滥用。 |
| loopSoundVolume | float | 0.5 | 激活音效的基础音量。 |
| soundPitchMin | float | 0.9 | 射击音效音高的作用范围。 |
| soundPitchMax | float | 1.1 | 射击音效音高的作用范围。 |
| ammoEjectBack | float | 1.0 | 弹药弹出效果的后向 Y 偏移。 |
| shootWarmupSpeed | float | 0.1 | 炮塔预热的插值速度。 |
| linearWarmup | boolean | false | 为 true 时，炮塔预热为线性而非曲线。 |
| recoil | float | 1.0 | 炮塔每次射击的后坐视觉幅度。 |
| recoils | int | -1 | 后坐力的额外计数次数。 |
| recoilTime | float | -1.0 | 炮塔回到起始位置所需的刻数。默认使用装填时间。 |
| recoilPow | float | 1.8 | 应用于视觉后坐的力度曲线 |
| cooldownTime | float | 20.0 | 热量区域冷却所需的刻数 |
| elevation | float | -1.0 | 炮塔阴影的视觉抬升量，-1 表示使用默认值。 |
| shake | float | 0.0 | 每次射击的屏幕震动幅度。 |
| drawer | DrawBlock | new DrawTurret() | 定义该炮塔的绘制行为。 |
