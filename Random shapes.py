import turtle
import random

def tri(num, angle):
    turtle.left(angle)
    turtle.forward(num)
    turtle.left(120)
    turtle.forward(num)
    turtle.left(120)
    turtle.forward(num)
    turtle.left(120)
    turtle.right(angle)
    
def sqr(num, angle):
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

def pent(num, angle):
    turtle.left(angle)
    for i in range(5):
        turtle.forward(num)
        turtle.left(108)
    turtle.right(angle)

def hexa(num, angle):
    turtle.left(angle)
    for i in range(6):
        turtle.forward(num)
        turtle.left(120)
    turtle.right(angle)

def changeShape():
    num = random.randint(0, 3)
    
    if(num==0):
        tri(random.randint(0, 50),random.randint(0,360))
    
    if(num==1):
        sqr(random.randint(0, 50),random.randint(0,360))
    
    if(num==2):
        pent(random.randint(0, 50),random.randint(0,360))
    
    if(num==3):
        hexa(random.randint(0, 50),random.randint(0,360))

def move():    
    turtle.penup()
    turtle.goto(random.randint(-450,450),random.randint(-400,400))
    turtle.pendown()

while(True):
    move()
    changeShape()


#Pick up the pen.
#Jump to a random x, y position (x between -450 and 450 and y between -400 and 400).
#Put down the pen.
#Start a random color fill (must use 10 or more colors/shades).
#Draw a small shape (triangle, square, pentagon, or hexagon).
#End the color fill.