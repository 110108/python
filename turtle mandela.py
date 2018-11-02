import turtle
import random

turtle.colormode(255)
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()

def leg(reps):
    for r in range((reps+1)):
        turtle.begin_fill()
        turtle.fillcolor((random.randint(50,255)),(random.randint(50,255)),(random.randint(50,255)))
        for z in range(50):
            turtle.forward(2)
            turtle.left(1)
        for y in range(50):
            turtle.forward(2)
            turtle.right(1)
        turtle.left(230)
        for x in range(50):
            turtle.forward(2)
            turtle.right(1)
        for w in range(50):
            turtle.forward(2)
            turtle.left(1)
        turtle.end_fill()
        turtle.home()
        turtle.setheading(360 / reps * r)

rep=input("How many repetitions? ")
rep=int(rep)
leg(rep)