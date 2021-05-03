from PIL import Image

def main():
    
    image = Image.open("eliza.jpg")
#     image.show()

    my_pixel = Pixel((40, 100, 254))
    
    print(my_pixel)
    print("R component:", my_pixel.r)
    print("RGB tuple:", my_pixel.get_tuple())
#     my_pixel.set_rgb(255, 255, 0)
#     print("RGB tuple after changing it:", my_pixel.get_tuple())
    
    print()
    my_pixel.make_grayscale()
    print("After making it grayscale:", my_pixel.get_tuple())
    
    detect_grayscale(image)
    image.show()
    
    
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
    
    def luminance(self):
        """Returns the luminance of this pixel."""
        
        return (self.r + self.g + self.b) // 3
    
    def make_grayscale(self):
        """Changes a pixel's components to grayscale based on their luminance."""
        
        lum = self.luminance()
#         self.r = lum
#         self.g = lum
#         self.b = lum

        # Instead, we can call them method we already defined for setting RGB
        self.set_rgb(lum, lum, lum)
    
    def __str__(self):
        """This method with this particular name is automatically called whenever
        Python needs a string representation of an object.
        This needs to return (not print) a string.
        
        For this class, it will look like: (R: 40, G: 53, B: 214)
        """
        
        s = "(R: " + str(self.r) + ", G: " + str(self.g) + ", B: " + str(self.b) + ")"
        return s
        
        
def detect_grayscale(image):
    """ Detects grayscale pixels in an image, making them bright red. All other
    pixels are turned into grayscale to make it easier to see the red pixels."""
    
    for y in range(image.height):
        print("y:", y)
        for x in range(image.width):
            
            pixel = Pixel(image.getpixel((x, y)))
            
            if pixel.is_grayscale():
                ## Make pixel bright red
                pixel.set_rgb(255, 0, 0)
                
            else:
                ## Make this pixel grayscale
                pixel.make_grayscale()
            
            image.putpixel((x, y), pixel.get_tuple())
    


if __name__ == "__main__":
    main()
    