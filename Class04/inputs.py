import math

name = input("Enter your name: ")

print("Hello", name)

# Even if the user types a number, it will be stored as a string
age = int(input("Enter your age: "))


print("Your age is", age)

age_in_100_years = 100 + age

print("In 100 years, you will be", age_in_100_years, "years old.")


radius = float(input("Enter a radius: "))
area = math.pi * radius * radius

print("The area of that circle is", area)
