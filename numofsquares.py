import turtle

num = input("How many squares? Type 1-10 ")
squares = int(num)

def makeSquare(num):
    for i in range (4):
        turtle.forward(num)
        turtle.right(90)

for i in range (squares):
    makeSquare(10)
    turtle.forward(10)
turtle.backward(5*squares)