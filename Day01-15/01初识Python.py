


#初识Python

"""
Python简介
Python的历史
1989年圣诞节：Guido von Rossum开始写Python语言的编译器。
1991年2月：第一个Python编译器（同时也是解释器）诞生，它是用C语言实现的（后面又出现了Java和C#实现的版本Jython和IronPython，
以及PyPy、Brython、Pyston等其他实现），可以调用C语言的库函数。在最早的版本中，Python已经提供了对“类”，“函数”，“异常处理”等
构造块的支持，同时提供了“列表”和“字典”等核心数据类型，同时支持以模块为基础来构造应用程序。

1994年1月：Python 1.0正式发布。

2000年10月16日：Python 2.0发布，增加了实现完整的垃圾回收，提供了对Unicode的支持。与此同时，Python的整个开发过程更加透明，
社区对开发进度的影响逐渐扩大，生态圈开始慢慢形成。

2008年12月3日：Python 3.0发布，它并不完全兼容之前的Python代码，不过因为目前还有不少公司在项目和运维中使用Python 2.x版本，
所以Python 3.x的很多新特性后来也被移植到Python 2.6/2.7版本中。

目前我们使用的Python 3.7.x的版本是在2018年发布的，Python的版本号分为三段，形如A.B.C。其中A表示大版本号，一般当整体重写，
或出现不向后兼容的改变时，增加A；B表示功能更新，出现新功能时增加B；C表示小的改动（例如：修复了某个Bug），只要有修改就增加C。
如果对Python的历史感兴趣，可以阅读名为《Python简史》的博文。

Python的优缺点

Python的优点很多，简单的可以总结为以下几点。

简单和明确，做一件事只有一种方法。
学习曲线低，跟其他很多语言相比，Python更容易上手。
开放源代码，拥有强大的社区和生态圈。
解释型语言，天生具有平台可移植性。
支持两种主流的编程范式（面向对象编程和函数式编程）都提供了支持。
可扩展性和可嵌入性，可以调用C/C++代码，也可以在C/C++中调用Python。
代码规范程度高，可读性强，适合有代码洁癖和强迫症的人群。


Python的缺点主要集中在以下几点。

执行效率稍低，因此计算密集型任务可以由C/C++编写。
代码无法加密，但是现在很多公司都不销售卖软件而是销售服务，这个问题会被淡化。
在开发时可以选择的框架太多（如Web框架就有100多个），有选择的地方就有错误。

Python的应用领域
目前Python在Web应用开发、云基础设施、DevOps、网络爬虫开发、数据分析挖掘、机器学习等领域都有着广泛的应用，因此也产生了Web后端开发、
数据接口开发、自动化运维、自动化测试、科学计算和可视化、数据分析、量化交易、机器人开发、图像识别和处理等一系列的职位。
"""



#代码中的注释
"""
注释是编程语言的一个重要组成部分，用于在源代码中解释代码的作用从而增强程序的可读性和可维护性，当然也可以将源代码中不需要参与运行的代码
段通过注释来去掉，这一点在调试程序的时候经常用到。注释在随源代码进入预处理器或编译时会被移除，不会在目标代码中保留也不会影响程序的执行结果。

单行注释 - 以#和空格开头的部分
多行注释 - 三个引号开头，三个引号结尾
"""

"""
第一个Python程序 - hello, world!
向伟大的Dennis M. Ritchie先生致敬

Version: 0.1
Author: 喻先明
"""

"""
print("Hello,world!")
print("你好,世界！")
print("hello,world",sep=",",end="\n") #end后面的赋值如果不是\n代表不换行，如果是\n代表换行
print("goodbye,world",end="!\n")
print("diskpart")
"""


#python之禅
"""
在python交互界面输入以下命令就可以看到Python之禅的内容了
import this
输出：
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

翻译上面的结果，对照每一行的翻译的输出
美丽总比丑陋好。
显式比隐式好。
简单总比复杂好。
复杂总比复杂好。
平的比嵌套的好。
稀疏总比密集好。
可读性。
特殊情况还不足以打破规则。
虽然实用性胜过纯洁性。
错误不应该悄无声息地过去。
除非显式地沉默。
面对模棱两可的情况，拒绝猜测的诱惑。
应该有一种——而且最好只有一种——显而易见的方法来做到这一点。
不过，除非你是荷兰人，否则这种方式一开始可能并不明显。
现在总比不做好。
虽然从来没有比“现在”更好。
如果实现很难解释，这是一个坏主意。
如果实现很容易解释，这可能是一个好主意。
名称空间是一个很棒的主意——让我们做更多这样的事情!
"""




#学习使用turtle在屏幕上绘制图形
"""
说明：turtle是Python内置的一个非常有趣的模块，特别适用于让小朋友体会什么是编程，它最早是Logo语言的一部分，
Logo语言是Wally Feurzig和Seymour Papert在1966发明的编程语言.
"""

#在python交互界面输入以下代码
import turtle    #导入turtle库
turtle.pensize(4)         #画笔的粗细
turtle.pencolor('red')    #画笔颜色
turtle.forward(100)       #向前
turtle.right(90)          #箭头的角度转向
turtle.forward(100)       #向前
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.mainloop()


