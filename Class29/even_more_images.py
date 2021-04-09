from PIL import Image

def main():

    ### This creates a new image object from the given file
    kids = Image.open("box.jpg")
    kids.show()
    
    print(kids.width, kids.height)
    
#     gradient = make_gradient()
#     gradient.show()

    ### Rotate image
#     kids_rotated = rotate(kids)
#     kids_rotated.show()

    ### Make image smaller
    shrunk = resize(kids, 200, 267)
    shrunk.show()
    
def resize(image, new_width, new_height):
    """Resizes the image to have the new_width as its width, and
    new_height as its height."""
    
    new_image = Image.new("RGB", (new_width, new_height))
    
    for y in range(new_image.height):
        
        for x in range(new_image.width):
            
            old_x = x * image.width / new_image.width
            old_y = y * image.height / new_image.height
            
            pixel = image.getpixel((old_x, old_y))
            new_image.putpixel((x, y), pixel)
            
    return new_image

    
    
def rotate(image):
    """Creates a new image that rotates the original 90 degrees clockwise."""
    
    height = image.height
    width = image.width
    
    new_image = Image.new("RGB", (height, width))
    
    for y in range(height):
        print(y)
        
        for x in range(width):
            
            pixel = image.getpixel((x, y))
            
            new_x = height - 1 - y
            new_y = x
            
            new_image.putpixel((new_x, new_y), pixel)
    
    return new_image
    
    
    
def make_gradient():
    """Makes a new image with a gradient."""
    
    ### First, make a new image
    
    image = Image.new("RGB", (256, 256))
    
    for y in range(image.height):
        
        for x in range(image.width):
            
            # Made a black to white gradient
#             image.putpixel((x, y), (x, x, x))
            
            # Gradient from green to purple
#             image.putpixel((x, y), (x, 128, x))
            
            # Gradient from black to yellow
#             image.putpixel((x, y), (y, y, 0))

            # Gradient from red to cyan, along the diagonal
#             image.putpixel((x, y), (y, x, x))
            
            # Fun gradient
            image.putpixel((x, y), (y, 128, x))
            
            
    return image
    


if __name__ == "__main__":
    main()
    