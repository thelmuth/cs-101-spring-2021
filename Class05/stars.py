from turtle import *

larry = Turtle()

larry.width(5)
larry.color("crimson")

## Draw a 8-pointed star!

for _ in range(8):
    larry.forward(150)
    larry.left(90 + 45)

larry.up()
larry.backward(200)
larry.down()
larry.color("gray")

## Draw a 5-pointed star!

# for _ in range(5):
#     larry.forward(100)
#     larry.right(144)

for w in range(5):
    larry.width(w * 4 + 1)
    larry.forward(100)
    larry.right(144)
    


