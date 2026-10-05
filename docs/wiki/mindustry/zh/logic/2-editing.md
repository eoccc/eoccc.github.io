# 代码的编写与编辑

编写 Mindustry Logic 有两种主要方式：可视化编辑器与手动编辑。各有各的优势，选择最适合你的即可。

## 可视化编辑器

可视化编辑器是处理器的“编辑”界面（当你按下“铅笔”按钮时）。**这是推荐新手使用的方式**，因为它被设计得易于理解和使用。

与手动编辑相比，这种方式编辑的优点是：

- 基于块、带颜色标记的拖放式界面

- 便捷的参数选择器，显示所有需要的参数

- 可视化的、易于设置的跳转关系

- 移动端友好

<img src="../../../../../ext/img/mindustry/misc/logic-editing-visualEditor-overview.png" alt="">

你也可以在文本形式之间导出和导入代码。

## 手动编辑

手动编辑是指使用文本编辑器（如 Notepad++、Vim 或 Visual Studio Code）来编辑代码。**对于更高级的用户和更长的代码，手动编辑是更好的选择**。

与可视化编辑器相比，手动编辑代码的优点是：

- 比可视化编辑器更紧凑；同一时间能看到更多代码

- 输入比在长长的代码墙上拖放更快

- 无需打开 Mindustry 即可编写用于演示的简短代码

- 部分编辑器支持语法高亮，例如 [VS Code（插件）](https://marketplace.visualstudio.com/items/?itemName=JeanJPNM.mlogls-vscode)、[Emacs（软件包）](https://github.com/vednoc/masm-mode)、[Vim（插件）](https://github.com/purofle/vim-mindustry-logic) 与 [Sublime Text（软件包）](https://github.com/gigamicro/Mindustry4Sublime)

- 文本块不会遮挡参数文本的一部分

- 能够在 Mindustry 之外保存和访问代码

不过，对新手或不太习惯编辑代码的人来说可能有点困难，因为变量必须显式输入，而且没有可视化引导时跳转会变得非常混乱，等等。
