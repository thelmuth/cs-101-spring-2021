
# numbers = [16, 2999, 308, 0, 10000]
# 
# ### We want a new list squares, which will be every element of
# ### the list numbers, except squared.
# squares = []
# 
# for num in numbers:
#     squares.append(num * num)
#     
# print(squares)


### Accumulate over a string:
### Want to take every character in the string, and add a period
### after it in a new string.
# city = "NYC"
# new_city = ""    # accumulator, starts as an empty string
# for c in city:
#     new_city += c + "."
#     
#     print(new_city)


### We have a list of names, and want a string containing those
### names separated by commas
# names = ["Elsa", "Anna", "Olaf", "Kristoff", "Sven"]
# frozen = ""
# for index in range(len(names) - 1):
#     
#     frozen += names[index] + ", "
# 
# frozen += names[-1]
# print(frozen)


## elif
## Want to print the letter grade associated with grade
# grade = 34
# if grade > 90:
#     print("A")
#     print("yay")
# elif grade > 80:
#     print("B")
#     
# elif grade > 70:
#     print("C")
#     print("outside of if")    
# elif grade > 60:
#     print("D")
#     
# else:
#     print("F")


### Examples of if statements in loops

### Print all of the even numbers between 0 and 50:
# for num in range(50):
#     # We can tell if a number is even if num % 2 == 0
#     if num % 2 == 0:
#         print(num)

# Print out the vowels in the name
name = input("Enter your name: ")
for char in name:
    if char in "aeiouAEIOU":
        print(char)
    





