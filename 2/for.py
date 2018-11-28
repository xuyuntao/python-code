# for 语句
# 格式 ： for 变量名 in 集合:
#            语句
"""
for i in [1,2,3,4,5]:
    print(i)
# range()函数，列表生成器

for i in range(10):
    print(i)
for i in range(2,20,2):
    print(i)

#    同时遍历下标和元素
for index, m in  enumerate([1,2,3,4,5,[6,7]]):
    print(index, m)

# break语句： 跳出循环，只能跳出距离该语句最近的一层循环
for i in range(10):
    print(i)
    if i == 5:
        break
i = 1
while i <= 10:
    print(i)
    if i ==5:
        break
    i += 1

# continue语句 跳过当前循环中的剩余语句，然后继续下一次循环
for i in range(10):
    print(i)
    if i == 3:
        continue
    print("*")
    print("&")
"""
"""
i = 1
while i < 10:
    print(i)
    if i == 3:
        i += 1
        continue
    print("*")
    print("&")
    i += 1
"""
# 打印99乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d * %d = %d " % (j, i, i*j))

# 输入两个数，求这两个数的最大公约数

# 输入一个字符串，将字符串中的大写字母转小写，小写转大写
