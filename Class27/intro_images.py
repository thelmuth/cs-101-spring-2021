from PIL import Image

def main():

    ### This creates a new image object from the given file
#     kids = Image.open("box_big.jpg")
    kids = Image.open("box.jpg")
    
    ### This displays the image
#     kids.show()

    ### Print some info about the image:
    ### width and height are _attributes_ of image objects, not methods
    print("Width of image:", kids.width)
    print("Height of image:", kids.height)
    
    ### What's the color at pixel (2000, 1600)
    ### getpixel takes 1 argument, a tuple containing x and y coordinates
#     print("RGB at (2000, 1600):", kids.getpixel((2000, 1600)))
#     
#     ### Now, let's set the value of that pixel to black, and see if we can
#     ### find it
#     ### putpixel takes a location tuple and an RGB tuple
#     kids.putpixel((2000, 1600), (0, 0, 0))
#     kids.show()
    

    ### Let's write a function that will change every pixel in the image
    ### Make a blue filter, that will make every pixel more blue
#     blue_filter(kids)
#     kids.show()
    
    ### Makes the image black and white
    black_and_white(kids)
    kids.show()
    
    
def blue_filter(image):
    """Takes an image, and makes it more blue.
    This is a good template for many other image functions."""
    
    ## This will go through every pixel's location, row by row
    for y in range(image.height):
        print("y:", y)
        
        for x in range(image.width):
            
            # Get the RGB values of this location
            (r, g, b) = image.getpixel((x, y))
    
            # Set the pixel, except make B higher
            image.putpixel((x, y), (r, g, b + 100))
            
            ## Turns out, any component value > 255 is automatically
            ## reduced to 255
            ## Any component value < 0 is set to 0


def luminance(rgb):
    """Finds the average of r, g, and b components in a given pixel."""
    
#     r = rgb[0]
#     g = rgb[1]
#     b = rgb[2]

    (r, g, b) = rgb
    return (r + g + b) // 3


def black_and_white(image):
    """Turns an image into black and white.
    Not grayscale, actually black or white."""
    
    for y in range(image.height):
        print("y:", y)
        
        for x in range(image.width):
            
            rgb = image.getpixel((x, y))
            
            ## How bright is that tuple?
            ## Find the average of r, g, and b => this is called luminance
            avg = luminance(rgb)
            
            if avg > 127:
                image.putpixel((x, y), (255, 255, 255))
            else:
                image.putpixel((x, y), (0, 0, 0))
            
    


if __name__ == "__main__":
    main()
    