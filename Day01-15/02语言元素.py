# 语言元素
"""
指令和程序
计算机的硬件系统通常由五大部件构成，包括：运算器、控制器、存储器、输入设备和输出设备。其中，
运算器和控制器放在一起就是我们通常所说的中央处理器，它的功能是执行各种运算和控制指令以及处
理计算机软件中的数据。我们通常所说的程序实际上就是指令的集合，我们程序就是将一系列的指令按照
某种方式组织到一起，然后通过这些指令去控制计算机做我们想让它做的事情。今天我们大多数时候使用
的计算机，虽然它们的元器件做工越来越精密，处理能力越来越强大，但究其本质来说仍然属于“冯·诺依曼结构”
的计算机。“冯·诺依曼结构”有两个关键点，一是指出要将存储设备与中央处理器分开，二是提出了将数据以二进
制方式编码。二进制是一种“逢二进一”的计数法，跟我们人类使用的“逢十进一”的计数法没有实质性的区别，人
类因为有十根手指所以使用了十进制（因为在数数时十根手指用完之后就只能进位了，当然凡事都有例外，玛雅
人可能是因为长年光着脚的原因把脚趾头也算上了，于是他们使用了二十进制的计数法，在这种计数法的指导下
玛雅人的历法就与我们平常使用的历法不一样，而按照玛雅人的历法，2012年是上一个所谓的“太阳纪”的最后一年，
而2013年则是新的“太阳纪”的开始，后来这件事情被以讹传讹的方式误传为”2012年是玛雅人预言的世界末日“这种
荒诞的说法，今天我们可以大胆的猜测，玛雅文明之所以发展缓慢估计也与使用了二十进制有关）。对于计算机来说，
二进制在物理器件上来说是最容易实现的（高电压表示1，低电压表示0），于是在“冯·诺依曼结构”的计算机都使用了
二进制。虽然我们并不需要每个程序员都能够使用二进制的思维方式来工作，但是了解二进制以及它与我们生活中的十
进制之间的转换关系，以及二进制与八进制和十六进制的转换关系还是有必要的。如果你对这一点不熟悉，
可以自行使用维基百科或者百度百科科普一下。

提示：近期关于量子计算机的研究已经被推倒了风口浪尖，量子计算机基于量子力学进行运算，使用量子瞬移的方式来传递信息。
2018年6月，Intel宣布开发出新款量子芯片并通过了在接近绝对零度环境下的测试；2019年1月，IBM向全世界发布了首款商业化量子计算机。
"""

# 变量和类型

"""
在程序设计中，变量是一种存储数据的载体。计算机中的变量是实际存在的数据或者说是存储器中存储数据的一块内存空间，
变量的值可以被读取和修改，这是所有计算和控制的基础。计算机能处理的数据有很多种类型，除了数值之外还可以处理文本、
图形、音频、视频等各种各样的数据，那么不同的数据就需要定义不同的存储类型。Python中的数据类型很多，而且也允许
我们自定义新的数据类型（这一点在后面会讲到），我们先介绍几种常用的数据类型。

整型：Python中可以处理任意大小的整数（Python 2.x中有int和long两种类型的整数，但这种区分对Python来说意义不大，
因此在Python 3.x中整数只有int这一种了），而且支持二进制（如0b100，换算成十进制是4）、八进制（如0o100，换算成十进制是64）
、十进制（100）和十六进制（0x100，换算成十进制是256）的表示法。


浮点型：浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，浮点数除了数学写法
（如123.456）之外还支持科学计数法（如1.23456e2）。


字符串型：字符串是以单引号或双引号括起来的任意文本，比如'hello'和"hello",字符串还有原始字符串表示法、字节字符串表示法、
Unicode字符串表示法，而且可以书写成多行的形式（用三个单引号或三个双引号开头，三个单引号或三个双引号结尾）。


布尔型：布尔值只有True、False两种值，要么是True，要么是False，在Python中，可以直接用True、False表示布尔值（请注意大小写），
也可以通过布尔运算计算出来（例如3 < 5会产生布尔值True，而2 == 1会产生布尔值False）。


复数型：形如3+5j，跟数学上的复数表示一样，唯一不同的是虚部的i换成了j。
"""

# 变量命名
"""
对于每个变量我们需要给它取一个名字，就如同我们每个人都有属于自己的响亮的名字一样。在Python中，
变量命名需要遵循以下这些必须遵守硬性规则和强烈建议遵守的非硬性规则。

硬性规则：
变量名由字母（广义的Unicode字符，不包括特殊字符）、数字和下划线构成，数字不能开头。
大小写敏感（大写的a和小写的A是两个不同的变量）。
不要跟关键字（有特殊含义的单词，后面会讲到）和系统保留字（如函数、模块等的名字）冲突。


PEP 8要求：
用小写字母拼写，多个单词用下划线连接。
受保护的实例属性用单个下划线开头（后面会讲到）。
私有的实例属性用两个下划线开头（后面会讲到）。

当然，作为一个专业的程序员，给变量（事实上应该是所有的标识符）命名时做到见名知意也是非常重要的。
"""

# 变量的使用

# 下面通过几个例子来说明变量的类型和变量使用。
"""
使用变量保存数据并进行算术运算

Version: 0.1
Author: 喻先明
"""
"""
a = 321
b = 123
print(a + b)
print(a - b)
print(a / b)
print(a * b)
print(a // b)  # 整除法，取整数部分，余数舍掉
print(a % b)  # 计算除法的余数
print(a ** b)  # a的b次方
"""

# input()函数的使用
"""
使用input()函数获取键盘输入
使用int()进行类型转换
用占位符格式化输出的字符串

Version: 0.1
Author: 喻先明
"""
a=int(input("a="))
b=int(input("b="))
print("%d+%d=%d"%(a,b,a+b))
