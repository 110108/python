import turtle
import random

cols = ["red","green","blue","purple","orange","pink","teal"]

turtle.tracer(5)
turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
turtle.hideturtle()
for i in range(300):
    color = random.choice(cols)
    turtle.color(color)
    turtle.forward(50)
    turtle.left((i))