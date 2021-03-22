
def main():
    
    ## Create a grid of color strings, which could be pixels in an image.
    colors = [["green", "orange", "brown", "orange"],
              ["blue", "green", "green", "orange"],
              ["purple", "red", "blue", "red"],
              ["yellow", "brown", "green", "yellow"]]
    
    print(colors)
    
    ## What's going to happen when we index and element of colors?
    mystery = colors[2]
    print("mystery = ", mystery)
    print(mystery[1])
    
    
    
    
    
    

if __name__ == "__main__":
    main()
    