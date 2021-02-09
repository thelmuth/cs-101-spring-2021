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


april.up()
april.forward(100)
april.down()

## Make a 30-60-90 triangle

side1 = 78
hypotenuse = side1 * 2

side2 = math.sqrt(hypotenuse * hypotenuse - side1 * side1)

## Draw the triangle

april.forward(side1)
april.left(120)
april.forward(hypotenuse)
april.left(150)
april.forward(side2)



### What if you want to know the exact value of length of side2?
### Print: allows us to display values to the user

print(side2)
print("The length of side2 is", side2)
print("and the length of side1 is", side1)

## We have printed 2 things on the same line: a string (The length...) and the integer
## side2


