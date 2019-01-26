print("来学习函数吧")

def MySun(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(MySun(1,2,3,4,5,6))

def func(**args):
    print(args)
    print(type(args))
func(x=1, y=2, z=3)

""" 
lambada的主体是有一个表达式，而不是代码块，仅仅只能在lambda中
封装简单逻辑
lambada的函数有自己的命名空间
"""

sum = lambda num1, num2: num1 + num2
print(sum(1,2))

# 打印99乘法表
def Print9x9():
    str = " "
    for i in range(1,10):
        for j in range(1,i+1):
            print("%d x %d = %d " % (j, i, j * i))

Print9x9()


def func():
    print('good good study ,day day up')
def outer(func):
    def inner():
        print('**************************')
        func()
    return inner()

f = outer(func)


# 作用域 局部作用域、全局作用域、内建作用域


try:
    #print(num)
    #print(3 / 0)
    print(3/1)
except ZeroDivisionError as e:
    print("除数为0")
except NameError as e:
    print("没有定义该变量")

else:
    print("代码没问题")
