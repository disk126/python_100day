
#应用场景
"""
迄今为止，我们写的Python代码都是一条一条语句顺序执行，这种代码结构通常称之为顺序结构。
然而仅有顺序结构并不能解决所有的问题，比如我们设计一个游戏，游戏第一关的通关条件是玩家
获得1000分，那么在完成本局游戏后，我们要根据玩家得到分数来决定究竟是进入第二关，还是
告诉玩家“Game Over”，这里就会产生两个分支，而且这两个分支只有一个会被执行。类似的场
景还有很多，我们将这种结构称之为“分支结构”或“选择结构”。给大家一分钟的时间，你应该可
以想到至少5个以上这样的例子，赶紧试一试。
"""

#if语句的使用
"""
在Python中，要构造分支结构可以使用if、elif和else关键字。所谓关键字就是有特殊含义的
单词，像if和else就是专门用于构造分支结构的关键字，很显然你不能够使用它作为变量名（事
实上，用作其他的标识符也是不可以）。下面的例子中演示了如何构造一个分支结构。
"""

"""
用户身份验证

Version: 0.1
Author: 喻先明

username=input("请输入用户名>:")
password=input("请输入密码>:")
if username=="admin" and password=="123456":
    print("身份验证成功!")
else:
    print("身份验证失败!")

输出结果：
请输入用户名>:admin
请输入密码>:123456
身份验证成功!      
"""

#分段函数求值
"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

Version: 0.1
Author: 喻先明


x =float(input("请输入X的值>:"))
if x>1:
    y=3*x-5
elif x>=-1:
    y=x+2
else:
    y=5*x+3
print("x的值是:%.2f,y的值是:%.2f"%(x,y))
print("x的值是:{},y的值是:{}".format(x,y))

"""

"""
当然根据实际开发的需要，分支结构是可以嵌套的，例如判断是否通关以后还要根据你获得的宝物或者道
具的数量对你的表现给出等级（比如点亮两颗或三颗星星），那么我们就需要在if的内部构造出一个新的
分支结构，同理elif和else中也可以再构造新的分支，我们称之为嵌套的分支结构，也就是说上面的代
码也可以写成下面的样子。

x =float(input("请输入X的值>:"))
if x>1:
    y=3*x-5
else:
    if x>=-1:
        y=x+2
    else:
        y=5*x+3
print("x的值是:%.2f,y的值是:%.2f"%(x,y))
print("x的值是:{},y的值是:{}".format(x,y))

说明： 大家可以自己感受一下这两种写法到底是哪一种更好。在之前我们提到的Python之禅中有这么一句
话“Flat is better than nested.”，之所以提倡代码“扁平化”是因为嵌套结构的嵌套层次多了之后会
严重的影响代码的可读性，所以能使用扁平化的结构时就不要使用嵌套。
"""

#练习题

#练习1：英制单位与公制单位互换
"""
英制单位英寸和公制单位厘米互换

Version: 0.1
Author: 喻先明

#1千米(km)=0.6213712英里(mi)

length_put=float(input("长度>:"))
unit_put=input("单位>:")

if unit_put=="km" or unit_put=="千米":
    print("%.2f千米=%.2f英里"%(length_put,length_put*0.6213712))
elif unit_put=="mi" or unit_put=="英里":
    print("%.2f英里=%.2f千米"%(length_put,length_put/0.6213712))
else:
    print("请输入正确单位!")
"""


#练习2：掷骰子决定做什么
"""
掷骰子决定做什么事情

Version: 0.1
Author: 喻先明


from random import randint

face= randint(1,6)
if face==1:
    result="唱歌"
elif face==2:
    result="跳舞"
elif face==3:
    result="学狗叫"
elif face==4:
    result="做俯卧撑"
elif face==5:
    result="绕口令"
else:
    result="冷笑话"
print(result)

说明： 上面的代码中使用了random模块的randint函数生成指定范围的随机数来模拟掷骰子。
"""


#练习3：百分制成绩转等级制
"""
百分制成绩转等级制成绩
90分以上    --> A
80分~89分    --> B
70分~79分	   --> C
60分~69分    --> D
60分以下    --> E

Version: 0.1
Author: 喻先明


grade=float(input("输入分数>:"))
if grade>=90:
    result="A"
elif grade>=80 and grade<=89:
    result="B"
elif grade>=70 and grade<=79:
    result="C"
elif grade>=60 and grade<=69:
    result="D"
else:
    result="E"
print(result)


"""

#练习4：输入三条边长如果能构成三角形就计算周长和面积
"""
判断输入的边长能否构成三角形
两边之和大于第三边，分别要ABC组合验证。
两边之和要小于第三，边也要分别组合验证
如果能则计算出三角形的周长和面积

三角形面积：p=(a+b+c)/2 #用边长计算三角形面积的公式叫做海伦公式
三角形周长: e=a+b+c

Version: 0.1
Author: 喻先明

a=float(input("输入a>:"))
b=float(input("输入b>:"))
c=float(input("输入c>:"))

if (a+b)>c and (a+c)>b and (b+c)>a:
    perimeter=a+b+c
    area=(a+b+c)/2
    print("周长%f"%perimeter)
    print("面积%f"%area)
else:
    print("不能构成三角形!")
    
    
说明： 上面的代码中使用了math模块的sqrt函数来计算平方根。用边长计算三角形面积的公式叫做海伦公式
"""



#练习5：个人所得税计算器

"""
输入月收入和五险一金计算个人所得税

salary:工资
insurance:保险
diff:起征额

a:税率
b=扣除数

个人所得税:起征额*税率-扣除数
实际工资=工资-保险-个人所得税

Version: 0.1
Author: 喻先明
"""
salary=float(input("工资>:"))
insurance=float(input("保险>:"))
diff = salary-insurance-3500
if diff <=0:
    a=0
    b=0
elif diff<1500:
    a=0.03
    b=0
elif diff<4500:
    a=0.1
    b=105
elif diff<9000:
    a=0.2
    b=555
elif diff<35000:
    a=0.25
    b=1005
elif diff<55000:
    a=0.3
    b=2755
elif diff<80000:
    a=0.35
    b=5505
else:
    a=0.45
    b=13505

print("个人所得税>:%.2f"%(diff*a-b))
print("实际工资>:%.2f"%(salary-insurance-(diff*a-b)))

a=yuxianming
print(a)

v=xuhongmei
print(v)
