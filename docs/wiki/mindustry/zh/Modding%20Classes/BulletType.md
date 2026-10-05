# BulletType

内置常量：

`placeholder` `spaceLiquid` `damageLightning` `damageLightningGround` `damageLightningAir` `fireball`

## BulletType

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| lifetime | float | 40.0 | 存活时间（刻）。 |
| lifeScaleRandMin | float | 1.0 | 该子弹生成时存活时间的最小/最大倍率。 |
| lifeScaleRandMax | float | 1.0 | 该子弹生成时存活时间的最小/最大倍率。 |
| speed | float | 1.0 | 速度（单位/刻）。 |
| velocityScaleRandMin | float | 1.0 | 该子弹生成时速度的最小/最大倍率。 |
| velocityScaleRandMax | float | 1.0 | 该子弹生成时速度的最小/最大倍率。 |
| damage | float | 1.0 | 命中时造成的直接伤害。 |
| hitSize | float | 4.0 | 碰撞箱尺寸。 |
| drawSize | float | 40.0 | 裁剪碰撞箱。 |
| angleOffset | float | 0.0 | 每次生成子弹时施加的角度偏移。 |
| randomAngleOffset | float | 0.0 | 每次生成子弹时施加的角度偏移。 |
| drag | float | 0.0 | 以速度比例表示的阻力。 |
| accel | float | 0.0 | 每帧加速度。 |
| pierce | boolean | false | Whether to pierce units. |
| pierceBuilding | boolean | false | Whether to pierce buildings. |
| pierceCap | int | -1 | 最多可穿透的物体数量。 |
| pierceDamageFactor | float | 0.0 | 每穿透一点生命值所减少伤害的倍率。 |
| maxDamageFraction | float | -1.0 | 大于 0 时，把非溅射伤害限制为目标最大生命值的一个比例。 |
| removeAfterPierce | boolean | true | 为 false 时，超过 pierceCap 后子弹不会被移除。仅供高级用法。 |
| laserAbsorb | boolean | true | 对穿甲激光而言，设为 true 时会被塑钢墙吸收。 |
| laserBullet | boolean | false | 该子弹是否被视为激光弹，从而被塑钢墙吸收。 |
| optimalLifeFract | float | 0.0 | 该子弹达到最佳射程/伤害等效果时的存活时间比例。用于激光与持续型炮塔。 |
| layer | float | 100.0 | Z layer to drawn on. |
| hitEffect | Effect | hitBulletSmall | 直接命中时显示的效果。 |
| despawnEffect | Effect | hitBulletSmall | 子弹消失时显示的效果。 |
| shootEffect | Effect | shootSmall | 射击时产生的效果。 |
| shootPattern | ShootPattern | null | 该子弹的发射模式。为 null 时使用炮塔的默认模式。 |
| chargeEffect | Effect | none | 开始蓄能时产生的效果；仅适用于带 firstShotDelay / shotDelay 的单发武器。 |
| smokeEffect | Effect | shootSmallSmoke | 射击时额外产生的烟雾效果。 |
| shootSound | Sound | none | 若设置，会覆盖炮塔中的射击音效。对单位无效，因为它们不能有多种弹药类型。 |
| hitSound | Sound | none | 命中目标或被移除时播放的音效。 |
| despawnSound | Sound | none | 命中目标或被移除时播放的音效。 |
| hitSoundPitch | float | 1.0 | 命中目标时音效的音高 |
| hitSoundPitchRange | float | 0.1 | 命中目标时音效的音高 |
| hitSoundVolume | float | 1.0 | 命中目标时音效的音量 |
| inaccuracy | float | 0.0 | 射击时的额外误差。 |
| ammoMultiplier | float | 2.0 | 每个弹药单位/液体生成的子弹数量。 |
| reloadMultiplier | float | 1.0 | 与炮塔装填速度相乘得到最终射击速度。 |
| buildingDamageMultiplier | float | 1.0 | 对地形造成基础伤害的倍率。 |
| shieldDamageMultiplier | float | 1.0 | 对力场护盾造成基础伤害的倍率。 |
| recoil | float | 0.0 | 来自射击实体的后坐力。 |
| killShooter | boolean | false | 被射击时是否杀死射击者。用于自杀式炸弹袭击者。 |
| instantDisappear | boolean | false | 是否让弹药立即消失。 |
| splashDamage | float | 0.0 | 溅射造成的伤害。0 表示禁用。 |
| scaledSplashDamage | boolean | false | 若为 true，溅射伤害会“正确地”受单位碰撞箱尺寸影响。用于不碰撞、或以溅射为主要伤害来源的弹药。 |
| knockback | float | 0.0 | 击退速度。 |
| impact | boolean | false | 击退方向是否跟随子弹方向 |
| status | StatusEffect | none | 命中时施加的状态效果。 |
| statusDuration | float | 480.0 | 所施加状态效果的持续时间强度。 |
| unitSort | Sortf | closest | 仅用于炮塔。用于选择攻击哪个单位的函数。会覆盖炮塔的排序 |
| statusChance | float | 1.0 | 该子弹施加状态效果的概率 |
| targetBlocks | boolean | true | 仅炮塔。为 false 时不会以方块为目标。 |
| targetMissiles | boolean | true | 仅炮塔。为 false 时不会以导弹为目标。 |
| collidesTiles | boolean | true | 该子弹类型是否与地形碰撞。 |
| collidesTeam | boolean | false | 该子弹类型是否与同队伍的地形碰撞。 |
| collidesAir | boolean | true | 该子弹类型是否与空中/地面单位碰撞。 |
| collidesGround | boolean | true | 该子弹类型是否与空中/地面单位碰撞。 |
| collides | boolean | true | 该子弹类型是否与任何物体碰撞。 |
| collideFloor | boolean | false | 为 true 时，该弹丸会与非地表地板碰撞。 |
| collideTerrain | boolean | false | 为 true 时，该弹丸会与静态墙体碰撞 |
| keepVelocity | boolean | true | 速度是否继承自射击者。 |
| scaleKeepVelocity | boolean | false | 若 keepVelocity = true，是否按增加的速度成比例减少存活时间，以保持射程一致。 |
| scaleLife | boolean | false | 是否按比例调整存活时间（并非实际速度！）以在目标位置消失。用于火炮。 |
| hittable | boolean | true | 该子弹是否可被近防系统拦截。 |
| reflectable | boolean | true | 该子弹是否可被反弹。 |
| absorbable | boolean | true | 该弹药是否会被护盾吸收。 |
| ignoreSpawnAngle | boolean | false | 为 true 时，create 中的 angle 参数被忽略。 |
| createChance | float | 1.0 | 该子弹被生成的概率。 |
| maxRange | float | -1.0 | 子弹射程的正向覆盖值。 |
| rangeOverride | float | -1.0 | 大于 0 时覆盖射程，即使小于基础射程。 |
| rangeChange | float | 0.0 | 在具有多种弹药类型的炮塔中使用时，可将其设为非零值以影响射程。 |
| extraRangeMargin | float | 0.0 | 在应用了 limitRange() 的炮塔中使用时，这会为弹药增加超出瞄准射程的额外射程。仅在原版中较有意义。 |
| range | float | 0.0 | 在 init() 中初始化的射程。 |
| minRangeChange | float | 0.0 | 在具有多种弹药类型的炮塔中使用时，可将其设为非零值以影响 minRange |
| healPercent | float | 0.0 | 方块生命值被治疗的比例 * |
| healAmount | float | 0.0 | 方块生命值的固定治疗量 |
| healSound | Sound | blockHeal | 方块被治疗时播放的音效 |
| healSoundVolume | float | 0.9 | volume of heal sound |
| lifesteal | float | 0.0 | 子弹伤害中用于治疗射手自身的比例。 |
| makeFire | boolean | false | 命中时是否点燃火焰 |
| hitUnder | boolean | false | 该子弹是否总是命中其下方的方块。 |
| despawnHit | boolean | false | 是否在消失时创建命中效果。若该弹药有任何特殊效果（如溅射伤害）则强制为 true。禁用 setDefaults 以避免覆盖 |
| fragOnHit | boolean | true | 为 true 时，该子弹命中任何物体时会生成子弹 |
| fragOnDespawn | boolean | true | 为 true 时，该子弹消失时会生成子弹 |
| fragOnAbsorb | boolean | true | 为 false 时，该子弹被护盾吸收后不会生成破片。 |
| pierceArmor | boolean | false | 为 true 时，伤害计算忽略单位护甲。 |
| armorMultiplier | float | 1.0 | 在伤害计算中乘以单位/建筑护甲。用于护甲弱点、护甲穿透和反护甲。 |
| blockArmorMultiplier | float | 1.0 | 仅放大伤害计算中使用的建筑护甲。 |
| sticky | boolean | false | 为 true 时，子弹会黏附到敌人身上并在碰撞时失效。 |
| stickyExtraLifetime | float | 0.0 | 子弹黏附到物体上时增加的存活时间。 |
| setDefaults | boolean | true | 是否自动设置 status 与 despawnHit。 |
| hitShake | float | 0.0 | 该子弹命中目标或消失时产生的震动强度。 |
| despawnShake | float | 0.0 | 该子弹命中目标或消失时产生的震动强度。 |
| fragBullet | BulletType | null | 该子弹消失时生成的子弹类型。 |
| delayFrags | boolean | false | 若为 true，碎片弹药会延迟到下一帧。修复了穿透弹药类型立即生成碎片、破坏 Damage 临时变量的隐蔽 bug。 |
| fragRandomSpread | float | 360.0 | 破片子弹的角度散布范围。 |
| fragSpread | float | 0.0 | 各破片子弹之间的均匀散布角（度）。 |
| fragAngle | float | 0.0 | 破片子弹的角度偏移。 |
| fragBullets | int | 9 | 生成的破片子弹数量。 |
| fragVelocityMin | float | 0.2 | 破片速度的随机范围倍率。 |
| fragVelocityMax | float | 1.0 | 破片速度的随机范围倍率。 |
| fragLifeMin | float | 1.0 | 破片存活时间的随机范围倍率。 |
| fragLifeMax | float | 1.0 | 破片存活时间的随机范围倍率。 |
| fragOffsetMin | float | 1.0 | 破片子弹相对母子弹的随机偏移。 |
| fragOffsetMax | float | 7.0 | 破片子弹相对母子弹的随机偏移。 |
| pierceFragCap | int | -1 | 当 pierce = true 时，该子弹可释放破片子弹的次数。 |
| intervalBullet | BulletType | null | 按固定间隔生成的子弹。 |
| bulletInterval | float | 20.0 | 子弹生成的间隔（刻）。 |
| intervalBullets | int | 1 | 每个间隔生成的子弹数量。 |
| intervalRandomSpread | float | 360.0 | 间隔子弹附加的随机角度。 |
| intervalSpread | float | 0.0 | 各间隔子弹之间的角度散布。 |
| intervalAngle | float | 0.0 | 间隔子弹的角度偏移。 |
| intervalDelay | float | -1.0 | 使用负值以禁用间隔子弹延迟。 |
| underwater | boolean | false | 为 true 时，该子弹在水下渲染。高度实验性！ |
| hitColor | Color | ffffffff | 命中/消失效果使用的颜色。 |
| healColor | Color | 98ffa9ff | 方块治疗效果使用的颜色。 |
| healEffect | Effect | healBlockFull | 对被治疗的方块发出的效果。 |
| spawnBullets | Seq of BulletType | [] | 该子弹生成时产生的子弹，极少需要，仅用于视觉效果。 |
| showStats | boolean | false | 是否显示所生成弹药的属性。 |
| spawnBulletRandomSpread | float | 0.0 | 生成子弹的随机角度散布。 |
| spawnUnit | UnitType | null | 生成*替代*该弹药的单位。用于导弹。 |
| despawnUnit | UnitType | null | 当该弹药击中某物、或因到达存活时间终点而消失时生成的单位。 |
| despawnUnitChance | float | 1.0 | 消失单位生成新单位的概率。 |
| despawnUnitCount | int | 1 | 该子弹消失时生成的单位数量。 |
| despawnUnitRadius | float | 0.1 | 相对原子弹消失/命中坐标的随机偏移距离。 |
| faceOutwards | boolean | false | 若为 true，该弹药消失时生成的单位会背对弹药，而不是与弹药同向。 |
| parts | Seq of DrawPart | [] | 该子弹的额外视觉部件。 |
| trailColor | Color | e58956ff | 子弹拖尾的颜色。 |
| trailChance | float | -1.0E-4 | 子弹每刻生成拖尾效果的概率。 |
| trailInterval | float | 0.0 | 拖尾效果的固定生成间隔。 |
| trailMinVelocity | float | 0.0 | 生成拖尾效果所需的最低速度。 |
| trailEffect | Effect | missileTrail | 生成的拖尾效果。 |
| trailSpread | float | 0.0 | 拖尾效果的随机偏移。 |
| trailParam | float | 2.0 | 传递给拖尾的旋转/尺寸参数。通常用于控制尺寸。 |
| trail旋转 | boolean | false | 传给拖尾的参数是否为子弹旋转角，而非固定值。 |
| trailInterp | Interp | one | 拖尾宽度随子弹存活时间的插值方式 |
| trailLength | int | -1 | 拖尾四边形的长度。任何值 0 |
| trailSinMag | float | 0.0 | 当 trailSinMag > 0 时，这些值会以正弦曲线作用于拖尾宽度。 |
| trailSinScl | float | 3.0 | 当 trailSinMag > 0 时，这些值会以正弦曲线作用于拖尾宽度。 |
| circleShooter | boolean | false | 为 true 时，子弹会尝试绕其发射者盘旋。 |
| circleShooterRadius | float | 13.0 | 子弹尝试盘旋的半径。 |
| circleShooterRadiusSmooth | float | 10.0 | 盘旋时的平滑额外半径值。 |
| circleShooterRotateSpeed | float | 0.3 | 盘旋时用于调整速度的倍率。 |
| splashDamageRadius | float | -1.0 | 使用负值以禁用溅射伤害。 |
| splashDamagePierce | boolean | false | 为 true 时，溅射伤害可穿透地形。 |
| incendAmount | int | 0 | 子弹周围尝试生成火焰的数量。 |
| incendSpread | float | 8.0 | 子弹周围火焰的散布范围。 |
| incendChance | float | 1.0 | 生成火焰的概率。 |
| homingPower | float | 0.0 | 子弹能力的强度。通常取 0 到 1 之间的数值，可从 0.1 开始尝试。 |
| homingRange | float | 50.0 | 子弹周围追踪效果的作用范围。 |
| homingDelay | float | -1.0 | 使用负值以禁用追踪延迟。 |
| followAimSpeed | float | 0.0 | 弹药旋转跟随光标的速度。数值越小震动越小。 |
| weaveMag | float | 0.0 | 子弹编织轨道的强度。注意这可能导致子弹失准。 |
| weaveRandom | boolean | true | 为 true 时，子弹编织轨迹在生成时随机改变方向。 |
| rotateSpeed | float | 0.0 | 子弹飞行时速度方向的旋转速率。 |
| puddles | int | 0 | 生成的独立液洼数量。 |
| puddleRange | float | 0.0 | 子弹位置周围形成液洼的范围。 |
| puddleAmount | float | 5.0 | 生成的每个液洼所含液体量。 |
| puddleLiquid | Liquid | water | 所生成液洼的液体种类。 |
| displayAmmoMultiplier | boolean | true | 是否在该弹药类型的属性中显示弹药倍率。 |
| statLiquidConsumed | float | 0.0 | 大于 0 时，显示时除以弹药倍率。 |
| lightRadius | float | -1.0 | 该子弹发出光的半径；小于 0 时使用默认值。 |
| lightOpacity | float | 0.3 | 光照颜色的不透明度。 |
| lightColor | Color | fbd367ff | 该子弹发出光的颜色。 |
