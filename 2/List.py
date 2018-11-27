# list 是一种有序的集合
# 格式 列表名 = [列表项1，列表项2，列表项3，.......,列表项n]
# 创建空列表
list1 = []
print(list1)
# 创建带用元素的列表
list2 = [18, 19, 20, 21, 22]
# list中元素可以是不同的类型
list3 = [1, 2, "xyt", True]
print(list3)

list4 = [1, 2, 3, 4, 5]
print(list4[2])

# 替换
list4[2] = 100
print(list4)

# 列表方法
# append 在列表末尾追加一个元素，返回值为None
list5 = [1, 2, 3, 4, 5]
list5.append(6)
print(list5)
list5.append([7, 8, 9])
print(list5)
list6 = list5.append([7, 8, 9])  # 此种方式不可取，不能这样赋值给list6
print(list6)
print(list5)
print(list5.append([7, 8, 9]))
list6 = list5
print(list6)




# extend在列表末尾追加另一个列表中的多个值元素
list7 = [1,2,3,4,5]
list7.extend([7,8,9])
print(list7)

#insert 在下标处插入元素，原数据向后顺延
list8 = [1,2,3,4,5]
list8.insert(1,20)
print(list8)
list8.insert(1, [20,20])
print(list8)

#pop()剔除指定下标的元素，默认剔除末尾的一个元素，并返回剔除的数据
list9 = [1,2,3,4,5]
list9.pop()
print(list9)
list9.pop(2)
print(list9)

# remove 移除列表内容中的某个元素第一匹配结果
list10 = [1,2,3,4,5,4,5,6]
list10.remove(4)
print(list10)

# clear 清除列表中的数据
list11 = [1,2,3,4,5,4,5,6]
list11.clear()
print(list11)

# index 在制定下表范围内，返回查找某个数据第一次出现在列表中的下标，默认范围是整个列表
list12 = [1,2,3,4,5]
print(list12.index(3))
list13 = [1,2,3,4,5,6,3,2,4]
print(list13.index(3,4,8))

# reverse 对列表进行倒序，注意不是排序，并且本身返回值为None
list14 = [1,2,3,4,5,6]
list14.reverse()
print(list14)

#  sort排序,默认为升序排列，语句自身返回值None
list15 = [3,2,1,5,6,4]
list15.sort()
print(list15)
print(list15.sort())

# 拷贝---浅拷贝or引用拷贝，只拷贝索引
list17 = [1,2,3,4,5,6]
list18 = list17
list18[2] = 99
print(list17 , list18)
print(id(list17), id(list18))

str1 = "hhahah"
str2 = str1
str2 = "bianle"
print(str1, str2)
print(id(str1), id(str2))

# copy() 深拷贝，将内存拷贝一份，修改后，不影响拷贝之前的内存空间
list19 = [1,2,3,4,5]
list20 = list19.copy()
list20[2] = 33
print(list19, list20)
print(id(list19), id(list20))

# 将元组转换成列表
list21 = list((1,2,3,4))
print(list21)