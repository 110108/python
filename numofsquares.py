import turtle

num = input("How many squares? Type 1-10 ")
squares = int(num)

for i in range (squares):
    turtle.forward(50)
    turtle.right(90)
    turtle.color("red")
    turtle.forward(50)
    turtle.right(90)
    turtle.color("green")
    turtle.forward(50)
    turtle.right(90)
    turtle.color("blue")
    turtle.forward(50)
    turtle.left(90)