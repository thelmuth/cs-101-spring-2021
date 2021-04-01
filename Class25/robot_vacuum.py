import csv

def main():
    
    room = csv_to_grid("room1.csv")
#     room = csv_to_grid("room2.csv")
    
    ## This prints the room, but it's ugly
#     for row in room:
#         print(row)
    
    ## This is a nicer printing of the room:
    print_room(room)
    
    ## Now, let's find the vacuume in the grid:
    location = find_element(room, "vacuum")
#     print(location)
    
    ## Find the closest dirt cell to the vacuum:
#     closest_dirt = find_closest_dirt(room, location)
#     print("The closest dirt is:", closest_dirt)
    

    (room, location) = clean_the_room(room, location)
    
    
def clean_the_room(room, location):
    """Will move the robot "intelligently" until the room is clean."""
    
    while find_closest_dirt(room, location) != None:
        
        ## Find the row and col of the vacuum
        (vacuum_row, vacuum_col) = location
        
        ## Find the closest dirt location
        (dirt_row, dirt_col) = find_closest_dirt(room, location)
        
        ## Move the vacuum one step toward the dirt
        if vacuum_row < dirt_row:
            (room, location) = move_vacuum(room, location, "D")
            print_room(room)
            input("Moved down") ## Program pauses after every move until user hits enter
        elif vacuum_row > dirt_row:
            (room, location) = move_vacuum(room, location, "U")
            print_room(room)
            input("Moved up")
        elif vacuum_col < dirt_col:
            (room, location) = move_vacuum(room, location, "R")
            print_room(room)
            input("Moved right")            
        elif vacuum_col > dirt_col:
            (room, location) = move_vacuum(room, location, "L")
            print_room(room)
            input("Moved left")
            
    return (room, location)
    

def distance_in_grid(row1, col1, row2, col2):
    """Finds the distance between two locations in the grid.
    Known as the Manhattan distance."""
    
    diff_row = abs(row1 - row2) # abs = absolute value
    diff_col = abs(col1 - col2)
    
    return diff_row + diff_col
    
    
def find_closest_dirt(room, location):
    """Finds the closest dirt to the vacuum's location."""
    
    (vacuum_row, vacuum_col) = location
    
    # Smallest distance to a dirt cell that we've found so far
    min_distance = 100000000
    min_location = None
    
    for row_num in range(len(room)):
        for col_num in range(len(room[0])):
            if room[row_num][col_num] == "dirt":
                distance_to_dirt = distance_in_grid(vacuum_row, vacuum_col,
                                                    row_num, col_num)
                
                # We want to check if the distance_to_dirt is smaller than
                # any that we've found so far. If so, keep track of it
                if distance_to_dirt < min_distance:
#                     print("Found a nearer dirt:", distance_to_dirt, (row_num, col_num))
                    min_distance = distance_to_dirt
                    min_location = (row_num, col_num)
    
    return min_location
                
    
    
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
