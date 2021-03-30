import csv

def main():
    
    room = csv_to_grid("room1.csv")
    
    ## This prints the room, but it's ugly
#     for row in room:
#         print(row)
    
    ## This is a nicer printing of the room:
    print_room(room)
    
    ## Now, let's find the vacuume in the grid:
    location = find_element(room, "vacuum")
    print(location)
    
    
    ### Move the vacuum to the right:
    (room, location) = move_vacuum(room, location, "R")
    print(location)
    print_room(room)
    
    ### Move the vacuum to the right:
    (room, location) = move_vacuum(room, location, "R")
    print(location)
    print_room(room)

    ### Move the vacuum to the right:
    (room, location) = move_vacuum(room, location, "R")
    print(location)
    print_room(room)
    
    ### Move the vacuum down
    (room, location) = move_vacuum(room, location, "D")
    print(location)
    print_room(room)
    
    ### Move the vacuum to the right:
    (room, location) = move_vacuum(room, location, "R")
    print(location)
    print_room(room)
    
    ## Want to make sure that when we do this, the robot does not walk on obstacles.
    for _ in range(4):
        (room, location) = move_vacuum(room, location, "R")
        print(location)
        print_room(room)
    
def move_vacuum(room, location, direction):
    """Moves the vacuum at location in room in the given direction."""
    
    # location is a tuple, so this tuple assignment just gets the row and col
    (row, col) = location
    
    # Check the direction we're trying to move in
    if direction == "R":
        intended_row = row
        intended_col = col + 1
    elif direction == "L":
        intended_row = row
        intended_col = col - 1
    elif direction == "U":
        intended_row = row - 1
        intended_col = col
    elif direction == "D":
        intended_row = row + 1
        intended_col = col        

    if room[intended_row][intended_col] == "obstacle":
        # If running into an obstacle, don't move the robot
        return (room, location)
    else:
        # Intended location isn't an obstacle, so vacuum can move there:
        room[intended_row][intended_col] = "vacuum"
        room[row][col] = "clean"
        
        return (room, (intended_row, intended_col))
    



    
def print_room(room):
    """Prints a room, with one character per cell."""
    
    for row in room:
        
        row_string = ""
        
        for cell in row:
            
            if cell == "obstacle":
                row_string += "O"
            elif cell == "clean":
                row_string += " "
            elif cell == "dirt":
                row_string += "*"
            elif cell == "vacuum":
                row_string += "V"
                
        print(row_string)
    print()
    
    
    
def csv_to_grid(filename):
    """Turns the CSV ifile given by filename into a grid and returns it."""
    
    file = open(filename, "r")
    reader = csv.reader(file)
    grid = []
    
    for line in reader:
        grid.append(line)
        
    return grid
    
    
    
    
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
