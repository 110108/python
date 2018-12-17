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
    turtle.color(random.randint(0,100),random.randint(97,160),255)
    turtle.circle(size/2)
    turtle.end_fill()
    turtle.penup()

def fish(x, y, size):
    turtle.goto(x,y)
    turtle.pendown()
    turtle.right(40)
    turtle.circle(size*2, 100, 15)
    turtle.seth(90)
    turtle.backward(size)
    turtle.forward(size/2)
    turtle.seth(180)
    turtle.forward(1000)
    turtle.penup()
fish(0,0,100)
#TODO: write write function
#TODO: write random code