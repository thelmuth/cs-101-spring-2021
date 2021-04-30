from PIL import Image

def main():
    
    image = Image.open("eliza.jpg")
#     image.show()

    my_pixel = Pixel((40, 100, 254))
    
    print(my_pixel)
    print("R component:", my_pixel.r)
    print("RGB tuple:", my_pixel.get_tuple())
    my_pixel.set_rgb(255, 255, 0)
    print("RGB tuple after changing it:", my_pixel.get_tuple())
    
    
#     gray_pixel = Pixel((80, 80, 80))
#     print(gray_pixel)
#     print("gray_pixel's R component:", gray_pixel.r)
# 
#     not_gray = Pixel((54, 54, 190))
#     
#     print()
#     print("my_pixel grayscale?", my_pixel.is_grayscale())
#     print("gray_pixel grayscale?", gray_pixel.is_grayscale())
#     print("not_gray grayscale?", not_gray.is_grayscale())
    
    
    
    
#     for y in range(image.height):
#         for x in range(image.width):
#             pixel_tuple = image.getpixel((x,y))
#             pixel = Pixel(pixel_tuple)
#             
#             ### Print all locations that are grayscale in image
#             if pixel.is_grayscale():
#                 print("Location", (x, y), "is grayscale with a value of",
#                         pixel.get_tuple())
    
    

class Pixel:
    """Represents a pixel in an image."""
    
    ## The following code is what is called when we create a new
    ## Pixel object:
    ## This is a method:
    def __init__(self, rgb):
        """
        __init__ is always the name of the *constructor* of a class.
        A constructor is the method that gets called when we create
        a new object.
        The first parameter of any method in Python must be self.
        self refers to the object that is created by this class.
        rgb is the other parameter, and will be a RGB tuple.
        """
        
        ## The following are this class's attributes
        self.r = rgb[0]
        self.g = rgb[1]
        self.b = rgb[2]
        
    def get_tuple(self):
        """Returns the tuple corresponding with this pixel."""
        return (self.r, self.g, self.b)
    
    def is_grayscale(self):
        """Return True if this is a grayscale pixel, and False otherwise."""
        return self.r == self.g == self.b

    def set_rgb(self, r, g, b):
        """This method sets the r, g, and b attributes of this pixel.
        Note: This doesn't return anything, since its purpose is to
        change the pixel."""
        self.r = r
        self.g = g
        self.b = b
    
    
    
    


if __name__ == "__main__":
    main()
    