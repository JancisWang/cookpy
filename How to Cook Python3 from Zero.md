# How to Cook Python3 from Zero

## 前言

> **Life is short**
> **(You need Python)**
> *--Bruce Eckel*
> *ANSI C++ Comitee member*

过去的一段时间里，不止一个人说过想要学习一门程序语言，我呢，非常推荐学习 Python。

在2015年9月，除了那时学习的 Matlab 外，我想深入学习一门程序语言，理解其语言机制。当时纠结着 R , Julia 以及 Python。当时没有考虑效率，而是从实用性上选择的，我想要的不仅仅是科学计算，处理数据，还应当可以做些小玩意儿，搞点惊喜w～然后选择了Python。当然，这期间一直在学在用的还有 JavaScript，毕竟这东西的用处太广了。

这一次主要分为这几个部分，Python的环境，基础数据类型，部分常用标准库介绍，最常用的第三方库介绍，一些语法糖，最后做个有趣有用的小东西w～

Python 版本众多，主要分为 Python2（目前最新的是 Python 2.7.13）和 Python3（目前最新的是 Python 3.6.0）。个人觉得 Python3 比 Python2 前途光明，以前不用 Python3 是因为兼容性问题，现在一些著名模块都开始不兼容Python2 了（说的就是Django），还用2干嘛？这次的文章使用的就是Python 3.6.0。

啊，趁着这次机会，一边写这个，一边复习 Python，还能让可怜的博客文章数量增加，真是好棒w

对了，开头那句话，之后有了很多个重构版：

> 2007 -> **Life is short, use Python!**
> 2007 -> **人生苦短，我用python!**
> 2013 -> **Life is shit, go Pythonic!**
> 2014 -> **Life is short, suck Python!**
> 
> latest -> **life's pathetic, let's Pythonic**

## 环境

### 安装 Python

任何高级语言都需要有自己的一个编程环境，Python 也不例外，先要装点东西才能用的。所需要安装的东西都在这个页面里面[^fn1]：[www.python.org/downloads](www.python.org/downloads/)。

#### windows

到下载页面，下载最新的 windows 安装包。不断的下一步，搞定。

#### macOS

Mac 是自带 Python2 的，在 Terminal 中输入`python`，但我们这里需要用的是 Python3。

