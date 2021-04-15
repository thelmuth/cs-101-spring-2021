"""
Replicates some of the work of this NYT article.
https://www.nytimes.com/interactive/2020/09/02/upshot/america-political-spectrum.html

In particular, we can take an image, sort its pixels by luminance, and make the
new image.
"""

from PIL import Image

def main():
    ### This is a satellite image of Blue Ridge, VA
#     satellite = Image.open("Blue_Ridge.jpg")
#     satellite = Image.open("Nevada_Summerlin.jpg")
    satellite = Image.open("Hamilton_College.jpg")
    
    satellite.show()
    
    
    print(satellite.width, satellite.height)


    ## Sort the picture by luminance and put it back in order
    sorted_image = nyt(satellite)
    
    
    
def nyt(image):
    """Replicates the NYT study cited in the docstring."""
    
    pixels = get_all_pixels(image)
    
    print("We have", len(pixels), "pixels")
    print("The first 10 pixels are:", pixels[:10])
    
    ### Want to sort the pixels by their luminance values
    ### How can we do that?
    
    print("Starting to find luminance of pixels")
    pixels_with_luminance = attach_luminance_to_pixels(pixels)
    print("Done finding luminance of pixels")
    
    print("The first 10 pixels with luminance are:", pixels_with_luminance[:10])
    
    pixels_with_luminance.sort()
    
    print("The first 10 pixels after sorting are:", pixels_with_luminance[:10])
    
    final_gradient = make_image_from_pixel_list(image.width, image.height,
                                                pixels_with_luminance)
    
    final_gradient.show()
    
    
def make_image_from_pixel_list(width, height, pixels_with_luminance):
    """Creates a new image with given width and height, filled with the
    pixels from pixels_with_luminance."""
    
    new_image = Image.new("RGB", (width, height))
    
    count = 0
    
    # Iterate through the locations in new_image
    for y in range(height):
        print("building new image at y =", y)
        for x in range(width):
            
            pixel_with_luminance = pixels_with_luminance[count]
            pixel = pixel_with_luminance[1]
            
            new_image.putpixel((x, y), pixel)
        
            count += 1
            
    return new_image

    
def attach_luminance_to_pixels(list_of_pixels):
    """Take a list of pixels and make a list of tuples that have luminance
    as the first element and the pixel as the second."""
    
    pixels_with_luminance = []
    
    for pixel in list_of_pixels:
        pwl = (luminance(pixel), pixel)
        pixels_with_luminance.append(pwl)
        
    return pixels_with_luminance
    
    
    
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
    