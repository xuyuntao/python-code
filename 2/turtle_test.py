"""
一个简单绘图工具
提供一个小海龟，可以把它理解为一个机器人，只能听懂有限的命令


其他命令
done（）保持程序不结束
"""

import turtle
turtle.speed(10)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.goto(0,0)
turtle.up()
turtle.goto(-100,100)
turtle.down()
turtle.pensize(5)
turtle.pencolor("red")
turtle.goto(100,-100)
while 1:

    turtle.right(45)
    turtle.circle(50)
turtle.done()





