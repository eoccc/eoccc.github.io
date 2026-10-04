# Block

## Block

*继承自 UnlockableContent*

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| hasItems | boolean | false | 为 true 时，建筑带有物品模块。 |
| hasLiquids | boolean | false | 为 true 时，建筑带有液体模块。 |
| hasPower | boolean | false | 为 true 时，建筑带有电力模块。 |
| outputsLiquid | boolean | false | 用于判定该方块是否向某处输出液体；用于连接判断。 |
| consumesPower | boolean | true | 供某些电力方块（节点）用于标记为不耗电。默认为 true，即使该方块没有电力。 |
| outputsPower | boolean | false | 为 true 时，该方块是可行发电的发电机。 |
| connectedPower | boolean | true | 为 false 时电力节点无法连接到该方块。 |
| conductivePower | boolean | false | 为 true 时，该方块可像电缆一样传导电力。 |
| outputsPayload | boolean | false | 为 true 时，该方块可输出载荷，并影响混合计算。 |
| acceptsUnitPayloads | boolean | false | 为 true 时，该方块可接收载荷，并影响单位载荷进入与寻路行为。 |
| acceptsPayload | boolean | false | 为 true 时，载荷会尝试移入该方块。 |
| acceptsItems | boolean | false | 用于某些运输方块混合的视觉标记。 |
| alwaysAllowDeposit | boolean | false | 为 true 时，该方块不受 onlyDepositCore 规则影响。 |
| allowedInPayloads | boolean | true | 为 false 时该方块不能作为载荷放置。 |
| depositCooldown | float | -1.0 | 任何物品存入该方块时，施加给玩家存物的冷却（秒）。非负时覆盖 itemDepositCooldown。 |
| separateItemCapacity | boolean | false | 为 true 时，该方块的各物品容量相互独立，而非合并为一个总量。 |
| itemCapacity | int | 10 | 该方块可携带的最大物品数（通常按物品种类计算） |
| liquidCapacity | float | -1.0 | 若 hasLiquids = true，该方块可携带的最大液体总量。默认值为 10，随 ConsumeLiquid 中的最大液体消耗量缩放 |
| liquidPressure | float | 1.0 | 数值越高，液体输出速度越快；TODO 移除并替换为更好的液体系统 |
| outputFacing | boolean | true | 为 true 时，该方块在适用情况下朝其朝向输出，用于混合计算。 |
| noSideBlend | boolean | false | 若为 true，该方块不接受来自侧面的输入（用于装甲传送带） |
| displayFlow | boolean | true | 是否显示流量 |
| inEditor | boolean | true | 该方块在编辑器中是否可见 |
| editorConfigurable | boolean | false | 若为 true，在编辑器中配置该方块时会调用 {@link #buildEditorConfig(Table)}。 |
| lastConfig | Object | null | 应用于该方块的最后一个配置值。 |
| saveConfig | boolean | false | 是否保存最后的配置并应用到新放置的方块 |
| copyConfig | boolean | true | 是否允许通过中键复制配置 |
| clearOnDoubleTap | boolean | false | 若为 true，双击该可配置方块会清除配置。 |
| update | boolean | false | 该方块是否有会更新的 tile entity |
| destructible | boolean | false | 该方块是否有生命值且可被摧毁。注意：若 update = true，则将其设为 false 不起作用！ |
| unloadable | boolean | true | 卸载器是否对该方块生效 |
| isDuct | boolean | false | 若为 true，该方块相当于管道，会从侧面连接装甲管道。 |
| allowResupply | boolean | false | 单位是否可以通过从该方块取用物品来补给 |
| solid | boolean | false | whether this is solid |
| solidifes | boolean | false | 该方块*是否能够*成为实心。 |
| teamPassable | boolean | false | 若为 true，对该队伍而言它算作非实心方块。 |
| underBullets | boolean | false | 若为 true，除非被显式指定为目标，否则该方块不会被弹药击中。 |
| rotate | boolean | false | whether this is rotatable |
| rotateDraw | boolean | true | 若 rotate 为 true 且此项为 false，绘制时区域不会旋转 |
| rotateDrawEditor | boolean | true | 若 rotate 为 true 且此项为 false，则在编辑器中绘制时区域不会旋转 |
| visual旋转Offset | float | 0.0 | 用于破损平面渲染的视觉旋转偏移 |
| lock旋转 | boolean | true | 若 rotate = false 且此项为 true，放置时旋转将锁定为 0（默认）；仅供高级用法 |
| ignoreLine旋转 | boolean | false | 若为 true，该方块不会朝向线拖拽方向 |
| invertFlip | boolean | false | 若为 true，含该方块的蓝图翻转会被反转。 |
| variants | int | 0 | 要使用的不同变体区域数量 |
| drawArrow | boolean | true | 是否绘制旋转箭头——这不适用于方块线 |
| drawTeamOverlay | boolean | true | 是否默认绘制队伍角标 |
| saveData | boolean | false | 仅适用于静态方块：若为 true，则 tile data() 会保存在世界数据中。 |
| breakable | boolean | false | 你是否可以用右键破坏它 |
| unitMoveBreakable | boolean | false | 若为 true，该方块会被某些单位踩踏/移动时破坏 |
| rebuildable | boolean | true | 是否将该方块加入 brokenblocks |
| privileged | boolean | false | 若为 true，该逻辑相关方块只能与特权处理器一起使用（或它本身就是特权处理器） |
| requiresWater | boolean | false | 该方块是否只能放置在水上 |
| placeableLiquid | boolean | false | 该方块是否可以放置在任意液体上的任意位置 |
| placeablePlayer | boolean | true | 该方块是否可以由玩家通过 PlacementFragment 直接放置 |
| placeableOn | boolean | true | 该地板是否可被放置。 |
| insulated | boolean | false | 该方块是否具有绝缘属性。 |
| squareSprite | boolean | true | 该贴图是否为完整正方形。 |
| absorbLasers | boolean | false | 该方块是否吸收激光攻击。 |
| enableDrawStatus | boolean | true | 若为 false，该状态永不绘制 |
| drawDisabled | boolean | true | 是否绘制禁用状态 |
| autoResetEnabled | boolean | true | 是否在逻辑方块一段时间未交互后自动重置启用状态。 |
| noUpdateDisabled | boolean | false | 若为 true，该方块在禁用时停止更新 |
| updateInUnits | boolean | true | 若为 true，当该方块是单位中的载荷时也会更新。 |
| alwaysUpdateInUnits | boolean | false | 若为 true，无论实验性游戏规则如何，该方块都会在单位中的载荷内更新 |
| canPickup | boolean | true | @deprecated use allowedInPayloads instead |
| deconstructDropAllLiquid | boolean | false | 若为 false，拆除时只掉落可燃尽液体；否则掉落所有液体。 |
| useColor | boolean | true | 是否在小地图中使用该方块的颜色。仅用于覆盖层。 |
| itemDrop | Item | null | 该方块掉落的物品，用于钻头 |
| playerUnmineable | boolean | false | 若为 true，该方块不能被玩家开采。对沙子之类烦人的东西很有用。 |
| attributes | Attributes | new Attributes() | 对各地板的亲和性。 |
| scaledHealth | float | -1.0 | Health per square tile that this block occupies; essentially, this is multiplied by size * size. Overridden if health is > 0. If () | Cost multipliers per-item. |
| researchCost | ItemStack[] | null | 研究成本的覆盖值。未设置时使用上方的倍率与建造需求。 |
| forceTeam | Team | null | 设置后，所有方块将被强制归为该队伍。 |
| instantTransfer | boolean | false | 该方块是否具备瞬时传输。 |
| maxConsecutive | int | 2 | instantTransfer 连续方块的最大数量。 |
| quickRotate | boolean | true | 放置后是否可以旋转该方块。 |
| allowDerelictRepair | boolean | true | 为 true 时，点击即可修复该废弃方块。 |
| subclass | Class of ? | class mindustry.world.Block | 主类。非匿名类。 |
| selectScroll | float | 0.0 | 某些方块的滚动位置。 |
| buildType | Prov of Building | null | 为该方块创建的建筑。在 init() 中通过反射初始化；模组内容需手动设置。 |
| configurations | ObjectMap of Class of ?, Cons2 | {} | 按类型划分的配置处理器。 |
| itemFilter | boolean[] | [] | 消耗过滤器。 |
| liquidFilter | boolean[] | [] | 消耗过滤器。 |
| consumers | Consume[] | [] | 该方块使用的消耗器数组，仅在 init() 之后填充。 |
| optionalConsumers | Consume[] | [] | 该方块使用的消耗器数组，仅在 init() 之后填充。 |
| nonOptionalConsumers | Consume[] | [] | 该方块使用的消耗器数组，仅在 init() 之后填充。 |
| updateConsumers | Consume[] | [] | 该方块使用的消耗器数组，仅在 init() 之后填充。 |
| hasConsumers | boolean | false | 若该方块的数组中含有消耗器则设为 true。 |
| consPower | ConsumePower | null | 单一的电力消耗器（若适用）。 |
| regionRotated1 | int | -1 | 来自 icons() 的、会被旋转的区域索引。如果其中任一不为 -1，其他区域在 ConstructBlocks 中不会被旋转。 |
| regionRotated2 | int | -1 | 来自 icons() 的、会被旋转的区域索引。如果其中任一不为 -1，其他区域在 ConstructBlocks 中不会被旋转。 |
| region | TextureRegion | null |  |
| customShadowRegion | TextureRegion | null |  |
| teamRegion | TextureRegion | null |  |
| teamRegions | TextureRegion[] | null |  |
| variantRegions | TextureRegion[] | null |  |
| variantShadowRegions | TextureRegion[] | null |  |
| dumpTime | int | 5 | 尝试卸出物品的间隔（刻），例如 5 表示每秒 12 次 |
