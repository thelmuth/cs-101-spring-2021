from turtle import *

leo = Turtle()

leo.speed(1)
leo.width(3)

### Python ignores every line that starts with a #
### This is called commenting, because it allows us to leave comments
### in our code.
# leo.forward(80)
# leo.forward(50)
# leo.left(60)
# leo.forward(110)
# 
# leo.left(170)
# leo.forward(200)

# Name of color must be in quotation marks
# This makes it a string of characters
leo.pencolor("red")
leo.forward(100)
leo.left(120)

leo.pencolor("blue")
leo.forward(100)
leo.left(120)

leo.pencolor("magenta")
leo.forward(100)

## We'll talk more about this later: it is an RGB value
leo.pencolor(200, 30, 250)
leo.forward(100)

