# 编程语言与数据格式

本分支按「语言」组织：每种语言各自成组，便于后续加入新的语言（如 YAML、TOML）而不打乱既有结构。

内容分两类：**标记语言**（Markdown）用于撰写本站页面本身；**数据格式**（JSON、HJSON）用于 Mindustry 的模组、数据补丁与内容定义。

## 本分支讲什么

- 这些语言的**语法结构**与书写规则
- 它们之间的**关系**与差异
- 在本站与 Mindustry 中**如何使用**

## 分支结构

| 分组 | 页面 | 内容 |
|---|---|---|
| **Markdown** | [Markdown 总览](markdown/) | 标记语言总览、学习路径与两条贯穿全篇的原则 |
| | [基础语法](markdown/basics.md) | 标题、段落、强调、列表、链接、图片、引用、分隔线 |
| | [进阶语法](markdown/advanced.md) | 表格、代码块、转义、HTML 混排、属性列表 |
| | [本站渲染规则](markdown/extensions.md) | 本站启用的扩展、支持与不支持哪些写法 |
| | [细节与常见错误](markdown/pitfalls.md) | 缩进、空行、嵌套、符号冲突等高频踩坑点 |
| | [速查表](markdown/cheatsheet.md) | 一页速览，写作时对照用 |
| **JSON** | [JSON 基础](json.md) | 标准 JSON 的语法结构、数据类型、书写规则与限制 |
| | [HJSON 基础](hjson.md) | HJSON 的宽松语法、注释支持，以及与 JSON 的关系 |
| | [JSON 与 HJSON 对比](compare/) | 语法差异速查、转换方式与选用建议 |

> HJSON 归入 **JSON** 分组，是因为它是 JSON 的**超集**——二者共享同一套数据模型，只是书写严格程度不同。

## 支持的语言

| 语言 | 全称 | 在本站中的定位 |
|---|---|---|
| Markdown | — | **标记语言**：本站全部页面（含本页）的撰写格式 |
| JSON | JavaScript Object Notation | 基准数据格式，最广泛使用 |
| HJSON | Human JSON | JSON 的可读化超集，适合手写 |

后续如需补充其他语言（YAML、TOML 等），在侧边栏新增同级分组即可，不会影响现有页面。

## 为什么需要了解它们

**Markdown** 是本站所有页面的撰写格式。改一个错别字也要用它，因此它是参与共建的**最低门槛技能**：语法掌握得越准，排版问题越少。系统讲解见 [Markdown 总览](markdown/)。

**JSON 与 HJSON** 是 Mindustry 的配置载体。Mindustry 的内容系统（方块、物品、单位、武器等）本质上是**结构化的数据**，游戏加载模组时会解析这些文本文件并据此构造对象。因此：

- 读得懂格式，才能看懂别人写的模组
- 写对格式，你的配置才会被正确解析
- 理解不同格式的差异，才能在「严格」与「易写」之间做取舍

## JSON 与 HJSON 的关系

一句话概括：**HJSON 是 JSON 的超集**。

<img src="/wiki/langs/assets/json-superset.svg" alt="JSON 与 HJSON 的集合关系：HJSON 是 JSON 的超集，合法 JSON 同时是合法 HJSON">

这意味着：

- 任何**合法的 JSON**，都是合法的 HJSON——可以直接被 HJSON 解析器读取
- HJSON 额外允许一些 JSON 不允许的写法（如注释、无引号键名、省略逗号）
- 反过来不成立：用了 HJSON 特有语法的文件，**不是**合法 JSON

## JSON 的来路与去向

JSON 从 JavaScript 的对象字面量语法中提炼而来，2006 年起进入标准化进程，2017 年的 **RFC 8259** 成为现行标准（互联网标准 STD 90）。它语法极小、语言无关，在 Web API 与配置领域取代 XML 成为事实标准。

它也有明显短板——不支持注释与尾随逗号，手写不便。HJSON、JSON5 等方言正是在**保持数据模型不变**的前提下放宽书写规则。

完整的发展脉络、标准化里程碑与未来走向，见 [JSON 的发展历程与现代前景](json-history.md)。

## 格式选择速查

| 你的情况 | 建议格式 |
|---|---|
| 撰写或修改本站页面 | Markdown |
| 手写配置、想加注释说明 | HJSON |
| 程序生成、需要格式唯一 | JSON |
| 要交给只认标准 JSON 的工具 | JSON |
| 从已有 JSON 改造、想逐步加注释 | HJSON（原文件直接可用） |
| 团队协作 | 统一其一，避免混用 |

## 在本站其他文档中的使用

这些语言在以下位置出现，可结合阅读：

- [Markdown 写作规范](../../dev/writing/) —— 撰写本站页面时的命名、用词与章节组织规范
- [数据补丁](../mindustry/zh/datapatches/) —— 补丁文件用 JSON 或 HJSON 编写
- [模组开发](../mindustry/zh/modding/1-modding/) —— 模组内容以 JSON 格式描述
- [模组类文档](../mindustry/zh/Modding%20Classes/) —— 各类的字段与默认值

## 阅读建议

如果你完全没有接触过这些格式，建议按 **Markdown → JSON 基础 → HJSON 基础 → 两者对比** 的顺序阅读：先掌握本站页面的撰写格式，再理解严格的数据格式规则，然后看 HJSON 放宽了哪些地方，最后对照速查。

若你只关心「为什么是 JSON 而不是别的」，可直接阅读 [JSON 的发展历程与现代前景](json-history.md)。
