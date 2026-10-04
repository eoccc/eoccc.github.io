# 8.0 迁移指南

## JSON 模组

如果你有 JSON 模组，你*大概*什么都不用做。所有现有的 JSON 模组应该仍能正常工作，只是在某些星球上内容的显示方式会有一些变化。请参阅下文「星球」一节。

## Java/JS 模组

## 杂项

- `Binding` 的按键绑定值现在采用 camelCase。

- 旧的按键绑定系统已被彻底重做，以支持自定义模组按键绑定——参见 `arc.input.KeyBind#add`。`Core.keybinds` 已被移除，请改用 `Keybind` 类。

- 不再允许在 `createIcons` 之外调用 `Core.atlas.getPixmap`。如果你的内容需要生成图标，请通过覆写 `createIcons` 来实现。否则你无法访问打包数据的图像数据；那曾是一个巨大的内存泄漏。

## 方块

- `Building` 的大多数不必要的「getter」方法（例如 `void tile(Tile), Tile tile(), block()`）已被移除。本来就没有理由使用它们，但如果你的模组恰好用了，你需要改为直接访问字段。

- 方块现在有一个单独的 `lightClipSize` 字段，用于 `drawLight()` 的尺寸裁剪。现在必须让 `emitLight` 为 true，才会调用此方法。

- `loopSound` 已被移除；循环音效必须在每个方块的 `Building` 中手动创建和更新。示例请参见 `Turret` 源代码。

## 单位

- `Player#unit()` **现在可能为 null。** 访问单位前请务必检查 `!player.dead()`。

- `Units.null` 已被移除。

- 命令现在属于内容。`UnitCommand.all` 已被移除。

- 单位命令现在是 `Seq`，而不是数组。

## 星球

- 所有与物品可见性相关的字段（`itemWhitelist`、`hiddenItems`、`Rules.hiddenBuildItems`）都已被移除。要让内容显示在某个特定星球上，请修改其 `shownPlanets` 字段以包含该星球。如果你为某个星球设置了科技树，这会被自动完成。
