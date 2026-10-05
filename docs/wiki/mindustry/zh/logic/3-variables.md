# 变量与常量

变量和常量本质上是值的“容器”。每个都有名称和值。Mindustry 有可由用户及其代码设置的变量，以及仅由处理器设置、用户无法更改的常量。

*要了解变量或常量可能的数据或参数类型，请参阅术语表。*

## 变量

### 变量的创建与修改

变量顾名思义，就是可以更改的值。

例如，在代码 `set myVariable 3` 中，`set` 指令会创建一个名为 `myVariable` 的变量，并赋予它值 `3`。

之后，可以这样把它的值改为 `9`：`set myVariable 9`。

注意我们对创建和修改变量使用了同一条指令。这是因为**如果某条指令要修改的变量尚不存在，它会先创建该变量。** 如果你了解 Python，大概已经意识到它的工作方式与此相同。

另一个例子是使用 `sensor`：`sensor playerX playerUnit @x`（在可视化编辑器中则为 Sensor playerX = @x in playerUnit）。

假设玩家位置是 `141, 20`，那么会先创建一个名为 `playerX` 的变量，然后赋予它值 `141`。

不过，示例中还有另一个变量 `playerUnit`。该变量是一个**参数**。参数是指令的输入值。在本例中，我们大概是从 `radar` 指令得到了 `playerUnit`。如果未提供参数或参数无效，该指令将不会执行。

### 数据类型与隐式转换

当然，变量中的值有不同的类型，具体取决于来源与用途，例如单位的 `Unit`、任意数字的 `number` 等。你可以在术语表中找到它们的完整列表。

Mindustry Logic 在变量上还有一个叫**隐式转换**的特性。也就是说，在需要时，它会把变量的值从一种类型转换为另一种类型。

如果某条指令需要 `Object` 却被给了 `number`，它会被转换为 `null`；如果需要 `number` 却被给了 `Object`，则当该对象不为 `null` 时转换为 1，否则转换为 0。

示例：

- `53` -> `null`

- `null` -> 0,

- `Object`（一座硅坩埚）-> 1

`print` 指令是唯一一条需要以 `String` 作为输入的指令，因此它的规则在本手册中单独说明。

### 变量命名

恰当命名变量是编程中一项重要的通用技能。它有助于让代码更易读、易懂，从而让别人更容易学习或修复你的代码。

变量名可以包含任何可输入字符。不过，它们不能是纯数字，因为那样会直接使用实际数字。

mlog 代码中最常见的命名约定是 camelCase（小驼峰），它本身就是一个例子。用 camelCase 命名的变量示例有：`playerX`、`coreFound`、`vertexAngle`。

**命名变量时，要确保它们既描述清楚又简短。**它们必须描述所保存的值或其用途。同时，它们不应是完整句子或占满整页，也不应短到令人困惑。你可以使用缩写、首字母缩略词或更短的词来让它们更简洁。

每个人都有自己的风格和偏好，但尽量从 mlog 和其他语言的优秀代码示例中学习，同时保持贴近通用风格。

## 处理器的变量与常量

常量也保存值，但不可更改。每个处理器都内置了这些常量与变量：

### 处理器

#### @this `constant` `Building`

一个表示处理器自身的 `Building` 对象。你可以配合 `sensor` 用它查询处理器的各种属性。

#### @thisx `constant` `number`

处理器的 y 坐标。

#### @thisy `constant` `number`

处理器的 y 坐标。

#### @ipt `constant` `number`

每刻执行的指令数（每秒 60 刻）。

- 微型处理器 -> 2

- 逻辑处理器 -> 8

- 超频处理器 -> 25

#### @counter `variable` `number`

一个表示处理器接下来将从哪一行读取代码的变量，相当于 x86 中的 `%IP`。它可以像其他变量一样被修改，作为执行跳转的另一种方式。

一个（高级）示例：设置 `@counter` 跳转到一个函数，然后再跳回调用方：

```
op add retAddr @counter 1 # Save where we will continue after the function returns by adding 1 to the counter
set @counter myFunc       # Jump to the line representing myFunc
...
set @counter retAddr      # Return to the line set earlier after the function is called
```

### 相关链接

#### @links `constant` `number`

一个等于链接到处理器的建筑数量的常量。当方块被链接或取消链接时，由处理器更改它。

你可以配合 `getlink` 遍历所有已链接的建筑，像这样：

```
set linkIter 0                  # Create iterator variable
getlink block linkIter          # Get Building Object of the "linkIter"th linked building.
# Do what you want with the building here
jump 1 lessThan linkIter @links # Loop
```

#### `constant` `Building`

这实际上是多个常量，每个都对应一个链接到处理器的建筑。每当建筑被链接或取消链接到处理器时，它们会被添加或移除。

`buildingName` 表示建筑的**内部名称**，你可以在 Wiki 的其余部分找到它。

`n` 从 1 开始，每链接一个该类型的建筑就递增。它有点像是某类型建筑中的第 `n` 个。

这可能有点难以理解，所以这里举几个例子：

- 链接到处理器的第一个散射炮：`scatter1`

- 第三个链接的涟漪：`ripple3`

- 第二个链接的激光钻头：`drill2`

- 第十一个链接的孢子压榨机：`press11`

选中处理器时，你还可以在每个已链接建筑上方看到它的“常量名”。

<img src="../../../../../ext/img/mindustry/misc/logic-variables-constants-links-linkedBuilding.png" alt="">

### 杂项

#### @unit `constant` `Unit`

一个表示当前已绑定单位的常量。只有当处理器解绑单位或绑定另一个单位时它才会变化。可以通过 `ucontrol`、`ulocate`、`uradar` 等单位指令访问它。由于它是 Unit 对象，你也可以配合 `sensor` 使用。

这体现了 mlog 中单位控制的核心部分：**同一时间只能绑定一个单位。** 不过，你可以在变量中引用它，例如 `set unitReference @unit`。但该变量不能用来控制所引用的单位，只能用来与其他单位比较或获取它的信息。因此，你可以把它看作一个“单位身份标识”。

#### @time `constant` `number`

表示当前的 UNIX 时间戳*（以毫秒为单位）*。

#### @tick `constant` `float`

表示自地图开始以来经过的刻数（每秒 60 刻）。

#### @mapw `constant` `number`

地图宽度，以格为单位。

#### @maph `constant` `number`

地图高度，以格为单位。
