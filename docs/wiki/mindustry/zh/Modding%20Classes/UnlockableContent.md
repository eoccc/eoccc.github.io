# UnlockableContent

## UnlockableContent

*继承自 MappableContent*

可解锁内容类型的基础接口。

| 字段 | 类型 | 默认值 | 备注 |
|---|---|---|---|
| stats | Stats | new Stats() | 该内容的属性存储。按需初始化。 |
| localizedName | String |  | 本地化的正式名称。永不为 null；在语言包中找不到时使用内部名称。 |
| description | String | null | 本地化的描述与详情。可为 null。 |
| details | String | null | 本地化的描述与详情。可为 null。 |
| credit | String | null | 本地化的描述与详情。可为 null。 |
| alwaysUnlocked | boolean | false | 该内容是否在科技树中始终解锁。 |
| inline描述 | boolean | true | 是否在研究对话框预览中显示描述。 |
| hideDetails | boolean | true | 如果在战役模式中尚未解锁，是否在自定义游戏中隐藏详情。 |
| hideDatabase | boolean | false | 是否在核心数据库中隐藏此项。 |
| generateIcons | boolean | true | 为 false 时，该内容的所有图标生成均被禁用，不再调用 createIcons。 |
| selectionSize | float | 24.0 | 该内容在某些选择菜单中的显示大小 |
| uiIcon | TextureRegion | null | 在界面中使用的该内容图标。 |
| fullIcon | TextureRegion | null | 该内容的完整图标，不缩放。 |
| fullOverride | String | "" | 完整图标的覆盖项。对于图标重复的模组内容很有用。会覆盖任何其他完整图标。 |
| allDatabaseTabs | boolean | false | 为 true 时，该内容会出现在所有数据库标签页中。 |
| shownPlanets | ObjectSet of Planet | [] | 该内容所面向的星球。如果为空，则根据物品需求决定星球。目前仅对方块有意义。 |
| databaseTabs | ObjectSet of UnlockableContent | [] | 决定该内容会出现在哪些数据库标签页中的内容——通常是一个星球。如果未定义，则使用 shownPlanets 中的值。如果 shownPlanets 也为空，则使用 Serpulo 作为“默认”标签页。 |
| databaseCategory | String | null | 内容类别。定义核心数据库中内容分类的主要类别，例如 "block"、"liquid"、"unit"。值为 null 或空时回退为 getContentType().name()。 |
| databaseTag | String | null | 分类标签。核心数据库中内容分类的次级分类。例如 databaseCategory 为 "block" 下的 "turret"、"wall"，databaseCategory 为 "units" 下的 "core-unit"、"ground-unit"。当值为 null 或空时使用 "default" 作为回退。使用 "default" 时不显示额外的标签。 |
| techNode | TechNode | null | 该内容的科技树节点（如果适用）。不属于科技树则为 Null。 |
| techNodes | Seq of TechNode | [] | 该内容所属各科技树的节点。 |
