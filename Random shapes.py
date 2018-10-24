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
    for i in range(5):
        

Pick up the pen.
Jump to a random x, y position (x between -450 and 450 and y between -400 and 400).
Put down the pen.
Start a random color fill (must use 10 or more colors/shades).
Draw a small shape (triangle, square, pentagon, or hexagon).
End the color fill.