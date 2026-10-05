# Weapon

## Weapon

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| name | String | Weapon Name | displayed weapon region |
| bullet | BulletType | placeholder | bullet shot |
| ejectEffect | Effect | none | shell ejection effect |
| display | boolean | true | 该武器是否应出现在持有该武器的单位属性中 |
| mirror | boolean | true | 是否在初始化时创建该武器的翻转副本。默认：true |
| flipSprite | boolean | false | 渲染时是否翻转武器的贴图。仅供内部使用——请勿设置！ |
| alternate | boolean | true | 是否让不同臂上的武器依次发射，而不是同时发射；仅当 mirror = true 时有效 |
| rotate | boolean | false | 是否独立于单位朝目标旋转 |
| showStatSprite | boolean | true | 是否在数据库中显示该武器的贴图。 |
| base旋转 | float | 0.0 | 该武器起始时的旋转。 |
| top | boolean | true | 是否在上方绘制外描边。 |
| continuous | boolean | false | 射击时是否将弹药固定在原位；它仍需要装填。 |
| alwaysContinuous | boolean | false | 该武器是否使用无需装填的连续射击；隐含 continuous = true |
| aimChangeSpeed | float | Infinity | 炮塔改变其弹药“瞄准”距离的速度。仅用于点激光弹药。 |
| controllable | boolean | true | 该武器是否可以由玩家手动瞄准 |
| aiControllable | boolean | true | 该武器是否可以由单位自动瞄准 |
| alwaysShooting | boolean | false | 该武器是否始终射击，无论目标或锥角如何 |
| autoTarget | boolean | false | 是否在 update() 中自动瞄准相关单位；仅当 controllable = false 时有效。 |
| predictTarget | boolean | true | 是否进行目标轨迹预测 |
| useAttackRange | boolean | true | 若为 true，该武器用于攻击射程计算 |
| targetInterval | float | 40.0 | 目标之间的等待刻数 |
| targetSwitchInterval | float | 70.0 | 目标之间的等待刻数 |
| rotateSpeed | float | 20.0 | 启用旋转时武器的旋转速度，单位为度/刻 |
| reload | float | 1.0 | weapon reload in frames |
| inaccuracy | float | 0.0 | 每次射击的角度误差 |
| shake | float | 0.0 | 每次射击屏幕震动的强度与持续时间 |
| recoil | float | 1.5 | visual weapon knockback. |
| recoils | int | -1 | 后坐力的额外计数次数。 |
| recoilTime | float | -1.0 | 武器回到起始位置所需的刻数。默认使用装填时间。 |
| recoilPow | float | 1.8 | 应用于视觉后坐的力度曲线 |
| cooldownTime | float | 20.0 | 热量区域冷却所需的刻数 |
| shootX | float | 0.0 | 弹丸/效果相对武器中心的偏移 |
| shootY | float | 3.0 | 弹丸/效果相对武器中心的偏移 |
| x | float | 5.0 | 武器在单位上的位置偏移 |
| y | float | 0.0 | 武器在单位上的位置偏移 |
| xRand | float | 0.0 | 沿 X/Y 轴的随机散布。 |
| yRand | float | 0.0 | 沿 X/Y 轴的随机散布。 |
| shoot | ShootPattern | new ShootPattern() | 子弹使用的发射模式 |
| shadow | float | -1.0 | 武器下方绘制阴影的半径；<0 表示禁用 |
| velocityRnd | float | 0.0 | 速度中随机部分的比例 |
| extraVelocity | float | 0.0 | 以比例形式附加的额外速度 |
| lifeRnd | float | 0.0 | 存活时间中随机取值的比例 |
| extraLife | float | 0.0 | 以比例形式附加的额外存活时间 |
| shootCone | float | 5.0 | 开始射击的锥形范围的半角半径。 |
| rotationLimit | float | 361.0 | 武器相对挂载点可旋转的锥形范围。 |
| minWarmup | float | 0.0 | 开火前武器的最小预热（这不是线性的，不要用 1！） |
| shootWarmupSpeed | float | 0.1 | 射击预热的插值速度，仅用于部件 |
| smoothReloadSpeed | float | 0.15 | 射击预热的插值速度，仅用于部件 |
| linearWarmup | boolean | false | 为 true 时，射击预热为线性而非曲线。 |
| soundPitchMin | float | 0.8 | 音效音高的随机范围 |
| soundPitchMax | float | 1.0 | 音效音高的随机范围 |
| ignore旋转 | boolean | false | 射击时是否忽略射击者的旋转。 |
| noAttack | boolean | false | 为 true 时，该武器不能用于攻击目标。 |
| minShootVelocity | float | -1.0 | 该武器射击所需的最小速度。-1 表示禁用该限制。 |
| maxShootVelocity | float | -1.0 | 该武器射击的最大速度。-1 表示禁用该限制。 |
| parentizeEffects | boolean | false | 射击效果是否应跟随单位（效果需将 followParent 设为 true 才能生效） |
| otherSide | int | -1 | 用于交替的内部值——请勿更改！ |
| layerOffset | float | 0.0 | 绘制 Z 偏移，相对于默认值 |
| activeSound | Sound | none | sound looped when shooting |
| activeSoundVolume | float | 1.0 | volume of active sound |
| shootSound | Sound | shoot | sound used for shooting |
| shootSoundVolume | float | 1.0 | 射击音效的音量 |
| initialShootSound | Sound | none | 该武器首次开火时使用的音效；仅用于连续型武器 |
| chargeSound | Sound | none | 用于有延迟的武器的音效 |
| region | TextureRegion | null | displayed region (autoloaded) |
| heatRegion | TextureRegion | null | 热量区域，必须与 region 尺寸相同（可选） |
| cellRegion | TextureRegion | null | 单元格区域，必须与 region 尺寸相同（可选） |
| outlineRegion | TextureRegion | null | 若 top 为 false 时要显示的外描边区域 |
| heatColor | Color | ab3400ff | heat region tint |
| shootStatus | StatusEffect | none | 射击时施加的状态效果 |
| mountType | Func of Weapon, WeaponMount | WeaponMount::new | 要使用的武器挂架类型 |
| shootStatusDuration | float | 300.0 | 被射击时的状态效果持续时间 |
| shootOnDeath | boolean | false | 该武器是否应在其拥有者死亡时开火 |
| shootOnDeathEffect | Effect | null | 若不为 null 且 shootOnDeath == true，则仅在其拥有者死亡时覆盖武器的射击效果。 |
| parts | Seq of DrawPart | [] | extra animated parts |
