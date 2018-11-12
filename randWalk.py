import turtle
import random

turtle.colormode(255)
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()

def bounce():
    if((x>=450 or x<=-450)or(y>=400 or y<=-400)):
        turtle.towards(0,0)
def turn():
    turtle.setheading(random.randint(1,360)
def move():
    turtle.forward(random.randint(5,50)
while not false:
    #