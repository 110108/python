import turtle
import random

def tri(num, angle):
    left(angle)
    forward(num)
    left(120)
    forward(num)
    left(120)
    forward(num)
    left(120)
    right(angle)
    
def sqr(num, angle):
    left(angle)
    forward(num)
    left(90)
    forward(num)
    left(90)
    forwrd(num)
    left(90)
    forward(num)
    left(90)
    right(angle)

def pent(num, angle):
    left(angle)
    for i in range(5):
        forward(num)
        left(108)
    right(angle)

def hex(num, angle):
    left(angle)
    for i in range(6):
        forward(num)
        left(120)
    right(angle)
    
shapes = [tri, sqr, pent, hex]

def changeShape():
    num = random.randint(0, 3)
    if(num==0):
        tri(random.randint(0, 50)

def move():    
    turtle.penup
    turtle.goto(random.randint(-450,450),random.randint(-400,400))
    turtle.pendown

while(True):
    move()
    changeShape()


#Pick up the pen.
#Jump to a random x, y position (x between -450 and 450 and y between -400 and 400).
#Put down the pen.
#Start a random color fill (must use 10 or more colors/shades).
#Draw a small shape (triangle, square, pentagon, or hexagon).
#End the color fill.