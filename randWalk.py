import turtle
import random

turtle.colormode(255)
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
turning = True

def bounce():
    if((x>=450 or x<=-450)or(y>=400 or y<=-400)):
        turning = False
    #if((x<=400 and x>=-400)and(y<=350 and y>=-350)):
        #turning = True

def turn():
    if(turning==True):
        turtle.setheading(random.randint(0,359))
    if(turning==False):
        turtle.setheading(turtle.towards(0,0))

def randMove():
    turtle.forward(random.randint(5,50))

while True:
    x=turtle.xcor()
    y=turtle.ycor()
    bounce()
    turn()
    randMove()
    turtle.update()