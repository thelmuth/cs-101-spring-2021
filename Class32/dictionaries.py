
### We want to take a user input string, and count the frequencies of
### how often each character appears.

### keys: characters
### values: how often each character appears in the text
### frequencies will look like: {"t": 3, "e": 5, "n": 2, ...}

text = input("Enter a sentence: ")

frequencies = {}

for char in text:
    if char not in frequencies:
        frequencies[char] = 1 # Assigning the value associated with char to 1
    else:
        # Update this char in the dictionary
        frequencies[char] += 1
        
# print(frequencies)

## Loop through the keys, and print out the associated values
for key in frequencies:
    print(key, "=>", frequencies[key])
        
