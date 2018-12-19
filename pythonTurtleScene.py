import turtle
import random

turtle.colormode(255)
turtle.speed(0)
turtle.tracer(0)
turtle.ht()
turtle.penup()

def seaweedLeaf(x, width, height):
    turtle.goto(x, -400)
    turtle.seth(0)
    turtle.pendown
    turtle.begin_fill()
    turtle.color(random.randint(0, 13), random.randint(50, 230), random.randint(0, 26))
    direction = 1
    turtle.left(25)
    for i in range(0, height):
        for i in range(0, 65):
            turtle.forward(width/5)
            turtle.left(direction*2)
        direction *= -1
    turtle.seth(270)
    turtle.forward((height*104)/width)
    turtle.end_fill()
    turtle.penup()
    turtle.update()

def bubble(x, y, size):
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(random.randint(0, 100), random.randint(97, 160), 255)
    turtle.circle(size/2)
    turtle.end_fill()
    turtle.penup()
    turtle.update()

def fish(x, y, size):
    turtle.goto(x, y)
    turtle.seth(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    turtle.right(40)
    turtle.circle(size*2, 100, 15)
    turtle.seth(90)
    turtle.backward(size)
    turtle.right(329)
    turtle.circle(size*2, 100, 15)
    turtle.end_fill()
    turtle.penup()
    turtle.update()
    
def name(x, y, name, font):
    turtle.goto(x, y)
    turtle.write(name, False, "center", (font, 8, "normal"))
    turtle.update()

def drawLayer():
    for i in range(0, random.randint(5, 15)):
        seaweedLeaf(random.randint(-400, 400), random.randint(1, 10), 7)
    for i in range(0, random.randint(1, 50)):
        bubble(random.randint(-400, 400), random.randint(-400, 300), random.randint(1, 50))
    for i in range (0, random.randint(1,50)):
        fish(random.randint(-400,400),random.randint(-400,300),random.randint(1,25))
    
turtle.goto(475,350)
turtle.pendown()
turtle.begin_fill()
turtle.color(random.randint(0,50),random.randint(0,100),random.randint(70,150))
for i in range(0, 25):
    turtle.seth(270)
    turtle.circle(-20,180)
turtle.left(90)
for i in range(0,3):
    turtle.left(90)
    turtle.forward(1000)
turtle.end_fill()
drawLayer()
turtle.update()
#def water(col):
#    turtle.goto(
#TODO: write random code