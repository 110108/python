import turtle
import random

turtle.colormode(255)
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()

def seaweedLeaf(x,width, height):
    turtle.goto(x,-500)
    turtle.pendown
    turtle.begin_fill()
    turtle.color(random.randint(0,13),random.randint(50,230),random.randint(0,26))
    direction = 1
    turtle.left(25)
    for i in range (0, height):
        for i in range (0, 65):
            turtle.forward(width/5)
            turtle.left(direction*2)
        direction*=-1
    turtle.seth(270)
    turtle.forward((height*104)/width)
    turtle.end_fill()
    turtle.penup()
    turtle.update()

def bubble(x,y,size):
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(random.randint(0,13),random.randint(200,255),random.randint(0,26)
    turtle.circle(size)
    turtle.penup()
#TODO: write write function