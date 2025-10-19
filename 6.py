from turtle import *
import time
def drawface():
    penup()
    goto(-120,0)
    pendown()
    pencolor("black")
    pensize(4)
    fillcolor("gold")
    begin_fill()
    seth(90)
    circle(-100,360)
    end_fill()
    
drawface()
def drawmouth():
    penup()
    goto(-80,-10)
    pendown()
    pencolor("black")
    pensize(4)
    circle(-55,-180)
    penup()
    
drawmouth()
def eyes_white():

    # 抬起画笔

    penup()
    seth(90)

    # 往前直走60步

    forward(60)

    # 将角度调整为155度

    seth(155)

    # 落笔

    pendown()

    # 设置画笔粗细为20

    pensize(20)

    # 设置画笔颜色为"white"

    pencolor("white")
    # 绘制一个半径为100，圆心角为45的弧形
    circle(100,45)

    # 抬笔

    penup()
eyes_white()
