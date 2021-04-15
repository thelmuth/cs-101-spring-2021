"""
Replicates some of the work of this NYT article.
https://www.nytimes.com/interactive/2020/09/02/upshot/america-political-spectrum.html

In particular, we can take an image, sort its pixels by luminance, and make the
new image.
"""

from PIL import Image

def main():
    ### This is a satellite image of Blue Ridge, VA
    va = Image.open("Blue_Ridge.jpg")
#     va.show()
    
    
    print(va.width, va.height)


    ## Sort the picture by luminance and put it back in order
    sorted_image = nyt(va)
    
    
    
def nyt(image):
    """Replicates the NYT study cited in the docstring."""
    
    pixels = get_all_pixels(image)
    
    print("We have", len(pixels), "pixels")
    print("The first 10 pixels are:", pixels[:10])
    
    ### Want to sort the pixels by their luminance values
    ### How can we do that?
    
    pixels.sort()
    
    print("The first 10 pixels after sorting are:", pixels[:10])
    
    
    
def get_all_pixels(image):
    """Given an image, returns a list of all pixels in the image."""
    
    pixels = []
    
    for y in range(image.height):
        print("Gathering pixels, at y = ", y)
        for x in range(image.width):
            pixel = image.getpixel((x, y))
            pixels.append(pixel)
            
    return pixels

    
def luminance(rgb):
    """Finds the average of r, g, and b components to determine how
    bright a pixel is."""
    
    (r, g, b) = rgb
    return (r + g + b) // 3


if __name__ == "__main__":
    main()
    