
def main():
    
    ## Create a grid of color strings, which could be pixels in an image.
    colors = [["green", "orange", "brown", "orange"],
              ["blue", "green", "green", "orange"],
              ["purple", "red", "blue", "red"],
              ["yellow", "brown", "green", "yellow"]]

    ### Want to print a grid so it looks nice
    print_grid(colors)
    
    ### Let's find the location in the grid where two elements next to each
    ### other in the same row are the same element.
    ### This type of thing where we consider adjacent elements in a grid
    ### is common when working with images.
    
    print(find_adjacent_same_elements(colors))
    
    ### Find same element in the same column
    print(find_column_adjacent_same_elements(colors))
    
    
def find_adjacent_same_elements(grid):
    """Find two elements that are adjacent in the same row of the grid.
    Returns the (row, col) of the first one.
    Returns None if no such elements exist."""
    
    for row_number in range(len(grid)):
        for col_number in range(len(grid[0]) - 1):
            
            if grid[row_number][col_number] == grid[row_number][col_number + 1]:
                return (row_number, col_number)
            
    return None


def find_column_adjacent_same_elements(grid):
    """Find two elements that are adjacent in the same column of the grid.
    Returns the (row, col) of the first one.
    Returns None if no such elements exist."""
    
    for row_number in range(len(grid) - 1):
        for col_number in range(len(grid[0])):
            
            if grid[row_number][col_number] == grid[row_number + 1][col_number]:
                return (row_number, col_number)
            
    return None
            
    
    
    
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
        for col_number in range(len(grid[row_number])):
            
            if grid[row_number][col_number] == target:
                return (row_number, col_number)
            
    return None

    

if __name__ == "__main__":
    main()
    