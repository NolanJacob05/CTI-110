# Nolan Jacob
# 10/28/24
# P4LAB1
# Use loops to make turtle move
import turtle

#making shapes with turtle
line = 0
while line < 4:
    turtle.forward(150)
    turtle.right(90)
    line += 1

for tri_line in range(3):
    turtle.forward(150)
    turtle.left(120)
    tri_line += 1
 
