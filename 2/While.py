# 打印出所有三位数中的水仙花数
"""
flower = 100
while flower <= 999:
    a = flower % 10
    b = flower // 10 % 10
    c = flower // 100
    if flower == a**3 + b**3 + c**3:
        print(flower)
    flower += 1
"""

# 统计出五位数中有多少个回文数
"""
number = 10000
count = 0
while number <= 99999:
    string = str(number)
    if (string[0] == string[4]) and (string[1] == string[3]):
        count += 1
    number += 1
print(count)

"""

# 输入一个整数，我来告诉你它是否是质数
"""
prime = int(input("输入一个整数，我来告诉你它是否是质数："))
if prime == 1 or prime == 4:
    print("No")
elif prime == 2 or prime == 3:
    print("Yes")
elif (prime + 1) % 6 == 0 or (prime - 1) % 6 == 0:
    print("Yes")
else:
    print("No")
"""
# 输入一个数，分解质因数
"""
# 90 = 2*3*3*5
num = int(input())
i = 2
while num != 1:
    if num % i ==0:
        print(i)
        num //= i
    else:
        i += 1
"""


# 输入一个字符串，返回这个字符串中有多少个单词
#"   xyt is a good    man    "    "xyt is a good    man "
string1 = input("请输入一个字符串:")
str1 = string1.strip()
i = 0
count = 0
while i < len(str1):
    while str1[i] != " ":
        i += 1
        if i == len(str1):
            break
    count += 1

    if i == len(str1):
        break
    while str1[i] == " ":
        i += 1

print(count)


# 输入一个字符串，打印出这个字符串所有数据字符的和
"""
string1 = input("请输入一个字符串:")
i = 0
count = 0
# list1 = ["1","2","3","4","5","6","7","8","9"]
string2 = "123456789"
while i < len(string1):
    if string1[i] in string2:
        count += int(string1[i])
    i += 1
print(count)
"""

print("push test")
