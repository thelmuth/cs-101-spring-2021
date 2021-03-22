
def main():
    number = 16
    # number = 16
    
    number = do_thing(number) ## will result in 11
    # number = 11
    
    print(number)

def do_thing(other):
    # other = 16
    
    number = 5
    # number = 5
    
    return other - number
    ## return 11

main()
