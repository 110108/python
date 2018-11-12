import turtle
import random

turtle.colormode(255)
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()

def sqr():
    for i in range(4):
        turtle.forward(5)
        turtle.left(90)
    turtle.forward(5)
def icoSide(length):
    for i in range(length):
        sqr()
    turtle.right(18)
def icoFull():
    for i in range(20):
        icoSide(10)
icoFull()
turtle.update()