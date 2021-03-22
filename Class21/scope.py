
def main(): 
    x = do_some_addition(4)
    sums = sum_evens(x)
    print("The sum of even #s up to", x, "is", sums)

def do_some_addition(z):
    x = 6
    y = x + z
    return y

def sum_evens(limit):
    total = 0
    for x in range(0, limit, 2):
        total += x  
    return total


if __name__ == "__main__":
    main()
