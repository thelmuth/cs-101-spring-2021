
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
    
    print("The following indexes colors at row 1 and col 2:")
    print(colors[1][2])
    
    
    ### Want to find the row and column of purple in our grid.
#     print(colors.index("purple")) # This doesn't work on 2D grid

    ## Write a function that returns the row and column of an element within a grid
    print(find_element(colors, "purple"))
    print(find_element(colors, "orange"))
    print(find_element(colors, "teal"))
    
    (row, col) = find_element(colors, "red")
    print("The row of red is", row, "and the col of red is" , col)
    
    ### Here's a rectangular grid of numbers
    num_grid = [[1,2,3,4,5,6],
                [5,3,8,3,5,1],
                [4,3,3,2,1,0],
                [7,7,7,7,7,7]]
    
    print()
    print(num_grid[1][4], "should be 5")
    print(find_element(num_grid, 8))
    
    ### Find all elements
    print()
    print("all green:", find_all_elements(colors, "green"))
    print("all cat:", find_all_elements(colors, "cat"))
    
    ### Summing grid
    print()
    print(sum_grid(num_grid))
    
    
    ### Want to print a grid so it looks nice
#     print(colors) # this is ugly
    print_grid(colors)
    
    
def print_grid(grid):
    """Prints a sort of nice printing of the grid."""
    
    for row in grid:
#         print(row)
        for element in row:
            ## Whatever is passed to end gets printed after the thing that is printed
            print(element, end=", ")
            
        print()
        
    
    
def find_element(grid, target):
    """Should find the row and column of target within grid.
    Will return a tuple (row, col).
    Returns None if target is not in grid."""
    
    # First, iterate over the row indices
    for row_number in range(len(grid)):
        
#         print("Checking row", row_number)
        
        for col_number in range(len(grid[row_number])):
            
#             print("Checking column", col_number)
            
            if grid[row_number][col_number] == target:
                return (row_number, col_number)
            
    return None

def find_all_elements(grid, target):
    """Finds a list of all (row, col) indices where target is in the grid."""
    
    indices = []
    
    ### This pattern of iterating through row and col indices is very common
    for row_number in range(len(grid)):
        for col_number in range(len(grid[row_number])):
            
            if grid[row_number][col_number] == target:
                indices.append((row_number, col_number))
    
    return indices
            
def sum_grid(grid):
    """Takes a grid of numbers, and returns the sum of all numbers in the grid."""
    
    total = 0
    
    ### This is the other very common patter for iterating through grids
    ### Here, we don't care what the row and column are, I just want the elements
    
    for row in grid:
#         print(row)

        ## Each row is just a list, so iterate through that
        for element in row:
#             print(element)
            total += element
            
#         print("----> End of row")
    
    
    return total
            
    
    

if __name__ == "__main__":
    main()
    