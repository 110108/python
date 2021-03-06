import turtle
import random

turtle.colormode(255)
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
turning = False

def drawBord():
    turtle.penup()
    turtle.goto(450,400)
    turtle.setheading(270)
    turtle.pendown()
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(900)
    turtle.right(90)
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(900)
    turtle.penup()
    turtle.home()
    turtle.pendown()

def bounce(x,y):
    
    if((x>=450 or x<=-450)or(y>=400 or y<=-400)):
        turning = False
    if((x<450 and x>-450)and(y<400 and y>-400)):
        turning = True
    return turning

def turn(turning):
    if(turning==True):
        turtle.setheading(random.randint(0,359))
    if(turning==False):
        turtle.setheading(turtle.towards(0,0))

def randMove():
    turtle.forward(random.randint(5,50))

drawBord()
while True:
    x=turtle.xcor()
    y=turtle.ycor()
    turning=bounce(x,y)
    turn(turning)
    randMove()
    turtle.update()