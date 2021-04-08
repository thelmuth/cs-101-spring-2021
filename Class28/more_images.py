from PIL import Image

def main():

    ### This creates a new image object from the given file
    kids = Image.open("box.jpg")
    
#     kids.show()
# 
#     print(kids.width, kids.height)
#     
#     width = kids.width // 2
#     height = kids.height // 2
#     
#     resized = kids.resize((width, height))
#     
#     print(resized.width, resized.height)
#     
#     resized.show()

    kids_edge = edge_detect(kids, 20)
    
    kids_edge.show()


def luminance(rgb):
    """Finds the average of r, g, and b components in a given pixel."""
    (r, g, b) = rgb
    return (r + g + b) // 3

    
def edge_detect(original_image, luminance_threshold):
    """Finds the edges of objects in an image, and returns a B&W version
    where the edge pixels are black and non-edges are white."""
    
    ### We're going to create a copy of the image, so that we aren't
    ### reading a pixel that we've already changed.
#     image = original_image.copy()

    ## Use a different size to not get last row and column un-edge-detected
    image = Image.new("RGB", (original_image.width - 1, original_image.height - 1))
    
    for y in range(original_image.height - 1):
        print("y:", y)
        
        for x in range(original_image.width - 1):
            
            # Need to get the pixel values of this pixel and the ones
            # right and down of it.
            pixel = original_image.getpixel((x, y))
            pixel_right = original_image.getpixel((x + 1, y))
            pixel_down = original_image.getpixel((x, y + 1))
            
            ## Calculate the luminance of each pixel
            lum_pixel = luminance(pixel)
            lum_right = luminance(pixel_right)
            lum_down = luminance(pixel_down)
            
            ## Compare the luminance values of pixel and its neighbors
            if abs(lum_pixel - lum_right) > luminance_threshold:
                # If here, make this pixel black in image
                image.putpixel((x, y), (0, 0, 0))
            elif abs(lum_pixel - lum_down) > luminance_threshold:
                image.putpixel((x, y), (0, 0, 0))
                
            else:
                ## Not an edge, so turn this pixel white
                image.putpixel((x, y), (255, 255, 255))
    
    return image



if __name__ == "__main__":
    main()
    