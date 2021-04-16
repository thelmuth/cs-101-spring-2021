from PIL import Image

def main():

    kids = Image.open("box.jpg")
    
    kids.show()
    print(kids.width, kids.height)
    
    
    ### Want to calculate: how many uniquely colored pixels are in the image?
    
    
    ## How many distinct colors are possible?
    print("There are 256^3 =", 256 ** 3, "possible pixel colors.")
    
    
    ## How many pixels are in the image?
    print("There are", kids.width * kids.height, "pixels in the image.")
    
    ### How many unique colors are in this image?
    
#     colors = []
    
    # Now try with a dictionary
    colors = {}
    
    for y in range(kids.height):
        print("y =", y, "and length of colors is", len(colors))
        for x in range(kids.width):
            
            pixel = kids.getpixel((x, y))
            
            if pixel not in colors:
                # List way
#                 colors.append(pixel)
                # Dictionary way
                colors[pixel] = 0
    
    print("The number of unique colors in the image is", len(colors))
    
    
    
    
    

if __name__ == "__main__":
    main()
    