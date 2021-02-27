
# Print out the vowels in the name
name = input("Enter your name: ")
vowels = ""
for char in name:
    if char in "aeiouAEIOU":
        vowels += char
    
print(vowels)


## We ask the user for a few sentences. We want to change
## each period into an exclamation point.
sentence = input("Write a few sentences: ")
new_sentence = ""
for char in sentence:
    if char == ".":
        char = "!"

    new_sentence += char

print(new_sentence)


# Ask for a social-security number (123-45-6789),
# and we want to remove any characters that are not digits.
# New string should only contain digits in user's input.

ss = input("Enter your SSN: ")
only_digits = ""
digits = "1234567890"
for char in ss:
    if char in digits:
        only_digits += char

print(only_digits)


## Given a list, want to find the longest string in the list.
names = ["Charlie", "Caroline", "Charlotte", "Cathy", "Carol", "Cole", "Chad", "Cat"]
longest = ""
for name in names:
    if len(name) > len(longest):
        longest = name

print(longest)
        


