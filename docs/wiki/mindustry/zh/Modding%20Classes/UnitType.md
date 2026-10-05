# UnitType

## UnitType

*继承自 UnlockableContent*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| envRequired | int | 0 | 该单位正常运作所需的全部环境标记。0 表示任意环境 |
| envEnabled | int | 1 | 该单位可以运作的环境标记。如果环境匹配其中任意一项，它就会被启用。 |
| envDisabled | int | 16 | 该单位*无法*运作的环境标记。如果环境匹配其中任意一项，它就会爆炸或被禁用。 |
| speed | float | 1.1 | movement speed (world units/t) |
| boostMultiplier | float | 1.0 | 加速时速度的倍率 |
| floorMultiplier | float | 1.0 | 该单位受地形影响的程度 |
| rotateSpeed | float | 5.0 | 身体旋转速度，单位为度/刻 |
| baseRotateSpeed | float | 5.0 | 机甲基础旋转速度，单位为度/刻 |
| drag | float | 0.3 | movement drag as fraction |
| accel | float | 0.5 | 加速度（作为速度的比例） |
| hitSize | float | 6.0 | 碰撞箱正方形一边的尺寸 |
| deathShake | float | -1.0 | shake on unit death |
| stepShake | float | -1.0 | 腿/机甲单位每步的震动 |
| rippleScale | float | 1.0 | 有腿单位的涟漪/尘埃尺寸 |
| riseSpeed | float | 0.08 | 加速上升速度（作为比例） |
| descentSpeed | float | 0.08 | 加速下降速度（作为比例） |
| fallSpeed | float | 0.018 | 该单位死亡时下落的速度 |
| missileAccelTime | float | 0.0 | 该导弹加速到全速需要多少刻 |
| health | float | 200.0 | raw health amount |
| armor | float | 0.0 | 受到的伤害按此数值减少 |
| range | float | -1.0 | 任意武器的最小射程；用于接近目标。可通过设置大于 0 的值来覆盖。 |
| maxRange | float | -1.0 | 任意武器的最大射程 |
| mineRange | float | 70.0 | 该单位可以开采矿石的射程 |
| buildRange | float | 220.0 | 该单位可以建造的射程 |
| circleTargetRadius | float | 80.0 | 若为 true，circleTarget 的半径 |
| crashDamageMultiplier | float | 1.0 | 该（飞行）单位撞击敌方物体时造成伤害的倍率 |
| wreckHealthMultiplier | float | 0.25 | 该飞行单位残骸的生命值倍率，基于其最大生命值。 |
| dpsEstimate | float | -1.0 | 对单位 DPS 的非常粗略的估计；在 init() 中初始化 |
| clipSize | float | -1.0 | 图形裁剪尺寸；0，这是腿在水平方向上离身体多远的缩放 |
| legMaxLength | float | 1.75 | 单条腿的最大长度（作为真实长度的比例） |
| legMinLength | float | 0.0 | 单条腿的最小长度（作为真实长度的比例） |
| legSplashDamage | float | 0.0 | 腿触地时造成的溅射伤害 |
| legSplashRange | float | 5.0 | 腿的溅射伤害半径 |
| baseLegStraightness | float | 0.0 | 腿的基部/原点有多直（0 = 圆形，1 = 直线） |
| legStraightness | float | 0.0 | 腿向外角度的直线程度（0 = 圆形，1 = 水平线） |
| legBaseUnder | boolean | false | 为 true 时，更靠外的腿部区域绘制在下层而非上层。 |
| lockLegBase | boolean | false | 若为 true，腿被锁定在单位基部，而不是位于隐式旋转的“挂架”上。 |
| legContinuousMove | boolean | false | 若为 true，即使单位未移动，腿也总是尝试移动（行为更自然） |
| flipBackLegs | boolean | true | TODO 这两项似乎都没有太大作用 |
| flipLegSide | boolean | false | TODO 这两项似乎都没有太大作用 |
| emitWalkSound | boolean | true | 是否在水中发出溅水声。 |
| emitWalkEffect | boolean | true | 是否在水中发出溅水效果（fasle 意味着 emitWalkSound 为 false）。 |
| mechLandShake | float | 0.0 | 该机甲加速后着陆时的屏幕震动幅度 |
| mechSideSway | float | 0.54 | 机甲摆动动画的参数 |
| mechFrontSway | float | 0.1 | 机甲摆动动画的参数 |
| mechStride | float | -1.0 | 机甲摆动动画的参数 |
| mechStepParticles | boolean | false | 该机甲迈步时是否产生粒子 |
| mechLegColor | Color | 6e7080ff | 腿在移动时变换成的颜色，用于模拟纵深感 |
| treadRects | Rect[] | [] | 履带列表，以图像坐标中的矩形表示，相对于中心。这些会被镜像。 |
| treadFrames | int | 18 | 履带中移动的帧数 |
| treadPullOffset | int | 0 | 履带贴图顶部有多少被“切掉”（相对于图案而言）；此值会被校正 |
| crushFragile | boolean | false | 若为 true，“脆弱”方块会在坦克周围 1x1 区域内被立即碾碎 |
| segments | int | 0 | number of independent segments |
| segmentUnits | int | 1 | TODO 波浪支持——对于多单位分段单位，这是所生成的独立单位数量 |
| segmentUnit | UnitType | null | 以分段方式生成单位；若为 null，则使用同一单位 |
| segmentEndUnit | UnitType | null | 末端生成的单位；若为 null，则使用该分段的单位 |
| segmentLayerOrder | boolean | true | true——父段在更高层；false——父段比头部在更低层 |
| segmentMag | float | 2.0 | 各段之间正弦偏移的幅度 |
| segmentScl | float | 4.0 | 各段之间正弦偏移的缩放 |
| segmentPhase | float | 5.0 | 各段之间正弦偏移的索引倍率 |
| segmentRotSpeed | float | 1.0 | 每个段向下一个段移动的速度 |
| segmentMaxRot | float | 30.0 | 各段角度之间的最大差值 |
| segmentSpacing | float | -1.0 | 单位各段之间的间距（仅用于多单位蠕虫） |
| segment旋转Range | float | 80.0 | 各段之间的旋转被限制在此范围内 |
| crawlSlowdown | float | 0.5 | 达到 crawlSlowdownFrac 时该单位将具有的速度倍率。 |
| crushDamage | float | 0.0 | 该坦克/爬行者每帧对其下方方块造成的伤害。 |
| crawlSlowdownFrac | float | 0.55 | 该方块下方达到 crawlSlowdown 所需的固体比例。 |
| lifetime | float | 300.0 | lifetime of this missile. |
| homingDelay | float | 10.0 | 该导弹开始追踪前必须经过的刻数。 |
| baseRegion | TextureRegion | null |  |
| legRegion | TextureRegion | null |  |
| region | TextureRegion | null |  |
| previewRegion | TextureRegion | null |  |
| shadowRegion | TextureRegion | null |  |
| cellRegion | TextureRegion | null |  |
| itemCircleRegion | TextureRegion | null |  |
| softShadowRegion | TextureRegion | null |  |
| jointRegion | TextureRegion | null |  |
| footRegion | TextureRegion | null |  |
| legBaseRegion | TextureRegion | null |  |
| baseJointRegion | TextureRegion | null |  |
| outlineRegion | TextureRegion | null |  |
| treadRegion | TextureRegion | null |  |
| mineLaserRegion | TextureRegion | null |  |
| mineLaserEndRegion | TextureRegion | null |  |
| wreckRegions | TextureRegion[] | null |  |
| segmentRegions | TextureRegion[] | null |  |
| segmentCellRegions | TextureRegion[] | null |  |
| segmentOutlineRegions | TextureRegion[] | null |  |
| treadRegions | TextureRegion[][] | null |  |
