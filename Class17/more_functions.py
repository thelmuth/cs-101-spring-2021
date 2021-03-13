

def main():
    
    # Call to function here
    longer = comparing("cat", "dog")
    print(longer)
    
    no_vowels = only_consonants("hello there class") + " <-- this is only consonants"
    print(no_vowels)
    
    nums = [23, 642, 1111, 93, 3900]
    print(sum_list(nums))
    

def comparing(str1, str2):
    """Given 2 strings, returns the longer of the strings."""
    
    if len(str1) >= len(str2):
        return str1
    else:
        return str2
    
    print("Program will never get here")


def only_consonants(string):
    """Takes a string, and returns the string without any of the vowels"""
    
    string_without_vowels = ""
    for char in string:
        if char in "qwrtypsdfghjklzxcvbnm":
            string_without_vowels += char
            
    return string_without_vowels


def sum_list(numbers):
    """Given a list of numbers, find the sum of the numbers in the list."""
    
    total = 0
    for num in numbers:
        total += num
        
    return total
    




if __name__ == "__main__":
    main()