# 标记语言

文本渲染器使用一种简单的标记语言为文本着色。

- `[name]` 按名称设置颜色，有一些[内置颜色](#built-in-colors)；

- `[#rrggbb]` / `[#rrggbbaa]` 按十六进制值设置颜色，每个值的范围是 `00` 到 `ff`：
`rr` 是红色值，

- `gg` 是绿色值，

- `bb` 是蓝色值，

- `aa` 是透明度值；

- `[]` 把颜色恢复为上一个颜色；

- `[[` 用于转义左方括号，因此你可以写 `[[red]`，它会渲染为 `[red]`。

备注：

- 错误/未知的颜色会被静默忽略。

示例：

```
[red]red
[#ff0000]full-red
[#ff000066]half-red
[#ff000033]half-half-red
[#00ff00]green
[]half-half-red
```

### 内置颜色

```
[clear]clear (#00000000)
[black]black (#000000FF)
[white]white (#FFFFFFFF)
[lightgray]lightgray (#BFBFBFFF)
[gray]gray (#7F7F7FFF)
[darkgray]darkgray (#3F3F3FFF)
[blue]blue (#0000FFFF)
[navy]navy (#00007FFF)
[royal]royal (#4169E1FF)
[slate]slate (#700090FF)
[sky]sky (#87CEEBFF)
[cyan]cyan (#00FFFFFF)
[teal]teal (#007F7FFF)
[green]green (#00FF00FF)
[acid]acid (#7FFF00FF)
[lime]lime (#32CD32FF)
[forest]forest (#228B22FF)
[olive]olive (#6B8E23FF)
[yellow]yellow (#FFFF00FF)
[gold]gold (#FFD700FF)
[goldenrod]goldenrod (#DAA520FF)
[orange]orange (#FFA500FF)
[brown]brown (#8B4513FF)
[tan]tan (#D2B48CFF)
[brick]brick (#B22222FF)
[red]red (#FF0000FF)
[scarlet]scarlet (#FF341CFF)
[coral]coral (#FF7F50FF)
[salmon]salmon (#FA8072FF)
[pink]pink (#FF69B4FF)
[magenta]magenta (#FF00FFFF)
[purple]purple (#8000FFFF)
[violet]violet (#EE82EEFF)
[maroon]maroon (#B03060FF)
```
