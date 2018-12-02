""""
# 截取字符串
str1 = "xyt is a good man！"
str2 = str1[0:8]
print(str2)
print("good" in str1)
print("male" not in str1)
# format string  %d %s %f 占位符
number1 = "xyt"
number2 = "is"
number3 = "a"
print("%-10s\n%-10s\n%-10s" %(number1,number2,number3))
print("%-10s" %number2)
print("%-10s" %number3)
"""

"""
print("good\\nnice\handsomme")
print("good\tnnice\thandsomme")
print("\\\t\\")
print(r"\\\t\\")
"""
"""
# eval(str) 将字符串当成有效的表达式来求值，并返回计算结果
print(eval("123"))
print(eval("+123"))
print(eval("-123"))
print(eval("12+3"))
print(eval("1-23"))
#munber1 = int("12+3")
# len(str) 计算字符串长度
str1 = "12345"
print(len(str1))
print(str1[2])
"""

# lower()  将字符串的大写字母转换成小写  upper()将字符串中的小写字母为大写字母
# swapcase()大小写字母转换    capitalize()只将首字母大写，其余小写
# title()每个单词的首字母大写
str1 = "XYT is a GoD mAn"
print(str1.lower())
print(str1.upper())
print(str1.swapcase())
print(str1.capitalize())
print(str1.title())
# center(width, fillchar)  设置字符串宽度，并且以指定字符填充
print(str1.center(40, "*"))

# ljust(width, fillchar) 返回一个指定宽度字符串，左对齐，以指定字符填充，默认空格填充
print(str1.ljust(40, "*"))
# rjust(width, fillchar) 返回一个指定宽度字符串，右对齐，以指定字符填充，默认空格填充
print(str1.rjust(40, "*"))
# zfill(width)  返回指定宽度字符串，右对齐用0填充字符串
print(str1.zfill(40))

# count(str， _start, _end)返回字符串中 指定字符串出现的次数，可指定位置搜索，默认是在整个字符串搜索
str2 = "xyt is a very very nice man!"
print(str2.count("very"))
print(str2.count("very", 9, len(str2)))
# find(str, _start, _end) 检测字符串中是否包含指定字符串，可以指定范围
# 默认从左到右搜索，得到的是第一次出现的下标 ,rfind(str, _start, _end) 从右到左查找
print(str2.find("very"))
print(str2.rfind("very"))
print(str2.find("very", 10, 18))
print(str2.find("very", 10, 17))

# index(str, _start, _end) 跟find()一样，如果不存在str，则抛出异常：（ValueError: substring not found）
# rindex(str, _start, _end)
#print(str2.index("very", 10, 17))

#lstrip()截掉字符串左侧指定的字符，默认为空格,rstrip()截掉字符串右侧指定字符,strip()左右都街区
str3 = "                  hello"
str4 = "******************hello"
str5 = "hello------------------"
str6 = "********hello***********"
print(str3)
print(str3.lstrip(), str4.lstrip(), str5.rstrip())
print(str3.lstrip(), str4.lstrip("*"), str5.strip("*"))
print(str6.strip("*"))


# replace(oldstr,newstr,counts) 替换字符串中的指定子字符串，默认全部替换，count为指定替换的个数
t1 = "xyt is a good good good guys"
t2 = t1.replace("good", "nice", 2)
print(t2)

# 替换translatio（）配合maketrans（）使用
t3 = str.maketrans("oo", "ce")
t4 = t1.translate(t3)
print(t1)
print(t4)


# startwith(str,start,end) 判断指定范围字符串是否以str开头，默认是整个字符串判断

# endwith（str，start，end）判断指定范围字符串是否以str结尾，默认是整个字符串判断

# encode(encodinng="utf-8",errors="strict")编码
t5 = "good good study"
t6 = t5.encode("utf-8")
print(t6)
# decode()解码
t7 = t6.decode("utf-8")
print(t7)


t8 = "   xyt is   a  good man"
t9 = list(t8)
print(t9)