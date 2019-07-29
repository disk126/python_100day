
#应用场景
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

#for-in循环
"""
如果明确的知道循环执行的次数或者要对一个容器进行迭代（后面会讲到），那么我们推荐使用for-in循环
，例如下面代码中计算1~100求和的结果（$\displaystyle \sum \limits_{n=1}^{100}n$）。
"""


#实现1-100之间的求和
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

#代码来实现1~100之间的偶数求和
"""
用for循环实现1~100之间的偶数求和

Version: 0.1
Author: 喻先明

sum=0
for i in range(2,101,2):
    sum+=i
print(sum)
"""
#也可以通过在循环中使用分支结构的方式来实现相同的功能
"""
sum=0
for i in range(1,101):
    if i%2==0:
        sum=sum+i
print(sum)
"""

import random
retun1=random.randint(1,100)
count=0
while True:
    count=count+1
    if count>3:
        print("你已经猜了%d次,强制退出循环!"%(count))
        break
    sr=int(input(">:"))
    if sr>retun1:
        print("小一点")
    elif sr<retun1:
        print("大一点")
    elif sr==retun1:
        print("猜对了!")
        break




