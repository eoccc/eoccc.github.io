# 插件与 JVM 模组

Mindustry 支持在桌面端与 Android 上加载含 Java 字节码的 `jar` 文件。它们的功能与 JS 模组类似，并且必须提供一个主类，供模组创建时实例化。

理论上，所有 JVM 语言都应受支持。

Jar/JVM 模组使用与标准模组相同的 `mod.hjson` 元数据文件，只多出一项：可用 `main: "mypackage.MyMod"` 指定*完全限定的主类*。该类应继承 `mindustry.mod.Mod`。

如果未指定主类，则默认为 `modnameinlowercase.ModName + "Mod"`。

一个简单的 Java 模组 `mod.hjson` 大致如下：

```
name: "Nothing"
author: "Yourself"
main: "nothing.NothingMod"
description: "..."
version: "99.99"
```

更多说明请参见 [Java 模组示例仓库](https://github.com/Anuken/MindustryJavaModTemplate) 或 [Kotlin 模组示例仓库](https://github.com/Anuken/MindustryKotlinModTemplate)。

## 插件

插件是仅在服务器上运行的 Java 模组，通常用于添加*新命令*或*新游戏模式*。
所有插件主类都应继承 `mindustry.mod.Plugin`。这会使其隐式变为*隐藏*——客户端无需下载插件即可加入服务器，它们仅在服务器端生效。安装插件时，把 JAR 放入 `/config/mods/` 即可。

插件的元数据文件命名为 `plugin.[h]json`，其文件结构与其他 Java 模组完全相同——详见上文。

你可以[在此](https://github.com/Anuken/MindustryPluginTemplate)查看示例插件。若需要可用于真实服务器的更实用示例，请见[该仓库](https://github.com/Anuken/AuthorizePlugin)。

## 导入

与 JS 或 JSON 模组不同，JAR 模组需要编译，因此无法直接从 Github 导入，而要改用 *Github Releases*。

当用户尝试安装 JAR 模组时，Mindustry 会检查最新的（且*仅*检查最新的）Github 发行版中的 `.jar` 产物。找到第一个产物后即下载到客户端。注意，预发行版会被忽略。

建议使用 Github Actions（或任何其他 CI）自动构建并把 jar 产物上传到新的发行版。

## 多线程

除非另有说明，**Mindustry 的代码都不是线程安全的**。从非主线程执行任何操作（例如发送数据包、修改地形）都可能导致随机崩溃或网络错误。若要在主线程上执行代码，请使用 `Core.app.post(() -> { /* code */ })`。

## 能力与安全

由于 jar 模组通过 `URLClassLoader` 直接加载且没有沙箱隔离，因此不受任何安全限制。这意味着：

- 可访问所有 Java API。

- 可使用反射访问私有/隐藏属性。

- 模组可完全访问客户端计算机，从而可能被用于恶意行为。

- 模组可修改游戏文件或重写核心字节码。

因此，*绝不要从不可信来源导入 jar 模组。* 你可能会问：为什么不给 jar 模组加沙箱？这不是巨大的安全风险吗？

答案是：*确实是*。但并没有更好的替代方案。即使我实现一个 `SecurityManager` 来限制模组能力也无济于事——Java 本身就不安全，而任何还算「安全」的沙箱实现（*如果真存在的话*）都需要禁用模组中的反射，这是不可接受的。

作为对比，Forge（*Minecraft 中流行的 Java 模组加载器*）同样没有对模组做沙箱隔离。
