# 6.0 迁移指南

如果你是 5.0 的插件或模组开发者，你可能已经注意到你的内容在 6.0 中不再正常工作。
这是由于大量内部改动与新增内容造成的，本文将对此进行记录。

## 通用变更

### 最低游戏版本

现在所有模组都必须指定值为「105」或以上的 `minGameVersion` 才能被加载。这是为了确保过时的模组不会被加载。
只需在你的 `mod.hjson` 文件中添加 `minGameVersion: "160.5"` 即可。

## 名称变更

### 变量与类名变更

`ItemTurret`:

- `ammo` -> `ammoTypes`

- `reload` -> `reloadTime`

`ArtilleryTurret`, `BurstTurret`, `ChargeTurret`:

- 已移除。请改用 `ItemTurret` 或 `PowerTurret`；所有功能都已合并到基类中。

`BasicBulletType`:

- `bulletWidth` -> `width`

- `bulletHeight` -> `height`

- `bulletSprite` -> `sprite`

### TileEntity -> Building

`TileEntity` 现在改为 `Building`。
因此，原先 `TileEntity` 的函数，以及与它相关的任何函数（名称中含有或提及「entity」的）都已重命名，现在它们会把 `TileEntity` 称为「building」或「build」。`Tile.entity` 已重命名为 `Tile.build`，所有 `TileEntity` 实例（例如 `RouterEntity`、`ConveyorEntity`）都被重命名为以「Build」后缀结尾（例如 `RouterBuild`、`ConveyorBuild`），仅举几例。

许多函数（如 `draw()` 或 `placed()`）已从在 `Block` 中声明改为在 `Building` 中声明。这意味着这些函数不再传入 `Tile`，同时也让方块特有的行为不那么复杂。值得注意的是，`update(Tile tile)` 已移至 `Building`，并重命名（严格来说并非如此，但移植时可以忽略这个细节）为 `updateTile()`。

### Array -> Seq

`arc.struct.Array` 已重命名为 `arc.struct.Seq`，它是 `Sequence` 的缩写形式。

为什么？

- 它更准确。该数据结构不是数组，而是类似 `ArrayList` 的列表。

- 它不会与名为 `Array` 的其他类冲突，例如 Java 反射 API 或 Javascript 数组中的那些。

- 它更短，这很好。

### mindustry.plugin.Plugin -> mindustry.mod.Plugin

`Plugin` 类已移入 `mod` 包，因为旧包本来就只包含这一个类。

### Call 方法移除 "on" 前缀

`Call` 中所有远程调用方法都去掉了「on」前缀。例如：

- `onSnapshot` -> `snapshot`

- `onSetRules` -> `setRules`

- `onLabel` -> `label`

### 新的玩家系统

既然玩家现在操控单位，他们就不再作为实体存在于游戏中——也就是说，他们没有生命值和武器。每个动作都由 `Unit` 执行。不再有 `Mech` 类，只有 `UnitType`。

- 每个单位都有一个 `UnitController`，它可以是 AI、逻辑或玩家。

- 要检查单位是否由玩家控制，请使用 `unit.isPlayer()`

- 要获取单位的玩家（如果有），请使用 `unit.getPlayer()`

- 设置玩家的位置不会有任何效果。请改为设置单位的位置。
