import matplotlib.pyplot as plt
import math

### Gets integers from the user until they enter a blank line
### Store these integers in a list, so we can graph them.
# 
# integers = []
# x = input("Enter an integer: ")
# 
# while x != "":
#     integers.append(int(x))
#     x = input("Enter an integer: ")
# 
# print(integers)
# 
# plt.plot(integers)
# plt.show()


def area_of_circle(radius):
    """Calculates the area of a circle based on the radius."""
    return math.pi * (radius ** 2)


r = 5
answer = area_of_circle(r)
print(answer)


def say_hello(name):
    """Prints hello to name"""
    print("Hello", name)


say_hello("Bill")
say_hello("Nancy")




