# (key-value) 无序
# 访问 get
dict1 = {  "tom":60, "lilei":80 }
print(dict1)
print(dict1["tom"])
print(dict1.get("tom"))
# 添加与修改
dict1["hanmeimei"] = 99
dict1["lilei"] = 90
print(dict1)
# 删除
dict1.pop("hanmeimei")
dict1["addas"] = 100
print(dict1)

# 遍历
for key in dict1:
    print(key,dict1[key])

for value in dict1.values():
    print(value)

for k,v in dict1.items():
    print(k, v)
for i , v2 in enumerate(dict1):
    print(i, v2)

word = input()
d = {}
str1 = """A boy will make you think he loves you, but he really doesn’t. \nA girl will make you think she doesn’t love you, when she really does."""
print(str1)
count = 0
l = str1.split(" ")
print(l)
for i in l:
    c = d.get(i)
    if c == None:
        d[i] = 1
    else:
        d[i] += 1
print(d.get(word))

