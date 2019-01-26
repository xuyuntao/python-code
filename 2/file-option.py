import pickle
path1 = r"C:\Users\xuyun\Desktop\oracle爱数备份.txt"
f = open(path1, "r", encoding="utf-8", errors="ignore")
"""
#str1 = f.read()
str1 = f.read(10)
print("*"+str1+"*")
str2 = f.read(10)
print("*"+str2+"*")
str4 =  f.readline()
print(str4)
str5 = f.readline()
print(str5)
str6 = f.readline(15)
print("*"+str6+"*")
"""
list1 = f.readlines()

print(list1[1])


# f.seek(0) 修改文件描述符的位置为文件开头

f.close()


path2 = r"C:\Users\xuyun\Desktop\new.txt"
with open(path2, "w", encoding="utf-8", errors="ignore") as f2:
    print("****************")
    f2.write("This is the first line!")  #将信息写入缓冲区
    f2.flush() #刷新缓冲区，写入文件

path2 = r"C:\Users\xuyun\Desktop\new.txt"
with open(path2, "wb") as f3:
    str1 = "hello 叶锦行！"
    f3.write(str1.encode("utf-8"))

with open(path2, "rb") as f4:
    data = f4.read()
    print(data, type(data))
    newdata = data.decode("utf-8")
    print(newdata, type(newdata))


myList = [1, 2, 34, 567, "Are you the one ? "]
path2 = r"C:\Users\xuyun\Desktop\new.txt"
with open(path2, "wb") as f5:
    pickle.dump(myList, f5)
with open(path2, "rb") as f6:
    tempList = pickle.load(f6)
    print(tempList)