Mac 安装 Python 可以和 windows 一样，去下载页面，下载安装。另外一种比较推荐的是通过 [homebrew(http://brew.sh)](http://brew.sh) 来安装。从 Terminal 中输入安装 homebrew 

```zsh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

之后安装Python3

```zsh
brew install python3
```

#### Linux & Unix

都用这两个了，还用说嘛，不管是从源码自己编译，还是直接用别人编译好的，相信你肯定都能搞定的。

### 安装 Python 的包管理系统

Python 拥有着大量的软件包。如果你是通过下载页面下载安装的 Python，或者是通过 homebrew 安装的 Python，那已经拥有一个自带的包管理系统 "pip" 了，只需要更新它[^fn2]:

```zsh
pip install -U pip
```

[^fn1]: [www.python.org](www.python.org/) 是 Python 的官网。
[^fn2]: 可能你需要把输入的`pip` 改为 `pip3`

### Python 的集成开发环境(IDE)推荐

做完之前的，在 Terminal 中输入 `python3` 或者应用程序里直接打开 Python，不管怎样，肯定能够找到一个地方，运行 Python，进入 Python 的交互模式。就像下面一样：

```Python
Python 3.6.0 (default, Feb  2 2017, 18:29:39)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

在 `>>>`之后输入 `print("hello, world")` 并按下回车。从这一刻开始，你已经是程序员了，标志就是你已经用代码向这个世界打招呼了w～每个程序员，都曾经经历过这样的时刻。

但是，各位有没有觉得，刚刚打印 "hello, world" 的 shell 或者 CMD 太简陋了？难道那些旷世代码就是用这种东西写出来的吗？当然不是，程序员肯定会为自己打造完美好用的工具。IDE 就是工具之一。

Integrated Development Environment 简称 IDE，具体的就引用维基百科了[^fn3]：

> 集成开发环境（Integrated Development Environment，简称IDE，也称为Integration Design Environment、Integration Debugging Environment）是一种辅助程序开发人员开发软件的应用软件，在开发工具内部就可以辅助编写源代码文本、并编译打包成为可用的程序，有些甚至可以设计图形界面。
> IDE通常包括编程语言编辑器、自动构建工具、通常还包括调试器。有些IDE包含编译器／解释器，如微软的Microsoft Visual Studio，有些则不包含，如Eclipse、SharpDevelop等，这些IDE是通过调用第三方编译器来实现代码的编译工作的。有时IDE还会包含版本控制系统和一些可以设计图形用户界面的工具。许多支持面向对象的现代化IDE还包括了类别浏览器、物件检视器、物件结构图。虽然目前有一些IDE支持多种编程语言（例如Eclipse、NetBeans、Microsoft Visual Studio），但是一般而言，IDE主要还是针对特定的编程语言而量身打造（例如Visual Basic）。

[^fn3]: [https://zh.wikipedia.org/zh-cn/集成开发环境](https://zh.wikipedia.org/zh-cn/集成开发环境)

对于 Python 来说，最简单的一个 IDE 就是 IDLE，安装 Python 之后，应用软件中直接打开或者从 Terminal 输入 idle 都能打开它。PyCharm ([https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/))，jupyter notebook ([http://jupyter.readthedocs.io/en/latest/index.html](http://jupyter.readthedocs.io/en/latest/index.html)), Emacs，Atom，Vim，Sublime Text 等也是使用人数众多的 Python IDE。只需要Google 一下 `Python IDE` 然后选一个自己喜欢的吧。这里主要说一下怎么安装 jupyter notebook。其实非常简单，打开 Terminal 或者 CMD 输入：

```zsh
pip3 install ipython jupyter
```

还有这几个推荐的 IDE 的简单对比：

* **Atom**：需要稍微折腾下，完全免费，很炫酷。插件众多，主题众多，什么风格都有。除了写 Python，还可以写其他的东西：C，Matlab，R，JavaScript ... 
* **PyCharm**：不需要折腾，社区版本免费，各种插件也丰富。
* **Spyder**：如果你熟悉 R studio，这个是一个非常不错的选择（虽然 Atom 通过 Hydrogen 也能达到类似的效果，甚至比它还要方便）。
* **jupyter notebook**：原来是 iPython notebook，最重要的一个功能是，可以直接把代码以及运行结果一起保留下来，就像是记事本一样，非常好用。

## 准备

### help

使用 Python 时，任何不清楚怎么做的时候，记得 `help`。

```Python
>>> help(help)
```

> **Help on _Helper in module _sitebuiltins object:**
> 
> class **_Helper**(builtins.object)
>  >  Define the builtin 'help'.
>  >
>  >  This is a wrapper around pydoc.help that provides a helpful message
>  >  when 'help' is typed at the Python interactive prompt.
>  >
>  >  Calling help() at the Python prompt starts an interactive help session.
>  >  Calling help(thing) prints help for the python object 'thing'.



### 数与初等算术

> **The different branches of Arithmetic -- Ambition, Distraction, Uglification, and Derision.**
> *-- Alice in Wonderland*
> &ensp;
> ps：我也不知道为什么要用这句

谈到计算机，普遍都会想到她是用来计算的机器吧，加减乘除幂，速度飞快。既然是从零开始的，就先说一说这个吧。

首先，打开 Python，再来问候一下世界：

```Python
>>> print("hello, world")
hello, world
```

在 Python 中，基本的数学运算符号是这样的：加`+`，减`-`，乘`*`，除`/`，幂`**`，带余除法的商`//`，带余除法的余数`%`。

来做点测试，看看 Python 与用人脑算的结果是否相等：

```Python
>>> 2 + 3
5
>>> 7 - 5
2
>>> 3 * 1
3
>>> 6 / 2
3.0
>>> 6 / 3 * 2 - 4 + 2 ** 4
16.0
>>> 2 * (5 // 2) + 5 % 2
5
>>> 2 ** 0.5
1.4142135623730951
```

上面把基本的运算都涉及到了，接下来，再来一些：

```Python
>>> 2.1 + 4.2
6.300000000000001
>>> 2.1 + 4.2 == 6.3
False
>>> 6.3 == 6.3
>>> 2 ** 1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
```

啊哈，发现了没？一方面 `2.1 + 4.3 ≠ 6.3` 呢，另一方面，却可以很轻松的计算 $2^{1000} $ 。

现在要引入三个数的类型，整数 `int` ，浮点数 `float`，布尔 `bool`。整数不用说了，浮点数的定义呢，照抄维基[^fn4]：

> 在计算机科学中，浮点（英语：floating point，缩写为FP）是一种对于实数的近似值数值表现法，由一个有效数字（即尾数）加上幂数来表示，通常是乘以某个基数的整数次指数得到。以这种表示法表示的数值，称为浮点数（floating-point number）。在计算机上，通常使用2为基数的幂数来表示。利用浮点进行运算，称为浮点计算，这种运算通常伴随着因为无法精确表示而进行的近似或舍入。

许多语言（包括 Python）会把浮点数舍入到 17 位有效数字。

至于整数，很多语言整数都是有精度的，长整型之类的，在 Python 中不用管这个，只要是整数，它就只是整数，而且无论整数有多大，在 Python 中总是精确的。

布尔数，简单点说就是 `1: True`，`0: False`，用 `bool(xxx)` 判断 `xxx`。

可以用一个简单的函数 `type(Object)` 来检测一个数是什么类型：

```Python
>>> type(2.1 + 4.2)
<class 'float'>
```
```Python
>>> type(2 ** 1000)
<class 'int'>
```
```Python
>>> type(2 ** 0.5)
<class 'float'>
```
```Python
>>> type(True)
<class 'bool'>
```

[^fn4]: [https://zh.wikipedia.org/zh-cn/浮点数](https://zh.wikipedia.org/zh-cn/浮点数)

### 模块

Python 会收到欢迎，有一个很重要的原因，就是模块（也可以用别的语言的名字，叫做"库"）特别多，成千上万。有 Python 自带的，也有别人做好的，我们要做的就是：拿来，用。

怎么用呢？有两种方式：

* `import module_name as name` | `import` 后面跟着模块名，`as` 这里是重新命名一下你导入的模块，没有也没关系
* `from module_name import module as name` | 基本和前一个一样，一般应用于一个模块里面还有很多其他模块的时候

不多说了，实验一下，我们要更精确的浮点数，使用标准模块 `decimal` 就行，对于这个模块更详细的介绍会在后面的标准库介绍里面。

```Python
>>> from decimal import Decimal as dec
>>> dec('2.1') + dec('4.2')
Decimal('6.3')
>>> 2 ** dec('0.5')
Decimal('1.414213562373095048801688724')
```

`decimal` 模块可以带来更加精确的浮点计算，支持所有常用的数学运算，唯一的缺点就是性能下降。大多数情况下普通的浮点数就够了。遇到数据库之类的那种精确度太高的情况下才会去使用它，比如下面这种情况：

```Python
>>> 3.21 * 10 ** 18 + 1 - 3.21 * 10 ** 18
0.0  # 1 是怎么消失的w~
>>> dec("3.21") * 10 ** 18 + 1 - dec("3.21") * 10 ** 18
Decimal('1.00')
```

### 其他运算

啊，还有三角函数啊，对数啊这些还没说。这些东西大都存在于一个标准库 `math` 里面（虽然更多的时候，可能用的是另外的库来做这些运算～）

```Python
>>> from math import pi, exp, sin, cos, e, log, log10  # 还有更多的
>>> pi
3.141592653589793
>>> exp(1)
2.718281828459045
>>> e
2.718281828459045
>>> sin(pi/2)
1.0
>>> cos(pi)
-1.0
>>> log(e)
1.0
>>> log10(10)
1.0
```

还有位运算 `<<`，`>>`，`^` ，这些就不作说明了（反正基本没机会用到

### 有序数据：列表 `list` 与 元组 `tuple`

Python 没有其他语言的数组，用来表示有序数据的数据类型有两种，就是 `list` 和 `tuple`。

#### 创建 `list`

在 Python 中用方括号 `[]` 表示 `list`，方括号里面可以是任何东西，`int`，`float`，`bool` 还是其他的什么都无所谓，先来看看是怎么创建的：

```Python
>>> lst = []  # 定义了一个空 list lst.
>>> type(lst)
<class 'list'>
>>> bool(lst)  # 空的东西的布尔值都是 `False`
False
>>> lst = [1, 0.3, True]  # 重新定义一个"实" list lst
>>> len(lst)  # 得到 list 的长度
0
>>> lst
[1, 0.3, True]
>>> len(lst)
3
```

#### `list` 索引 与 切片

在 Python 中，有序数据中的每一个元素都具有表示次序的编号，编号是从0开始的，不允许索引超过编号的元素，可以切片。个人觉得，切片的方式是 Python 的一大特色，可以用简单的切片方式，搞定其他语言需要写好多代码才能解决的事情。

先来看看索引，直接使用 `[i]`，索引返回的是一个元素。得到索引使用 `list.index(x)`。

代码示例：

```Python
>>> lst[0]
1
>>> lst[1]
0.3
>>> lst[-1]  # 索引时，可以是负数，表示从尾到头
True
>>> lst[-2]
0.3
>>> lst.index(1)  # 得到的是第一个元素值为1的索引
```

然后是切片，和索引不同，切片返回的是一个新的 `list`。

一个完整的切片表达式是这样的：

```Python
lst[start:end:step]
```

`step` 默认是1，可以省略。切片的时候，第一个 `:` 不可省略。

切片代码示例：

```Python
>>> num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> num_lst[:]  # 截取整个list
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> num_lst[:5]  # 截取前5个
[1, 2, 3, 4, 5]
>>> num_lst[-4:]  # 截取后4个
[7, 8, 9, 10]
>>> num_lst[2:6]  # 截取第三个到第6个
[3, 4, 5, 6]
>>> num_lst[-6:-2]  # 截取倒数第6个到倒数第三个
[5, 6, 7, 8]
>>> num_lst[-2:-6:-1]  # 截取倒数第二个到倒数第五个
[9, 8, 7, 6]
>>> num_lst[::2]  # 截取编号为偶数的
[1, 3, 5, 7, 9]
>>> num_lst[1::2]  # 截取编号为奇数的
[2, 4, 6, 8, 10]
>>> num_lst[::3] # 截取编号为0, 3, 6, 9的
[1, 4, 7, 10]
>>> num_lst[::-1]  # 截取倒数第一个到第一个（反转整个 list）
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

#### 对 `list` 的操作

对 `list` 操作，包括添加元素，合并两个 `list`，删除元素，反转和排序。操作是在原始 `list` 上产生的，而非生成一个新的 `list`。

**添加**元素最常用的是 `list.append(x)`，用来在原始 `list` 最后添加一个元素。其次是 `list.insert(i, x)` ，官方文档：

> list.insert(i, x)
>	> Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

**合并** `list`，一般使用的是 `list.extend(L)`，有些时候可能会见得到这样合并两个 `list` 的方式：

```Python
list3 = list1 + list2
```

啊，这样合并 `list` 得到的是一个新的 `list` 而非在原始的 `list` 上操作（而且我不是很推荐这样做，很多库使用类似 `list` 的数据结构时，这样做都是两个 `list` 里面的元素互相相加。）

**删除** `list` 的元素一般用 `list.pop([i])` 删除 `list` 的编号为 `i` 的元素。这里的 `[i]` 表示的是 `i` 是可以省略的，默认的 `i` 是最后一位。另外一种方式是，当你知道 `list` 元素时，可以使用 `list.remove(x)` 删除第一个 `x` 元素。

**反转** `list` 使用 `list.reverse()`

**排序** `list` 使用 `list.sort()`，默认是从小到大，如果要从大到小可以 `list.sort(reverse=True)`

**更改 `list` 元素** 只需要索引到元素，可以使用切片的方式索引多个元素，再重新赋值就行。

代码示例：

```Python
>>> lst = [1,2,3,4,5]
>>> lst.append(6)
>>> lst
[1, 2, 3, 4, 5, 6]
>>> lst.insert(0,7)
>>> lst
[7, 1, 2, 3, 4, 5, 6]
>>> lst.sort()
>>> lst
[1, 2, 3, 4, 5, 6, 7]
>>> lst.extend(lst)
>>> lst
[1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]
>>> lst.append([1, 2, 3])
>>> lst
[1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, [1, 2, 3]]
>>> lst.pop()
[1, 2, 3]
>>> lst
[1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]
>>> lst.remove(3)
>>> lst
[1, 2, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]
>>> lst.sort(reverse=True)
>>> lst
[7, 7, 6, 6, 5, 5, 4, 4, 3, 2, 2, 1, 1]
>>> lst.reverse()
>>> lst
[1, 1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7]
# 更改
>>> lst[0] = 0
>>> lst
[0, 1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7]
>>> lst[0:5:2] = [10, 10, 10]
>>> lst
[10, 1, 10, 2, 10, 4, 4, 5, 5, 6, 6, 7, 7]
```

#### 不可更改的 `list` -- 元组 `tuple`

`[]` 创建的是 `list`，`()` 创建的就是 `tuple`，需要注意的是，如果生成的 tuple 中只有一个元素，需要在后面加一个 ','。

代码示例：

```Python
>>> tpl = (1, 2, True, [1, 2, 3], [], (1, 2))
>>> tpl
(1, 2, True, [1, 2, 3], [], (1, 2))
>>> tpl2 = (1)  # 此时()表示的是运算优先度，而不是生成元组
>>> tpl2
1
>>> tpl3 = (1,)
>>> tpl3
(1,)
```

`tuple` 的索引与切片与 `list` 没有什么区别，但 `tuple` 是不能更改的，也就是说，之前的 `list` 的一切操作，合并啊，添加啊，删除啊什么的，对 `tuple` 来说，都是不存在的。当然，组合两个 `tuple` 可以使用：

```Python
tuple3 = tuple1 + tuple2
```

因为，这是生存一个新的 `tuple`。

那 `tuple` 用在什么地方呢？`list` 与 `tuple` 都可以用来表示有序数据，但是 `list` 可以更改，有些时候，这个更改可能会坏事，这时使用 `tuple` 的话，可以避免这种情况导致的 bug。

#### `list` 与 `tuple` 互相转换

`list` 与 `tuple` 互相转换非常简单：

```Python
list(tuple)  # tuple to list
tuple(list)  # list to tuple
```

实际上，`list()` 是一个用来创建 `list` 的东西，括号内如果什么都不填，就相当于 `[]`，同样 `tuple` 也是这样的。

#### 注意⚠️

使用 `list` 以及 `tuple` 的时候，有一些地方需要注意，比如当你想得到一个 `list` 的拷贝时，不能简单的直接用 `b = a` 这样的形式，这样得到的新 `list` 和老的其实是同一个东西，新的改变了，老的也会变。有两种简单的办法可以得到新的拷贝，一种是 `list.copy()`，一种是 `list[:]`。

代码示例：

```Python
# 正确的拷贝方式
>>> a = [0, 5, 1, 7]
>>> b = a[:]
>>> c = a.copy()  # b 和 c 都是 a 的拷贝，与 a 只是数值上相等
>>> a
[0, 5, 1, 7]
>>> b
[0, 5, 1, 7]
>>> c
[0, 5, 1, 7]
>>> id(a)  # 用 id(...) 查看是否是同一个东西
4386077576
>>> id(b)
4382838536
>>> id(c)
4386036680
# 错误的拷贝方式
>>> a = [3, 1, 5, 4]
>>> a
[3, 1, 5, 4]
>>> b = a  # 此时得到的 b 和 a 是同一个东西
>>> b
[3, 1, 5, 4]
>>> b[0] = 0  # 因为是同一个东西，b 更改时，a 也会一起更改
>>> b
[0, 1, 5, 4]
>>> a
[0, 1, 5, 4]
>>> id(a)
4386036680
>>> id(b)
4386036680
```

### 键 `key` 与 值 `value`

在 Python 中，另外一种使用的比较多的数据类型，就是由 `key` 和 `value` 组成的 字典 `dict` 以及 只有 `key` 的 集合 `set`。不管是字典还是集合，`key` 都是唯一，不可有重复的。

#### 创建 `dict`

创建 `dict` 有两种方法，一种是，使用大括号，另外一种是使用 `dict()`。

代码示例

```Python
# 使用大括号
# {key: value}
>>> dct = {0: 1, 1: 2, 3: [1,2,3]}
>>> dct
{0: 1, 1: 2, 3: [1, 2, 3]}  # value 可以是任何东西，key 只能是数字，字符串这种可以"hash"的
# 使用 dict()
#  1. dict(key=value)  # 这种形式 key 不能是数字，只能使用字符串，但字符串不需要引号
#  2. dict([(key, value)])  # key 只能是数字，字符串这种可以"hash"的
>>> dct2 = dict(key1=123, key2=234)
>>> dct2
{'key1': 123, 'key2': 234}
>>> dct3 = dict([("key3", 345), ("key4", 456), (0, 4567)])
>>> dct3
{'key3': 345, 'key4': 456, 0: 4567}
```

#### `dict` 索引 与 简单操作

`dict` 的索引方式与 `list` 基本一样，只是 `[]` 中不再是编号，而是 `key`。

代码示例

```Python
>>> dct[3]
[1, 2, 3]
>>> dct2["key1"]
123
>>> dct3[0]
4567
>>> dct3["0"]  # 存在 0 这个 key，但是不存在 "0" 这个 key
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: '0'
>>> dct3.keys()  # 可以通过 dict.keys() 得到一个 dict 所有的 key
dict_keys(['key3', 'key4', 0])
>>> dct3.values()  # 可以通过 dict.values() 得到一个 dict 所有的 values
dict_values([345, 456, 4567])
```

#### 集合 `set`

`set` 与数学意义上的 集合 基本是相同的，可以做交集，并集之类的。它的元素是 `key`，是无序，不重复的。（自己用的不怎么多，但有些情况还是很有用的）

来看看可以做些什么：

```Python
>>> set1 = {1, 2, 3, 4, "Nasy"}  # 创建 set
>>> set2 = {3, 4, 5, 6, "nasy"}
>>> set1 & set2  # 交集
{3, 4}
>>> set1 | set2  # 并集
{1, 2, 3, 4, 5, 6, 'nasy', 'Nasy'}
>>> set1 - set2  # 差集
{1, 2, 'Nasy'}
>>> set1 ^ set2  # 对称差集
{1, 2, 5, 6, 'nasy', 'Nasy'}
>>> "Nasy" in set1  # "Nasy" 在 set1 中？
True
```

还有一些判断子集之类的操作，`help(set)` 看看就行了（真的不是很用得到）

#### `list`，`dict` 与 `set`

`dict` 与 `list` 相比，最主要的一点就是，`dict` 多了一个 `key`，有了这个 `key` 我们可以更快的得到我们想要的数据。比如说，某一组数据，有0-99999999，100000000个，当我们要找98707000的时候，对于 `list`，使用 `98707000 in list`，对于 `dict`，使用 `98707000 in dict`。看上去似乎没什么区别，其实速度区别非常大。`list` 要得到第98707001个数据，需要从第一个数据开始数，一个一个的，而 `dict` 只需要数一个，索引是98707000的那个就行。

速度比较代码示例

```Python
# 导入 time 模块
>>> import time
# 生成 list 和 dict
>>> lst = list(range(100000000))
>>> dct = {k: v for k, v in zip(range(100000000), range(100000000))}
# 一个比较速度的函数
>>> def speed_test():
...     """Speed test function."""
...     t1 = time.time()  # 得到当前时间
...     98707000 in lst
...     print(time.time() - t1)  # 得到 list 的时间
...     t2 = time.time()
...     98707000 in dct
...     print(time.time() - t2)  # 得到 dict 的时间

>>> speed_test()  # 运行
1.4860880374908447  # list
2.1457672119140625e-06  # dict
```

可以看到速度区别有多大！但 `list` 依然存在，最主要的原因就是，`dict` 的大小太大了，比如刚刚的那两个，对比一下大小：

```Python
>>> import sys
>>> sys.getsizeof(lst)
900000112
>>> sys.getsizeof(dct)
5368709216
```

对于 `set` 来说，单独使用没什么意义，更多的时候是把他用来和 `list` 做一些东西。比如 `list` 去重，`list` 之间做交集之类的。这里就说一下去重：

```Python
>>> lst = [1, 2, 3, 3, 4, 7]
>>> list(set(lst))  # 使用 set 的不能有重复 `key` 的特性，把 list 转为 set 再转回来就行。唯一的缺点就是 list 顺序会打乱。
[1, 2, 3, 4, 7]
```

### 字符串 `string`

啊，不要问我为什么字符串放到这儿，Python 的字符串，简单也简单，复杂也复杂。诸君都知道，字符串就是双引号，单引号之类括起来的东西。`"string"` 这样子的。

就说最常用的一点操作吧。

```Python
>>> str = "I love Nasy Bot!"  # 'I love Nasy Bot!' 也是一样的。
>>> str2 = "'\\n' is a line \n breaker."  # 输出 \ 前面需要再来一个 \
>>> print(str2)
'\n' is a line
 breaker.
>>> str3 = "\t".join(["\\t", "is", "a", "tab"])  # 使用 `.join()` 可以把 join 前的字符串插入 join 里面。
>>> print(str3)
\t	is	a	tab
>>> str4 = "12,34,56,78"
>>> lst4 = str4.split(",")  # 将 str4 使用 "," 分割成 list。（处理数据特别常用呢！）
>>> lst4
['12', '34', '56', '78']
>>> str5 = str4.replace(",", "\n")  # 将 str4 的 "," 替换为 换行符
>>> print(str5)
12
34
56
78
```

### 其他

那么，准备就到此结束了，接下来，将开始真正的编程w

## 开始

在之前的准备中，我们都是在交互模式下使用的 `Python`，从现在开始，我们将不止在交互模式下继续 `Python`，还要写完整的 `py` 文件。

Python 的一切都是要符合 [PEP](https://www.python.org/dev/peps/) 规范的。那么真正的编程开始了。


### 条件语句 和 条件表达式

啊，这个没多少好说的。Python 中的条件语句结构是 `if-elif-else` ，把原来C语言中的 `else if 改为 elif` 嗯，写起来更简单了。而条件表达式，则对应着 C语言中的 `a?b:c` 。就这样吧：

```python
# 每个完整的条件语句之后应该空一行
# 完整的情况
if condition_1:
	print("condition_1 is True")
elif condition_2:
	print("condition_2 is True")
else:
	print("...")	
	
# 不存在 else 的情况
# 通常每个语句应该独占一行
if condition:
	print("ヽ(。_°)ノ")

# 只有不存在 else，以及只执行一个动作的时候，允许下面这样写。
if condition: print("ヽ(。_°)ノ")

# a?b:c 结构的条件表达式
b if a else c

```

### 循环语句

Python 的循环，非常简单方便，除了常见的 `while, for` 都能使用外，还有一些语法糖。


* 每个完整的循环语句之后应该空一行。
* 跳出循环使用 `break`，继续循环使用 `continue`，以及占位用的 `pass`
* 循环 `list` 直接使用 `for i in list`，循环 `dict` 使用 `for key, value in dict.items()`
* 如果需要知道循环的 `index`，使用 `for index, ele in enumerate(Object)`。注意，从 0 开始计算index

```python
"""循环语句."""
# while ... else ... 循环。else 在 while 那里为 False 的时候执行
# 需要无限循环的时候，使用 while 1: 就行
# while 1 所需要的时间比 while True 要短。
i = 0
while i < 5:
	print(i)
	i += i
else:
	print(i + 1)	

# 运行结果:
# 0
# 1
# 2
# 3
# 4
# 6

# for ... else ... 循环
# 这是使用的最多的循环了。
# 循环5次，不输出第二次的结果，并在第4次的时候停止
for i in range(5):  # range(5) 得到的是 (0, 1, 2, 3, 4)
	if i == 1:
		continue
	 elif i == 3:
		break
	
	print(i)
else:
	pass

# 运行结果
# 0
# 2

# 循环 list 与 dict
for i in [1, 2, 3, 4]:
	print(i)

for key, value in {1:2, 2:3, 3:4}.items():
	print(key, value)

# 结果
# 1
# 2
# 3
# 4
# 1 2
# 2 3
# 3 4

# 循环 dict 并记录 index
for i, e in enumerate({1:1, 2:2, 3:3}.items()):
	print(i, e)

# 结果
# 0 (1, 1)
# 1 (2, 2)
# 2 (3, 3)

```

### 函数

#### 函数构造

函数是 Python 中使用的最多的东西了。Python 有两种构造一个函数的方法，一种大多数情况下使用的 `def function_name(parameters)`，一种是 lambda 创建的匿名函数 `lambda args: expression` 。大部分情况下都用前一种，后一种主要用于一些突然要写点小函数的地方，比如把 `dict` 当作 `switch ... case ...` 使用的时候。

Python 不需要 `main()` 函数也能运行。函数名使用小写字母加下划线的结构，别用驼峰式。

代码示例

```Python
# 声明 def
def fibonacci(x: int) -> None:  # 这里使用的 ": int" 以及 " -> None"  并不是必须的
	"""Fibonacci series up to x."""  # 但使用的话可以让函数的运行速度更快
	a, b = 0, 1
	while a < x:
		print(b, end=" ")
		a, b = b, a + b  # python 中，交换两个数只需要 a, b = b, a 非常方便
	return a

# 使用
result = fibonacci(1000)
# 结果
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
# >>> result
# 987

# 声明 lambda
# 注意，这种写法是非常不推荐的，虽然没什么错误，但这种情况应该使用 def 而非 lambda
rectangle_area = lambda a, b: a * b
# def 版本
# def rectangle_area(a, b):
#     """Rectangle area."""
#     return a * b

# 使用
area = rectangle_area(10, 5)
# 结果
# >>> area
# 50

# 正常使用 lambda 的情况之一
def rectangle_area(wide):
	"""rectangle_area"""
	return lambda long: wide * long

# 使用
rect = rectangle_area(10)  # 一个宽为10的矩形
rect(10)  # 宽为10的情况下，长为10
rect(7)  # 宽为10的情况下，长为7

# 上面两个的返回值为 100 和 70

# 其他使用 lambda 的情况：数值计算，列表推导以及关键词排序。

```

#### 函数参数

构造一个函数的时候，如果要一个参数或者两个参数的时候，只需要直接 `def func_name(p1, p2)` ，使用的时候，`func_name(p1, p2)` 或者 `func_name(p2=xx, p1=xxx)` 就行。前一种方式只需要按照 `p1, p2` 的顺序，填上参数就行，后一种，可以不按照顺序，使用参数的关键词。

有些时候我们需要的参数可能不止一个，比如要100个之类的，这时候显然不能 `p1, p2, ... ` 这样写下去了。Python 可以构造一个可接受任意数量参数的函数。

为了让一个函数接受任意数量的参数，使用 `*`，例如：

```Python
def avg(first, *args):
	"""Average."""
	return (first + sum(args)) / (len(args) + 1)

# 使用结果
# >>> avg(1,2,3,4,5)
# 3.0

```

`args` 在函数里把它当作一个列表来使用就好。这只是可以接受任意数量的普通参数，如果使用 `**`，那就可以构造任意数量关键词参数的函数：

```Python
def disp_info(**kwgs):
	"""Display name and age."""
	for name, age in kwgs.items():
		print(name, age)

# 使用结果
# >>> disp_info(Tom=19, Benny=21, Summer=2, Sue=33, Mewing=32)
# Tom 19
# Benny 21
# Summer 2
# Sue 33
# Mewing 32

```

那么新问题来了，如果本来有一个 `list`，一个 `dict`，在遇到这种函数的时候，还要把它分解为一个一个的，非常麻烦。不过简单的方法也有，使用 `*` 和 `**` 就行，这也是 Python 的语法糖吧！

```Python
lst = [1, 2, 3, 4, 5]
info = {'Tom': 19, 'Benny': 21, 'Summer': 2, 'Sue': 33, 'Mewing': 32}
# 使用方法
# 正确
avg(*lst)
disp_info(**info)


# 会报错，不信可以试试
avg(lst)
disp_info(info)

```

#### 函数递归

先来看看，如果要实现一个 `sum(List)` 的函数，应该怎么写：

```Python
def sum(lst):
	 """Sum."""
	 result = 0
	 for i in lst:
		  result += i
	 return result
```

注意这个函数，内部引入了一个新的变量，`result`，这一点也不函数，函数就应该专门计算。于是有了下面这种函数式的写法：

```Python
def sum(lst):
	 """Sum."""
	 if len(lst):
        return lst[0] + sum(lst[1:])
	 else:
        return 0
```

啊，如果之前没有接触过函数式编程的话，这种方式是不是有种很奇怪的感觉？不过要是写过 `lisp` 的话，一定对这种方式很熟悉。这种方式虽然写起来很爽，但也有一个问题，比较占内存，当你超过一千次的时候，就会出现下面这个错误了。

```Python
RecursionError: maximum recursion depth exceeded
```

避免出现这个错误只需要加上这样的两行:

```Python
import sys
sys.setrecursionlimit(5000)  # 想要多少写多少，默认是1000
```

### 推导式

使用列表的时候，应该会出现一个问题，如何创建一个全是1或者全是0啊之类的 `list`，数量小的时候还好说，直接：

```Python
>>> lst = [1, 1, 1, 1, 1]
>>> lst2 = [0, 0, 0, 0, 0]
```

要是遇到需要创建的是100个1，1000个0的 `list` 的时候怎么办？这时候就需要用到推导式了。

最简单的推导式，使用 `* count.`

```Python
>>> [0] * 1000
[0, 0, ..., 0]  # 共 1000 个 0

# 生成一个 3x3 的单位矩阵
>>> [[1] * 3] * 3
[[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
```

稍微复杂一些的，从一个 `list/tuple, dict` 中取得需要的值：

```Python
# list/tuple
# 注意!! 这种做法得不到 tuple，也就是说，不能是 (i for i in [1, 2, 3, 4]) 这样的
[i for i in [1, 2, 3, 4]]  # 得到 [1, 2, 3, 4]
[i for i in (1, 2, 3, 4)]  # 得到 [1, 2, 3, 4]

# dict
{k: v for k, v in {"a": 1, "b": 2, "c": 3}}  # 得到 {"a": 1, "b": 2, "c": 3}

```

可能看上去似乎没什么用，因为上面这样的，使用 `list.copy() dict.copy()` 也能办到。事实上，这个推导式能做到的更多：

```Python
# 将 list 里的偶数都 *3，奇数不变
lst = [1, 2, 3, 4, 5, 6, 7]
# 想要的结果 [1, 6, 3, 12, 5, 18, 7]
result = [i * 3 if i % 2 == 0 else i for i in lst]
print(result)  # 可以看看是不是这样的

# 还可以更复杂一些
# 将 list 里面能被 2 整除的提出来，如果还能被 4 整除，那就乘以 3
lst = [1, 2, 3, 4, 5, 6, 7]
# 想要的结果 [2, 12, 6]
result = [i * 3 if i % 4 == 0 else i for i in lst if i % 2 == 0]
print(result)
```

或许，这样子的，使用一个循环也能办到，但是，如果我想要得到的一个结构很复杂的时候，推导式能做到的，就不是一个循环，两个循环可以搞定的了。比如说从什么诡异的地方得到了一个巨大的 `tuple`，为了以后读取啊，操作啊，更快速，更方便，要把它转为 `dict` 的形式。比如下面的这个，虚拟的，已经解析过一次的微信消息，需要解析成 `dict` 的形式：（可以先不看后面我的做法，自己试试看）

```Python
from types import Tuple, List, Dict, Any

# 不要问我为什么这么多括号怎么对齐，怎么不看花的，你们要知道，lisp 比这个不知道高到哪里去了，我和 lisp 啊，谈笑风生

DATA_TUPLE: Tuple[Tuple[str, Any], ...] = (
    ("type", "text"),
    ("collection", "group message"),
    ("time", "1488844812123"),
    ("title", "An Emoji"),
    ("from", (("name", "Nasy"), ("id", "nasy"))),
    ("to", (("name", "可愛いです"), ("id", "g_07"))),
    (
        "mentioned", [(("name", "C.C."), ("id", "畅酱")), (("name", "benny"),
                                                         ("id", "bey"))]),
    # 注意这里的 "\u2005" 不是一个空格
    # 这是微信@人之后的那个空出来的东西，真实的哟
    ("data", "@C.C.\u2005@benny\u2005ヽ(。_°)ノ"))

```

初一看，似乎很复杂。不过这也是已经解析过一遍，而且简化过的了，原始的数据，就一段 `xml (或者希望是 json (如果是json那就幸福很多了！))` 甚至就一段字符串，中间靠 `\t` 之类的分隔符分割。

来看看我怎么处理吧：

```Python
def parser() -> Dict[str, Any]:
    """Parsing the raw data."""
    return {
        i[0]: {j[0]: j[1]
               for j in i[1]}
        if type(i[1]) is tuple else ([{k: l
                                       for k, l in j} for j in i[1]]
                                     if type(i[1]) is list else i[1])
        for i in DATA_TUPLE
    }

# 使用

data = parser()
print(data)
# {'type': 'text', 'collection': 'group message', 'time': '1488844812123', 'title': 'An Emoji', 'from': {'name': 'Nasy', 'id': 'nasy'}, 'to': {'name': '可愛いです', 'id': 'g_07'}, 'mentioned': [{'name': 'C.C.', 'id': '畅酱'}, {'name': 'benny', 'id': 'bey'}], 'data': '@C.C.\u2005@benny\u2005ヽ(。_°)ノ'}
# 啊，看的不太清晰
import pprint  # pprint 这个包，可以让你打印到屏幕上的 list, dict 之类的更漂亮
pprint.pprint(data)
# 结果，达到目的
# {'collection': 'group message',
#  'data': '@C.C.\u2005@benny\u2005ヽ(。_°)ノ',
#  'from': {'id': 'nasy', 'name': 'Nasy'},
#  'mentioned': [{'id': '畅酱', 'name': 'C.C.'}, {'id': 'bey', 'name': 'benny'}],
#  'time': '1488844812123',
#  'title': 'An Emoji',
#  'to': {'id': 'g_07', 'name': '可愛いです'},
#  'type': 'text'}

# 输出成人能看的
for i in data.items():
	print(*i, sep=': ')
# 结果
# type: text
# collection: group message
# time: 1488844812123
# title: An Emoji
# from: {'name': 'Nasy', 'id': 'nasy'}
# to: {'name': '可愛いです', 'id': 'g_07'}
# mentioned: [{'name': 'C.C.', 'id': '畅酱'}, {'name': 'benny', 'id': 'bey'}]
# data: @C.C. @benny ヽ(。_°)ノ

```

### Python 文件

C语言的源代码文件是 `*.c, *.h`，编译后的文件， `*.exe (windows), * (other), *.so (share lib)`。`Python` 不用编译，主要的源代码文件是 `*.py` 以及特别强调是 `Python3` 的 `*.py3` 文件。还有一些 `*.cpy` 之类的，则不用太在意了。根据 PEP-394 `py` 文件里，应该以 `Shebang ( Hashbang )`开始。

一般来说，一个 `py` 至少是这样的:

* 第一行写 `Shebang`，就是 `#!/usr/bin/env python3`
* 第二行写文件的格式
* 接下来在 `""""""` 之间写这个文件的文档，可以不像我这样写的这么全，最好留下作者以及邮箱。避免出错的时候不知道找谁啊什么的
* 最后就开始写代码了

在代码中，和其他语言一样，有一个 `main` 函数，大多数情况下，我们就是运行这个。虽然在 `python` 中这不是强制的，但这样写可以避免发生很诡异的一些事情。最后那个 `__name__ == "__main__"` 就是说是，这段程序是直接运行的，不是由其他文件引用而运行的，注意，这个非常重要，主功能应该放在 `main()` 函数中。

在文件的结尾，应该留出一行空行。

将前面推导式中解析一个巨大的 `tuple` 那一部分写成一个 `temp.py` 如下：

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Life's pathetic, let's happy coding everyday ♡~ Nasy.

@author: Nasy
@date: Mar 11, 2017
@email: sy_n@me.com
@file: temp.py
@license: MIT

Copyright © 2017 by Nasy. All Rights Reserved.
"""
from typing import Tuple, List, Dict, Any
import pprint

DATA_TUPLE: Tuple[Tuple[str, Any], ...] = (
    ("type", "text"),
    ("collection", "group message"),
    ("time", "1488844812123"),
    ("title", "An Emoji"),
    ("from", (("name", "Nasy"), ("id", "nasy"))),
    ("to", (("name", "可愛いです"), ("id", "g_07"))),
    (
        "mentioned", [(("name", "C.C."), ("id", "cc")), (("name", "benny"),
                                                         ("id", "bey"))]),
    # 注意这里的 "\u2005" 不是一个空格
    # 这是微信@人之后的那个空出来的东西，真实的哟
    ("data", "@C.C.\u2005@benny\u2005ヽ(。_°)ノ"))


def parser() -> Dict[str, Any]:
    """Parsing the raw data."""
    return {
        i[0]: {j[0]: j[1]
               for j in i[1]}
        if type(i[1]) is tuple else ([{k: l
                                       for k, l in j} for j in i[1]]
                                     if type(i[1]) is list else i[1])
        for i in DATA_TUPLE
    }


def main() -> None:
    """Main function."""
    data = parser()
    pprint.pprint(data)
    print()
    for i in data.items():
        print(*i, sep=': ')


if __name__ == "__main__":
    main()

```

