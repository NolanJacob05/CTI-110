# Nolan Jacob
# 10/28/24
# P4LAB1
# Use loops to make turtle move
import turtle


# Drawing innitials with turtle
user_input = input("Would you like to start turle?(yes/no) ")

while user_input == "yes":
    turtle.left(90)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(141)
    turtle.left(135)
    turtle.forward(100)
    turtle.right(90)
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(30)
    turtle.penup()
    turtle.right(180)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(150)
    turtle.pendown()
    

    user_input = input("Would you like to start turle again?(yes/no) ")
