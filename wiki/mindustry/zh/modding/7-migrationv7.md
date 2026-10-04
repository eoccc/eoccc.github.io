# 7.0 迁移指南

## 方块

- `Block#expanded` 现已弃用且不产生任何效果，请改用 `Block#clipSize`。该字段被保留以确保兼容性，但最终会被移除。

- 所有 `mindustry.world.meta.values.*` 类都已替换为 lambda。参见 `StatValues` 类。

- `BlockForge` 已移出实验性包，并且很可能会经历重大改动。如果你在 Java 模组中使用了这个类，我建议把它复制进来，以便继续使用旧版本。其他实验性方块也可能被移出。

- `CacheLayer` 现在是一个包含可覆写方法的类——而不是枚举。可以用 `CacheLayer#add` 注册新图层。

- 各种字段（如 `variants` 和 `attributes`）已从 `Floor` 移至 `Block`。

- `Iconc` 及相关方法已被移除；请使用 `UnlockableContent.uiIcon/fullIcon`。

- `Smelter` 和 `AttributeSmelter` 已弃用。这些类的绘制功能是硬编码的。请尽快迁移到搭配 `DrawSmelter` 的 `GenericCrafter`。如需属性支持，请使用 `AttributeCrafter`。

- `Cultivator` 因与 `Smelter` 相同的原因而弃用，请改用 `AttributeCrafter`。

- `ExtendingItemBridge` 和 `LiquidExtendingBridge` 已合并到 `ItemBridge` / `LiquidBridge`，请改用它们。

- `PayloadAcceptor` 这个名称具有误导性，且位于错误的包中，请改用 `PayloadBlock`。

- 生成的图标现在**必须**在 `createIcons` 中创建；尝试使用 `Core.atlas.addRegion` 根本不会生效。

- `LiquidModule#total()` 已弃用；请改用 `currentAmount()`。

## 弹药

- 任何处理单位弹药（ammo）的模组代码现在都会失效。

- `ResupplyPoint` 类已被移除。

- `AmmoType` 现在是接口，而不是类。

- `AmmoTypes` 已被移除，请改为创建新的实例。

- 弹药类型类已移入 `mindustry.type.ammo` 包。

- `ContentType.ammo` 已被「移除」，因为弹药不再是内容。

## 电弧

- `Pixmap` 的 API 已完全改变。大多数方法现在默认禁用混合，颜色/混合/缩放参数也不再是 `Pixmap` 状态机的一部分。大多数与图像相关的方法现在是纯 Java，而不再是 JNI + C。

- `SettingsDialog`（`Vars.ui.settings`）已移入 Mindustry 的代码库。严格来说这并未改变 API；但用 6.0 源码编译的 Java 模组会尝试访问一个不存在的类的不存在字段，从而导致崩溃。用 v7 的 Mindustry/arc 依赖重新编译应该就能解决这个问题。

- TextureAtlas 现在使用更小、更快的 `aatls` 二进制格式。请更新你的 Arc 依赖以读取它。

- `Core.net` 已被移除，请改用 `arc.util.Http` 中的静态方法。

- `RidgedPerlin` 已重命名为 `Ridged`。

- `Simplex` 和 `Ridged` 现在是无状态的；现在请使用静态方法生成噪声。种子是一个参数。

## 网络

- 用于数据包的 `Registrator` 已移至 `Net`，注册方法也已公开，以便在 Java 模组中可能使用。

- `InvokePacket` 已被移除，取而代之的是直接处理事件的生成数据包类。

- `RemoteRead{Server, Client}` 也已被移除。

- `Packet` 现在是抽象类，而不是接口。

## 杂项

- 在许多情况下不再调用 `BulletType#despawned`，如果你需要监听所有移除事件，请使用 `#removed`

- `Attribute` 现在是普通类，而不是枚举。请使用 `Attribute.add` 注册新的属性。

- `Vars.miningRange` 已移至 `UnitType`。

- `Tex` 中的所有字段现在都是 `Drawable`，而不是 `NinePatchDrawable` 或 `TextureRegionDrawable`。为什么？这些字段是从图集加载的，这意味着更改 UI 精灵图或使用过时图集的模组以前可能导致 `ClassCastException` 崩溃。

## 精灵图

- 现在会为单位和武器精灵图自动生成描边。腿部区域目前除外。

- 现在启用线性过滤时，所有模组精灵图都会在加载时自动进行 alpha 溢出（alpha-bleed）处理——无需手动操作。
