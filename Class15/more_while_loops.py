import matplotlib.pyplot as plt
import random

### From last class:
### Plot some x-y pairs for the function y = 2^x

# x_values = []
# y_values = []
# for x in range(15):
#     x_values.append(x)
#     y = 2 ** x
#     y_values.append(y)
#     
# plt.plot(x_values, y_values, color="green")
# plt.show()


### How would we change this so that it started with x = 0, and
### continued until y = 2^x is greater than 1 million?

# x_values = []
# y_values = []
# y = 1
# x = 0
# while y < 1000000:
#     x_values.append(x)
#     y = 2 ** x
#     x = x + 1
#     y_values.append(y)
#     
# print(x_values)
# print(y_values)
#     
# plt.plot(x_values, y_values, color="green")
# plt.show()


### Guessing game
### The computer is going to pick a random number between 0 and 100
### The human needs to keep guessing until they guess it correctly
### For each guess, the computer should tell whether the guess is too high
### or too low

answer = random.randint(0, 100)  ## This will include 100

# answer = random.randrange(0, 100) ## This won't include 100

# guess = -1
# 
# guesses = []
# while guess != answer:
#     guess = int(input("Please guess an integer between 0 and 100: "))
#     guesses.append(guess)
#     
#     if guess > answer:
#         print("Your guess of", guess, "was too high.")
#     elif guess < answer:
#         print("Your guess of", guess, "was too low.")
#     else:
#         print("Yay, you got it!")
#     print()
#             
# 
# plt.plot(guesses, marker = "o")
# plt.show()


### Imagine we are creating a website, and want the user to create
### a password that is at least 8 characters long.
### Repeatedly ask the user for a password until they enter one that
### is long enough.

# password = input("Create a password. It must be 8 characters long: ")
# 
# while len(password) < 8:
#     password = input("Sorry, that wasn't long enough. Enter a longer password: ")
# 
# 
# print("Yay, your password is:", password)


### Now, password has to be 8 characters, must have 1 capital, 1 lowercase, and 1 digit

password = input("Create a password: ")
conditions_met = 0

while conditions_met < 4:
    conditions_met = 0
    
    if len(password) < 8:
        print("Sorry, your password isn't long enough")
    else:
        conditions_met += 1
    
    capital_found = False
    lowercase_found = False
    digit_found = False
    for char in password:
        if char in "QWERTYUIOPASDFGHJKLZXCVBNM":
            capital_found = True
        if char in "qwertyuiopasdfghjklzxcvbnm":
            lowercase_found = True
        if char in "1234567890":
            digit_found = True
            
    if capital_found:
        conditions_met += 1
    else:
        print("Sorry, your password doesn't have a capital letter.")
    
    if lowercase_found:
        conditions_met += 1
    else:
        print("Sorry, your password doesn't have a lowercase letter.")
    
    if digit_found:
        conditions_met += 1
    else:
        print("Sorry, your password doesn't have a digit.")        
    

    if conditions_met < 4:
        password = input("Please enter a new password: ")


print("Yay, your password is:", password)





