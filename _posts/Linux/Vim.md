### vim + filename

```
    I --  edit
    : --  command
    wq
    q --  exit
    w -- reserve
    ggyG -- dG
    G ：光标移到最后一行 

    选中内容以后就可以其他的操作了，比如： 
    d  删除选中内容 
    y  复制选中内容到0号寄存器 
    "+y  复制选中内容到＋寄存器，也就是系统的剪贴板，供其他程序用 

```

### Shift/ Amend

```
CTRL + a --- first word
CTRL + e --- end word

CTRL + w --- delete the left word
CTRL + k --- clean the word to the right

SHIFT + PageUp/ PageDwon

CTRL + r --- find cmd history 
```

### Find

```
/text;    --- 查找text，按n健查找下一个，按N健查找前一个。

/hello\>  --- find start with hello

# hello位于行首
/^hello

# world位于行末
/world$


```

### Copy

```
yy or Y   复制游标所在的整行（3yy表示复制3行）

p --- paste
```

### Undo

```
u 撤销（Undo）

U 撤销对整行的操作

Ctrl + r 重做（Redo），即撤销的撤销。
```

### Blank Line

```
o or O --- insert mode
```

### Move Cursor

```
w --- next word
b --- last word

fx - jump to the previous occurrence of character x
Fx - jump to the previous occurrence of character x

)( --- move by sentense



```

