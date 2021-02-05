from turtle import *
import math

april = Turtle()
april.width(5)

# Create our first variable, for the length of a side of the triangle
side1 = 129
# This assigns the value 129 to the variable side1
# Can't do: 129 = side1

side2 = 129
hypotenuse = math.sqrt(side1 * side1 + side2 * side2)

# one_half = 1 / 2

# Let's see how to fill in shapes that we draw
april.fillcolor("darkorchid")
april.begin_fill()

april.forward(side1)
april.left(90)
april.forward(side2)

april.left(90 + 45)
april.forward(hypotenuse)

april.end_fill()




