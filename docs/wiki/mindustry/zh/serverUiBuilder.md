# 服务器界面构建系统

## 该系统的设计初衷

过去服务器只能使用 `Call.menu`，它仅支持一个普通的按钮网格，别无其他。

UI 构建器提供了一种在服务器端创建动态、可序列化 UI 树的方式，并支持每个对话框返回多个值。

*注意：该系统仅在 build 160+ 中可用。*

## 对话框示例

```
static int voteId; //ID of vote menu

static{
    //register handler once
    voteId = Menus.registerMenuBuilder((player, result) -> {
        Log.info(result); //for debugging

        if(result.is("vote1")){ //player pressed vote1 button
            MenuBuilder.of(
            """
            id: table1
            background: button
            margin: 10
            image{
              region: "ok"
              size: 300
            }
            row
            label: "you voted!!!!"
            """).id(voteId).update(player, "table1");
        }else if(result.is("vote2")){ //player pressed vote2 button
            MenuBuilder.of(
            """
            id: table2
            background: button
            margin: 10
            image{
              region: "ok"
              size: 300
            }
            row
            label: "you voted!!!!"
            """).id(voteId).update(player, "table2");
        }else if(result.is("ok")){ //player pressed 'ok' button (it has clicked: ok)
            //hide menu
            Call.hideMenuBuilder(player.con, voteId);
            //search label
            Call.infoMessage(player.con, "You typed: " + result.getString("searchLabel"));
        }
    });
}

public static void show(){
    //if you don't want to parse the DSL each time (might be a little slow), you can cache it with UiBuilder.parse("yourDsl") as a static field and pass that to MenuBuilder.
    MenuBuilder.of("""
    defaults{
      pad: 2
    }
    table{
      id: table1
      background: button
      margin: 10
      image{
        region: "ranai"
        size: 300
      }
      row
      //note: you can add a bundle to assets/bundles, and use "@somebundlekey" for text instead, which will automatically be localized!
      label: "Map 1"
    }
    table{
      id: table2
      background: button
      margin: 10
      image{
        //regions can be data patch regions too, e.g. dp-mysprite
        region: "cat"
        size: 300
      }
      row
      label: "Map 2"
    }
    row
    button{
      fillX: true
      height: 60
      text: "Vote for map 1"
      clicked: vote1
    }

    button{
      fillX: true
      height: 60
      text: "Vote for map 2"
      clicked: vote2
    }
    row
    table{
      colspan: 2
      height: 50
      growX: true
      image{
        region: zoom
        size: 32
        padRight: 8
      }
      label: "Input text here..."
      field{
        //by setting an ID, the value will be returned in the result, so you can call result.getString("searchLabel")
        id: searchLabel
        growX: true
      }
    }
    row
    button{
      icon: ok
      text: "Do something"
      //result will be 'ok' when this is clicked
      clicked: ok
      colspan: 2
      width: 200
      height: 60
    }
    """)
    .id(voteId) //menu ID, important, unless you're reusing IDs
    .title("Select Map") //can be null for no title table at all
    //.token(someLong) //you can pass an optional long token if you want to reuse menu IDs; this is returned in menu results, and can be used for tracking which specific menu the player had opened
    .hideOnClick(false) //do not hide automatically when a button is clicked
    .show(Groups.player.find(p -> !p.isLocal())); //show to first online player (for testing), substitute for proper person
}
```

## Builder API 与 DSL 对比

两者生成相同的 `NodeBuilder` 树，可视情况选择更便利的一种。对于静态布局，DSL 更简洁；而当布局依赖数据时（Java 中的循环与条件），Java 构建器更易用。

**构建器 API：**

```
import static mindustry.ui.builder.UiBuilder.*;

TableBuilder ui = table()
    .add(defaults().pad(2))
    .add(
        table().background("button").margin(10)
            .add(image().region("ranai").size(300))
            .row()
            .add(label("Map 1"))
    )
    .row()
    .add(button("Vote for map 1").fillX().height(60).clicked("vote1"));

MenuBuilder.of(ui).id(voteId).title("Select Map").show(player);
```

**DSL：**

```
MenuBuilder.of("""
defaults{
  pad: 2
}
table{
  background: button
  margin: 10
  image{
    region: "ranai"
    size: 300
  }
  row
  label: "Map 1"
}
row
button{
  fillX: true
  height: 60
  text: "Vote for map 1"
  clicked: vote1
}
""").id(voteId).title("Select Map").show(player);
```

## DSL 的编辑与预览

