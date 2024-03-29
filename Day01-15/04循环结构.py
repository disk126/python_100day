# 应用场景
"""
如果在程序中我们需要重复的执行某条或某些指令，例如用程序控制机器人踢足球，如果机器人持球而且
还没有进入射门范围，那么我们就要一直发出让机器人向球门方向奔跑的指令。当然你可能已经注意到了
，刚才的描述中其实不仅仅有需要重复的动作，还有我们上一个章节讲到的分支结构。再举一个简单的例
子，比如在我们的程序中要实现每隔1秒中在屏幕上打印一个"hello, world"这样的字符串并持续一个
小时，我们肯定不能够将print('hello, world')这句代码写上3600遍，如果真的需要这样做，那么
编程的工作就太无聊了。因此，我们还需要了解一下循环结构，有了循环结构我们就可以轻松的控制某件
事或者某些事重复、重复、再重复的去执行。

在Python中构造循环结构有两种做法，一种是for-in循环，一种是while循环。
"""

# for-in循环
"""
如果明确的知道循环执行的次数或者要对一个容器进行迭代（后面会讲到），那么我们推荐使用for-in循环
，例如下面代码中计算1~100求和的结果（$\displaystyle \sum \limits_{n=1}^{100}n$）。
"""

# 实现1-100之间的求和
"""
用for循环实现1~100求和

Version: 0.1
Author: 喻先明

sum=0
for i in range(1,101):
    sum=sum+i
print(sum)

需要说明的是上面代码中的range类型，range可以用来产生一个不变的数值序列，而且这个序列通常都是用在循环中的，例如：

range(101)可以产生一个0到100的整数序列。
range(1, 100)可以产生一个1到99的整数序列。
range(1, 100, 2)可以产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量

"""

# 代码来实现1~100之间的偶数求和
"""
用for循环实现1~100之间的偶数求和

Version: 0.1
Author: 喻先明

sum=0
for i in range(2,101,2):
    sum+=i
print(sum)
"""
# 也可以通过在循环中使用分支结构的方式来实现相同的功能
"""
sum=0
for i in range(1,101):
    if i%2==0:
        sum=sum+i
print(sum)
"""

# while循环
"""
如果要构造不知道具体循环次数的循环结构，我们推荐使用while循环，while循环通过一个能够
产生或转换出bool值的表达式来控制循环，表达式的值为True循环继续，表达式的值为False循
环结束。下面我们通过一个“猜数字”的小游戏（计算机出一个1~100之间的随机数，人输入自己猜
的数字，计算机给出对应的提示信息，直到人猜出计算机出的数字）来看看如何使用while循环
"""

"""

猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

Version: 0.1
Author: 喻先明
Date: 2019-07-30

"""

"""
import  random
a=random.randint(1,100)
count=0
while True:
    count=count+1
    if count==4:
        print("你已经猜测%d次,智商好低呀！是否还需要继续猜数字，是Y,否N....."%(count))
        h=input("继续<Y>/结束<N>")
        if h=="Y":
            count=0
            continue
        elif h=="N":
            print("结束猜数字游戏!")
            break
    b=int(input("请输入数字>:"))
    if b>a:
        print("数字在小一点！")
    elif b<a:
        print("数字在大一点！")
    else:
        b=a
        print("数字猜对了！,非常棒.....")
        break


说明：上面的代码中使用了break关键字来提前终止循环，需要注意的是break只能终止它所在的那个循环，
这一点在使用嵌套的循环结构（下面会讲到）需要引起注意。除了break之外，还有另一个关键字是continue，
它可以用来放弃本次循环后续的代码直接让循环进入下一轮。
"""

# 练习

# 练习1：九九乘法口诀

"""
输出乘法口诀表(九九表)

Version: 0.1
Author: 喻先明
Date: 2019-07-30



for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+"x"+str(j)+"="+str(i*j),end=" ")
    print()
"""

# 练习2：输入一个数判断是不是素数

"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: 喻先明
Date: 2019-08-03

import math
a=int(input("请输入一个正整数>:"))
b=int(math.sqrt(a))
c=True
for i in range(2,b+1):
    if a%2==0:
        c=False
        break
if c ==True and a!=1:
    print("%d是一个素数"%(a))
else:
    print("%d不是一个素数"%(a))
    
"""

#练习2：输入两个正整数，计算最大公约数和最小公倍数
"""
输入两个正整数计算最大公约数和最小公倍数

Version: 0.1
Author: 喻先明
Date: 2019-08-04


x=int(input("请输入一个正整数>:"))
y=int(input("请输入一个正整数>:"))
if x>y:
    x,y=y,x
for i in range(x,0,-1):
    if x%i==0 and y%i==0:
        print("数字%d和数字%d的最大公约数是:%d"%(x,y,i))
        print("数字%d和数字%d的最小公倍数是:%d"%(x,y,x*y//i))

"""

a=int(input("请输入行数>:"))
for i in range(a):
    for i1 in range(0,i+1):
        print("*",end="")
    print("\n")