from PIL import Image, ImageDraw

def main():
    
    leo = MyTurtle("Leo")
    
#     leo.forward(100)
#     
#     leo.left()
#     leo.forward(200)
#     leo.left()
#     leo.forward(300)

    for x in range(10):
        leo.forward(x * 10)
        leo.right()
        
        
    leo.width(20)
    leo.pencolor((255, 0, 0))
    leo.up()
    leo.forward(100)
    leo.down()
    leo.forward(100)
    
    leo.pencolor((0, 190, 190))
    leo.goto(10, 10)
    leo.forward(100)
    
    leo.pencolor((220, 200, 0))
    leo.goto(100, -250)
    leo.forward(200)
    
    sarah = MyTurtle("Sarah", leo.image)
    sarah.pencolor((0, 255, 0))
    sarah.forward(100)
    
    leo.right()
    leo.forward(100)
    
    sarah.left()
    sarah.width(5)
    sarah.forward(200)
    
    leo.show()
    


class MyTurtle:
    """Implement a class that replicates the behavior of turtles."""
    
    def __init__(self, name, image = None):
        """Constructor for the MyTurtle class."""

        if image == None:
            ## The image itself that the turtle is drawn on
            self.image = Image.new("RGB", (600, 600), (255, 255, 255))
        else:
            self.image = image
            
        self.image_draw = ImageDraw.Draw(self.image)

        self.name = name
        self.color = (0, 0, 0)
        self.pen_width = 1
        
        # x and y locations
        self.x = 300
        self.y = 300
        
        ## Turtle can only face 4 directions: north, south, east, and west
        self.headings = [(1, 0), # East
                         (0, -1), # North
                         (-1, 0), # West
                         (0, 1)] # South
        
        self.heading = 0 ## Indicates which index in our headings list to use
        
        ## This handles up/down
        self.pen_down = True
        
        
    def show(self):
        """Shows the current image."""
        self.image.show()
        
    def draw(self):
        """Draws at a single location where the turtle is."""
        
        if self.pen_width == 1:
            self.image.putpixel((self.x, self.y), self.color)
            
        else:
            radius = self.pen_width // 2
            self.image_draw.ellipse((self.x - radius, self.y - radius,
                                    self.x + radius, self.y + radius),
                                    fill = self.color)
        
        
    def forward(self, pixels):
        """Moves the turtle forward the given number of pixels."""
        (delta_x, delta_y) = self.headings[self.heading]

        for _ in range(pixels):
            if self.pen_down:
                self.draw()
            
            # Change the turtle's location
            self.x += delta_x
            self.y += delta_y

    def left(self):
        """Turn turtle to the left 90 degrees"""
        self.heading = (self.heading + 1) % 4

    def right(self):
        """Turn turtle to the right 90 degrees."""
        self.heading = (self.heading - 1) % 4
        
    def up(self):
        """Lifts the pen up"""
        self.pen_down = False
        
    def down(self):
        """Puts the pen down"""
        self.pen_down = True

    def goto(self, new_x, new_y):
        """Sends turtle to (new_x, new_y)
        Does not draw along the way."""
        self.x = new_x + 300
        self.y = 300 - new_y
        
    def pencolor(self, new_color):
        """Changes the pen's color to new_color"""
        self.color = new_color
        
    def width(self, new_width):
        """Changes the pen's width."""
        self.pen_width = new_width

if __name__ == "__main__":
    main()
    