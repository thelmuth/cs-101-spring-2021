####################
## Loops stuff

# print(0)
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)


### A loop to print 0 to 5
# for number in range(1001):
#     print(number)
# print("The loop ended!")


### This one goes from 5 to 9
# for x in range(5, 10):
#     print(x)
#     print("squaring x gives", x * x)
#     print()

# print("before loop")
# 
# for x in range(5, 20, 4):
#     print(x)
#     
# print("after loop")


### Can go backwards in loops
# for time in range(10, -1, -1):
#     print("T-minus", time, "seconds")


### We want to do something for each character in a string:
# animal = "panda"
# for index in range(len(animal)):
#     char = animal[index]
#     print("The character at index", index, "is", char)
    
    
# animal = "panda"
# for index in range(len(animal)):
#     print(animal[:index + 1])


### Special way to iterate through the chars in a string, or elements in a list:
# animal = "panda"
# for squid in animal:
#     print("next char is", squid)


### Iterate through the elements in a list:
# numbers = [16, 2999, 308, 0, 10000]
# for num in numbers:
#     print(num * num * num)
    

### Accumulator pattern
### Use a variable to accumulate a value each time through the loop
### Ex: Want to sum all of the elements in the list
# numbers = [16, 2999, 308, 0, 10000]
# total = 0 # When the loop is done, this will hold our total sum
# for num in numbers:
#     total = total + num
# 
# print("The sum of the numbers is", total)


### We want the sum of all integers between 0 and 1 million
# total = 0
# for num in range(1000001):
#     total = total + num
#     if num == 500000:
#         half_total = total
#     
# print("The sum of all integers 0 to 1 million is", total)
# print("The sum at 500000 is", half_total)

### This does the exact same thing:
total = 0
for num in range(1000001):
    total += num   # this and the following are equivalent
#     total = total + num
    
print("The sum of all integers 0 to 1 million is", total)

