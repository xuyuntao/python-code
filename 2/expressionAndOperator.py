# 判断一个数字是否是水仙花数
""""
number1 = int(input("请输入一个三位数："))
a = number1 // 100
b = number1 // 10 % 10
c = number1 % 10
if int(number1) == a**3 + b**3 + c**3:
    print("是水仙花数")
else :
    print("不是水仙花数")

"""
# 判断一个五位数是否是回文数
"""
number2 = input("请输入一个五位数:")
d = list(number2)
if d[0] != d[4]:
    print(number2 + "不是回文数")
if d[1] == d[3]:
    print(number2 + "是回文数")
"""
# 输出两个数的较大者
"""
number3 = input("请输入第一个数：")
number4 = input("请输入第二个数：")
if int(number3) > int(number4):
    print("较大的数是：" + number3)
elif int(number3) < int(number4):
    print("较大的数是：" + number4)
else:
    print("两个数一样大！")
"""
# 比较三个数中的最大值
"""
number5 = input("请输入第一个数：")
number6 = input("请输入第二个数：")
number7 = input("请输入第三个数：")
if number5 > number6:
    if number5 > number7:
        print("三者中最大的是：" + number5)
    else:
        print("三者中最大的是：" + number7)
elif number6 > number7:
    print("三者中最大的是：" + number6)
else:
    print("三者中最大的是：" + number7)
"""

#  & 按位与运算 , | 按位或  ^ 按位异或      ~ 按位取反
print(5 & 7)
# 101               101         101            101
# 111              111          111
# ------------------------------------------------
# 101 = 5          111 = 7      010 = 2        010
print(~5)
print(~4)
print(~3)
print(~-5)
print(~-4)
print(~-3)
print(~1000)
print(~1001)
print(~1002)
print(~-1000)
print(~-1001)
print(~-1002)

# << 二进制位左移  高位丢弃，低位补0    >> 二进制位右移 低位丢弃
print(2 << 2)
print(3 >> 2)
print(13 >> 2)