如需语法高亮、校验与自动补全，可以安装 [IntelliJ 插件](https://github.com/Anuken/MindustryUiDslIntelliJ)。

配置完成后，用你惯用的编辑器打开 `.msui` 文件。启动 Mindustry，在控制台（在开发者选项中启用，按 F8 打开）中输入：

`UiHotReload.show()`

这会打开一个文件选择窗口。选中你的 `.msui` 文件后，游戏内对话框会自动显示你正在编辑的布局文件，并在文件变化时实时重载。

## 条件布局（竖屏与横屏）

节点接受 `condition` 字符串。若其求值为假，该节点会被完全跳过（而非仅仅隐藏）。该判断在客户端构建时进行，因此会自然适配每位玩家各自的屏幕形状。

支持的判断条件：`"portrait"`、`"landscape"`，或 `"  "`，其中 `op` 为 `>=`、`>`、`
```
table{
  condition: "landscape"
  row
  label: "Wide layout: map previews side by side"
}
table{
  condition: "portrait"
  row
  label: "Narrow layout: map previews stacked"
}
table{
  condition: "width >= 900"
  label: "Extra info panel, only on large screens"
}
```

由于该判断在构建树时按客户端执行，因此同一条由服务器下发的 DSL 字符串，会让每位玩家看到适配自身窗口的布局。

## 更多示例

### 可搜索的玩家列表（builder API）

显示玩家列表，可通过搜索框筛选；点击搜索时在原位置重建筛选后的列表。菜单处理器在静态块中注册一次。

`update(player, "list")` 按 id 替换单个元素，而不是整个对话框。该更新会构建带行的 `pane{ id: list }` 节点并发送，而初始的 `show` 调用会构建完整对话框（含搜索栏）。这就是 `buildList` 被拆分为独立方法、而非放在 `buildRoot` 中的原因。

```
//replace with real player names
static String[] players = {"Alice", "Bob", "Charlie", "Dave", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"};
static int listId;

static{
    listId = Menus.registerMenuBuilder((player, result) -> {
        if(result.is("search")){
            String query = result.getString("query", "");
            //rebuild inner contents of search pane
            MenuBuilder.of(buildList(query)).id(listId).update(player, "list");
        }else if(result.result != null && result.result.startsWith("kick:")){
            String target = result.result.substring("kick:".length());
            Call.infoMessage(player.con, "Kicked: " + target);
        }
    });
}

public static void showPlayerList(Player viewer){
    MenuBuilder.of(buildRoot("")).id(listId).hideOnClick(false).title("Players").show(viewer);
}

private static TableBuilder buildRoot(String query){
    return table()
    .add(defaults().pad(4))
    .add(
        table().growX()
        //note: enter("search") makes the text field fire 'search' when enter is pressed, for convenience
        .add(field(query).id("query").enter("search").hint("Search players...").growX())
        .add(button("Go").clicked("search"))
    )
    .row()
    .add(buildList(query));
}

private static PaneBuilder buildList(String query){
    TableBuilder rows = table();
    for(String name : players){
        if(!query.isEmpty() && !name.toLowerCase().contains(query.toLowerCase())) continue;
        rows.add(image("players").size(32f).padRight(5f))
        .add(label(name))
        .add(button("Kick").padRight(10f).width(150f).clicked("kick:" + name))
        .row();
    }
    return pane().id("list").add(rows);
}
```

目标玩家的名字被直接写进 `clicked` 结果字符串（`"kick:" + name`），因为普通按钮没有其他可挂载带 id 值的地方。初始 `show` 时设置了 `hideOnClick(false)`，因此点击搜索或踢人后对话框仍保持打开，因为这两者都意在原地更新列表，而不是关闭菜单。

### 带滑条阈值的投票踢人确认框

```
defaults{
  pad: 6
  width: 300
}
label{
  text: "Reason: tomfoolery."
  labelAlign: center
}
row
slider{
  id: threshold
  min: 1
  max: 8
  step: 1
  defaultValue: 3
  text: "Votes needed"
}
row
button{
  text: "Start Vote"
  icon: ok
  clicked: startVote
  fillX: true
  height: 50
}
```

当返回 `startVote` 时，服务器会读取 `result.getFloat("threshold")`。

### 含复选框与分组按钮的服务器设置面板

```
defaults{
  pad: 8
}
check{
  id: Bingus
  text: "Enable bingus"
  checked: true
}
check{
  id: frogs
  text: "Enable frogs"
  checked: false
}
row
label: "Difficulty"{ //placing it here is shorthand for text
  colspan: 2
  labelAlign: center
  fillX: true
}
row
table{
  colspan: 2
  defaults{
    width: 200
    height: 50
  }
  button: "Easy"{ //also shorthand for text
    group: difficulty
    id: diffEasy //no clicked: here because it shouldn't close the dialog
    style: togglet
  }
  button: "Normal"{
    group: difficulty
    id: diffNormal
    style: togglet
  }
  button: "Insufferable"{
    group: difficulty
    id: diffInsufferable
    style: togglet
  }
}
row
button: "Save"{
  clicked: save
  colspan: 2
  fillX: true
  height: 50
}
```

`group: difficulty` 让三个难度按钮互斥（一个 `ButtonGroup`），其 `checked` 状态会在 `values` 中返回给任何带 id 的可勾选元素，因此服务器在按下 “save” 时能读取当前选中的是哪一个。

## 单元格属性

这些作用于节点在其父表格中所占的*单元格*，对应 `scene2d` 表格布局。布尔属性在构建器 API 中不取值（直接调用方法即可）；在 DSL 中写作 `key: true` 或 `key: false`。

| Property | Type | 描述 |
|---|---|---|
| `grow` | bool | 在两个方向上扩展并填充。 |
| `growX` | bool | 水平扩展并填充。 |
| `growY` | bool | 垂直扩展并填充。 |
| `fill` | bool | 在两个方向上填充单元格（不扩展）。 |
| `fillX` | bool | 水平填充单元格。 |
| `fillY` | bool | 垂直填充单元格。 |
| `expand` | bool | 在两个方向上占用额外的可用空间。 |
| `expandX` | bool | 占用额外的可用水平空间。 |
| `expandY` | bool | 占用额外的可用垂直空间。 |
| `uniform` | bool | 强制该单元格在两个方向上与其他 uniform 单元格尺寸一致。 |
| `uniformX` | bool | 强制与其他 uniform 单元格宽度一致。 |
| `uniformY` | bool | 强制与其他 uniform 单元格高度一致。 |
| `width` | float | 固定单元格宽度。 |
| `height` | float | 固定单元格高度。 |
| `size` | float | 同时固定宽度与高度。 |
| `minWidth` | float | 最小宽度。 |
| `maxWidth` | float | 最大宽度。 |
| `minHeight` | float | 最小高度。 |
| `maxHeight` | float | 最大高度。 |
| `pad` | float | 四周内边距。 |
| `padTop` | float | 顶部内边距。 |
| `padLeft` | float | 左侧内边距。 |
| `padBottom` | float | 底部内边距。 |
| `padRight` | float | 右侧内边距。 |
| `align` | string | 单元格内的对齐方式（`top`、`bottom`、`left`、`right`、`center`、`topLeft`、`botLeft`、`topRight`、`botRight`）。 |
| `colspan` | int | 该单元格跨越的列数。 |
| `color` | string | 单元格的着色（十六进制字符串或颜色名，例如 `"white"` 或 `"ffaa00"`）。无论节点类型如何，都作用于其单元格。 |

注意：`defaults{}` 块会把单元格属性应用到同一表格主体内其后添加的每个同级节点，但不会进入嵌套的 `table{}`/`pane{}` 块。

注意：`disabled`（bool）也会作用于单元格层级，但仅对实现了 `Disableable` 的元素有效——`button`、`imageButton`、`field`、`check`、`slider` 与 `buttonTable`。它设置元素的初始禁用状态。

## 元素

| Node | 用途 | 示例（DSL） |
|---|---|---|
| `table` | 嵌套的表格/容器。 Supports `background`, `margin`, `wrap` (switches to a `WrapTable` instead of `Table`, which ignores rows/columns). | `table{ background: button margin: 10 label: "hi" }` |
| `pane` | 包裹内部表格的可滚动容器。 Supports `style`. | `pane{ label: "scrollable content" }` |
| `stack` | 将其子节点层叠在一起的容器（所有子节点共用同一单元格）。 No node-specific properties. | `stack{ image{ region: "ok" size: 300 } label: "Overlaid text" }` |
| `label` | 文本标签。 Supports `text`, `wrap`, `style`, `labelAlign`. Resolves `@bundleKey` text itself, which can be sourced from bundles in the server assets/bundles folder. | `label: "Hello"` |
| `image` | 来自纹理图集的图片或图标。 Supports `region`/`icon`, `scaling`, `size`. | `image{ region: "ok" size: 300 }` |
| `button` | 文本按钮，可选图标。 Supports `text`, `icon`, `style`, `clicked`, `group`, `checked`, `disabled`. | `button{ text: "Vote" clicked: vote1 }` |
| `imageButton` | 纯图标按钮。 Supports `icon`, `style`, `clicked`, `group`, `checked`, `disabled`. | `imageButton{ icon: ok clicked: confirm }` |
| `field` | 文本输入框。 Supports `text`, `hint`, `maxLength`, `style`, `disabled`, and `id` to read back the value. | `field{ id: search hint: "Search..." growX: true }` |
| `check` | 复选框。 Supports `text`, `checked`, `style`, `group`, `disabled`, `id`. | `check{ id: ranked text: "Ranked only" checked: true }` |
| `slider` | 滑块。 Supports `min`, `max`, `step`, `defaultValue`, `style`, `disabled`, `id`, `text`. Text can be a format string that contains `{0}` from a bundle. | `slider{ id: kickVotes min: 1 max: 10 step: 1 defaultValue: 3 text: "Votes: " }` |
| `space` | 空单元格，可用作间隔。 | `space` |
| `buttonTable` | 同时可作为其他节点容器的 `Button`（整张可点击的表格）。 Supports `style`, `clicked`, `group`, `margin`, `disabled`. | `buttonTable{ clicked: pick1 label: "Map 1" }` |
| `defaults` | 不是真正的元素；为本块中后续同级节点设置单元格属性默认值。 | `defaults{ pad: 4 }` |
| `row` | 不是节点；结束当前行并开始新的一行。 | `row` |

任何设置了 `id` 的节点，其元素都会以该 id 注册。对于交互元素（`field`、`slider`、`check`、可勾选的 `button`/`buttonTable`），当任何带 `clicked` 结果的按钮触发时，该 id 会作为键出现在 `MenuResult.values` 中。

# Button Styles

`Styles` 上可用样式名的参考；可通过 `button`/`buttonTable`（`TextButtonStyle`）与 `imageButton`（`ImageButtonStyle`）节点上的 `style: "name"` 使用。

## 文本按钮样式（button 元素）

| Name | 描述 |
|---|---|
| `defaultt` | 默认文本按钮样式，45 度灰色切角。 |
| `flatt` | 扁平、方形、不透明。 |
| `grayt` | 扁平、方形、不透明、灰色。 |
| `flatTogglet` | 扁平、方形、可切换。 |
| `flatBordert` | 扁平、方形、灰色边框。 |
| `nonet` | 完全无背景，只有文字。 |
| `logicTogglet` | 与 `flatToggle` 类似，但为逻辑做了小幅调整。 |
| `flatToggleMenut` | 与 `flatToggle` 类似，但基础背景为透明。 |
| `togglet` | 默认样式的切换变体。 |
| `cleart` | 半透明方形按钮。 |
| `clearTogglet` | 透明、方形、橙色边框，可切换。 |
| `fullTogglet` | 与 `flatToggle` 类似，但没有更深的边框。 |
| `squareTogglet` | `flatBorder` 的可切换版本。 |
| `logict` | 用于逻辑对话框的特殊方形按钮。 |

## 图像按钮样式（imageButton 元素）

| Name | 描述 |
|---|---|
| `defaulti` | 默认图片按钮样式，45 度灰色切角。 |
| `nodei` | 用于科技树中的研究节点。 |
| `emptyi` | 无背景，悬停时给图片本身着色。 |
| `emptyTogglei` | `emptyi` 的可切换变体。 |
| `selecti` | 选中时在图片周围显示边框，用于放置片段。 |
| `logici` | `emptyi` 的纯黑版本，用于逻辑工具栏。 |
| `geni` | 用于地图生成筛选器的工具栏。 |
| `grayi` | 灰色、可切换、无背景。 |
| `graySquarei` | 灰色方形背景，标准行为。等同于 `grayt`。 |
| `flati` | 扁平、方形、黑色背景。 |
| `squarei` | 方形边框。 |
| `squareTogglei` | 方形边框，可切换。 |
| `grayTogglei` | 方形边框，可切换。 |
| `clearNonei` | 除聚焦外无背景，无边框。 |
| `cleari` | 半透明黑色背景。 |
| `clearTogglei` | `cleari` 的可切换变体。 |
| `clearNoneTogglei` | `clearNone`，但可切换。 |

*注意：buttonTable 元素可以使用这些按钮样式中的任意一种。*
