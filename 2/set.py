# 创建set需要一个list 、tuple、或者dict作为输入集合，无序不重复，重复元素会被过滤
s1 = set([1,2,3,4,5,4,3,2,1])
print(s1)
s2 = set((1,2,3,4,3,2,1))
print(s2)
s3 = set({"str1":8,"str2":9,"str3":10})
print(s3)
# 添加 set的元素不能是list和字典
s1.add(6)
s1.add(5)
print(s1)
# update() 将插入的list、tuple、dict 打碎之后，逐个添加到set中
s1.update([6,7,8])
print(s1)

# remove 直接删除元素的值
s1.remove(6)
print(s1)

# 遍历
for i in s1:
    print(i)

s8 = set([1,2,3])
s9 = set([2,3,4,5])
# 交集
a1 = s8 & s9
a2 = s8 | s9
print(a1,a2)
print(type(a1),type(a2))


