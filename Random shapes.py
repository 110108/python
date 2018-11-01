import turtle
import random

turtle.speed(10)
turtle.colormode(255)

def tri(num, angle):
    turtle.begin_fill()
    turtle.fillcolor((random.randint(0,255)),((random.randint(0,255))),(random.randint(0,255)))
    turtle.left(angle)
    turtle.forward(num)
    turtle.left(120)
    turtle.forward(num)
    turtle.left(120)
    turtle.forward(num)
    turtle.left(120)
    turtle.right(angle)
    turtle.end_fill()
    
def sqr(num, angle):
    turtle.begin_fill()
    turtle.fillcolor((random.randint(0,255)),((random.randint(0,255))),(random.randint(0,255)))
    turtle.left(angle)
    turtle.forward(num)
    turtle.left(90)
    turtle.forward(num)
    turtle.left(90)
    turtle.forward(num)
    turtle.left(90)
    turtle.forward(num)
    turtle.left(90)
    turtle.right(angle)
    turtle.end_fill()

def pent(num, angle):
    turtle.begin_fill()
    turtle.fillcolor((random.randint(0,255)),((random.randint(0,255))),(random.randint(0,255)))
    turtle.left(angle)
    for i in range(5):
        turtle.forward(num)
        turtle.left(72)
    turtle.right(angle)
    turtle.end_fill()

def hexa(num, angle):
    turtle.begin_fill()
    turtle.fillcolor((random.randint(0,255)),((random.randint(0,255))),(random.randint(0,255)))
    turtle.left(angle)
    for i in range(6):
        turtle.forward(num)
        turtle.left(60)
    turtle.right(angle)
    turtle.end_fill()

def changeShape():
    num = random.randint(0, 3)
    
    if(num==0):
        tri(random.randint(10, 50),random.randint(0,360))
    
    if(num==1):
        sqr(random.randint(10, 50),random.randint(0,360))
    
    if(num==2):
        pent(random.randint(10, 50),random.randint(0,360))
    
    if(num==2 or num==3):
        hexa(random.randint(10, 50),random.randint(0,360))

def move():    
    turtle.penup()
    turtle.goto(random.randint(-450,450),random.randint(-400,400))
    turtle.pendown()

for i in range(200):
    move()
    changeShape()

#Start a random color fill (must use 10 or more colors/shades).