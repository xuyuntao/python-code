"""
分类:整数\浮点数\复数 整数:Python可以处理任意大小的整数
"""
print(int(1.9))
print(float(1))
print(int("123"))
print(float("12.3"))
print(int("+123"))
# print(int ("abc"))
# print(int ("123abc"))
# 最小值min(),# 绝对值abs()
print(min(1,2,3,-1))
a1 = -10
a2 = abs(a1)
print("a1 的绝对值是：", a2)
#最大值max()
print(max(a1,a2))
print(max(3,3))
# 求x的y次方 pow(x,y)
print(pow(2, 5))
# 四舍五入 round(values,float_bit)
print(round(3.1415))
print(round(3.1415,3))
# 导入库math
import math
# 向上取整math.ceil()
print(math.ceil(18.1))
print(math.ceil(18.9))
# 向下取整math.floor()
print(math.floor(18.1))
print(math.floor(18.9))
#返回整数部分与小数部分
print(math.modf(20.3))
#开方
print(math.sqrt(16))

import random
#随机数
#从序列的元素中随机原则一个，random.choice([])
print(random.choice([1,3,5,7,9]))
print(random.choice(range(20))) #range(20)==[0,1,2,3....,19]
print(random.choice("xyt")) #"xyt" == [x,y,t]
#产生一个1-100之间的随机数
r1 = random.choice(range(10)) + 1
#r2 = random.choice(range(10) + 1)
print(r1)
