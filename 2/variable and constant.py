age = 18
name = 'xyt'
print("The age's type is: ", type(age))
print("The age's id is: ", id(age))
print("The name's type is: ", type(name))
print("The name's id is: ", id(name))


import random

#随机生成固定步长的值 random.randrange(start, stop, step))
print(random.randrange(2, 10, 2))

# 调整序列
list = [1,2,3,4,5,6]
random.shuffle(list)
print(list)

# 随机生成一个实数
print(random.uniform(3,9))