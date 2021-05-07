from PIL import Image

def main():
    
    leo = MyTurtle("Leo")
    
    leo.forward(100)
    
    leo.show()



class MyTurtle:
    """Implement a class that replicates the behavior of turtles."""
    
    def __init__(self, name):
        """Constructor for the MyTurtle class."""

        ## The image itself that the turtle is drawn on
        self.image = Image.new("RGB", (600, 600), (255, 255, 255))

        self.name = name
        self.color = (0, 0, 0)
        
        # x and y locations
        self.x = 300
        self.y = 300
        
        ## Turtle can only face 4 directions: north, south, east, and west
        self.headings = [(1, 0), # East
                         (0, -1), # North
                         (-1, 0), # West
                         (0, 1)] # South
        
        self.heading = 0 ## Indicates which index in our headings list to use
        
    def show(self):
        """Shows the current image."""
        self.image.show()
        
    def forward(self, pixels):
        """Moves the turtle forward the given number of pixels."""
        (delta_x, delta_y) = self.headings[self.heading]

        for _ in range(pixels):
            self.image.putpixel((self.x, self.y), self.color)
            
            # Change the turtle's location
            self.x += delta_x
            self.y += delta_y





if __name__ == "__main__":
    main()
    