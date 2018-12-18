# 可迭代对象 可直接作用于for循环的可迭代对象
# 1. 集合数据类型： list\tuple\dict\set\string
# 2.generator,包括生成器和带yield的generator function

from collections import  Iterable

print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance((),Iterable))
print(isinstance(" ",Iterable))
print(isinstance(1,Iterable))
print(isinstance((x for x in range(10)),Iterable))

"""
# 迭代器：不但作用于for循环，还可以被next()不断调用并返回下一个值
直到最后抛出一个Stopiteration错误，表示无法继续返回下一个值
可以被next()函数调用并不断返回下一个值的对象成为迭代器
"""

from collections import Iterator
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance((),Iterator))
print(isinstance(" ",Iterator))
print(isinstance(1,Iterator))
print(isinstance((x for x in range(10)),Iterator))


l = (x for x in range(5))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
#print(next(l))

a = iter([1,2,3,4,5])
print(next(a))
print(next(a))
a = iter((1,2,3,4,5))
print(next(a))
print(next(a))
a = iter({1,2,3,4,5})
print(next(a))
print(next(a))

str = ""
for line in iter(input,"end"):
    str += line + "\n"
print(str)

