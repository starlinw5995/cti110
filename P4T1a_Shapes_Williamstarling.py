# This program will draw 100 squares.
# 10/15/2019
# CTI-110 P4T1a - Turtle Graphic: Repeating Squares.
# William Starling
#
#  This program will draw 100 squares.

# Import turtle.
import turtle

# Name set the angle and side.
angle = 90
side = 10

# Hide the turtle cursor.
turtle.hideturtle()

# Set the speed.
turtle.speed(30)

# Turn right 180 degrees.
turtle.right(180)

# Set the program with a loop: for square in range(100).
for square in range(100):
    turtle.forward(side)
    turtle.right(angle)
    turtle.forward(side)
    turtle.right(angle)
    turtle.forward(side)
    turtle.right(angle)
    turtle.forward(side)
    turtle.right(angle)

    # Make the turtle go back to the X znd Y coordinates of(0,0).
    turtle.goto(0,0)

    # The sides increase by 3 pixels for the nest square.
    side += 3
