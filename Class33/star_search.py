from PIL import Image
import matplotlib.pyplot as plt

def main():

    stars = Image.open("stars.jpg")
    
#     stars.show()
    print(stars.width, stars.height)
    
    turn_sky_to_black_and_white(stars, 16)
    
    stars.show()

    # For testing
#     turn_pixel_and_neighbors_black(stars, (5, 5))
                                   
                    

    count = count_stars(stars)
    print("Number of stars:", count)               
    stars.show()
    
def count_stars(image):
    """Counts the stars in the image that has been turned into B&W"""
    
    count = 0
    
    for y in range(image.height):
        print("counting: y =", y)
        for x in range(image.width):
            
            pixel = image.getpixel((x,y))
            
            # If pixel is white, then it's part of a star
            if pixel == (255, 255, 255):
                count += 1
                
                turn_pixel_and_neighbors_black(image, (x, y))
                
    return count


def turn_pixel_and_neighbors_black(image, xy):
    """Turns the given pixel and all of its neighbors into black pixels."""
    
#     print(xy)
    
    ### Turn this pixel black
    image.putpixel(xy, (0, 0, 0))
    
    ### Make this function call itself for every neighbor that is white
    
    (x, y) = xy
    
    ## Check the neighbor to the north
    if (y - 1) >= 0 and image.getpixel((x, y - 1)) == (255, 255, 255):
        turn_pixel_and_neighbors_black(image, (x, y - 1))
                
    ## Check the neighbor to the south
    if (y + 1) < image.height and image.getpixel((x, y + 1)) == (255, 255, 255):
        turn_pixel_and_neighbors_black(image, (x, y + 1))
  
    ## Check the neighbor to the east
    if (x + 1) < image.width and image.getpixel((x + 1, y)) == (255, 255, 255):
        turn_pixel_and_neighbors_black(image, (x + 1, y))
  
    ## Check the neighbor to the west
    if (x - 1) >= 0 and image.getpixel((x - 1, y)) == (255, 255, 255):
        turn_pixel_and_neighbors_black(image, (x - 1, y))



def turn_sky_to_black_and_white(image, threshold):
    """Turn the sky into b&w, where stars are white and background is black."""
    
    for y in range(image.height):
        print("y = ", y)
        
        for x in range(image.width):
            
            pixel = image.getpixel((x,y))
            
            lum = luminance(pixel)
            
            if lum > threshold:
                image.putpixel((x,y), (255, 255, 255))
            else:
                image.putpixel((x,y), (0, 0, 0))
    
    
    
def analyze_luminances(image):
    """Makes a plot of luminance counts for the image."""
    
    # Make a list of all of the luminances:
    luminances = []
    
    for y in range(image.height):
        print("y = ", y)
        
        for x in range(image.width):
            
            pixel = image.getpixel((x,y))
            
            lum = luminance(pixel)
            luminances.append(lum)
            
    luminance_counts = []
    
    for lum in range(256):
        print("counting luminances at lum =", lum)
        
        count = luminances.count(lum)
        luminance_counts.append(count)
        
    print(luminance_counts)
    
    plt.plot(luminance_counts)
    plt.show()
    
            
    
def luminance(rgb):
    """Finds the average of r, g, and b components to determine how
    bright a pixel is."""
    
    (r, g, b) = rgb
    return (r + g + b) // 3
    

if __name__ == "__main__":
    main()
    
