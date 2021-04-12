from PIL import Image

def main():

    ### This creates a new image object from the given file
    kids = Image.open("box.jpg")
#     kids.show()
    
    print(kids.width, kids.height)

    ### Make image smaller
#     shrunk = resize(kids, 200, 267)
#     shrunk.show()

#     tiny = resize(kids, 20, 27)
#     tiny.show()

#     square = resize(kids, 300, 300)
#     square.show()

#     enlarged = resize(kids, 2000, 2667)
#     enlarged.show()

#     greet("Hello", "Bill", "How's the weather?")

#     greet("Hi", "Andrew")

#     greet("What's up")

#     greet("Howdy", question="How was your day?")

    ## Default test
    new_image = resize(kids, 250)
    new_image.show()
    
    
def greet(greeting, name="person", question="How are you?"):
    
    print(greeting, name, ".")
    print(question)
    
   

def resize(image, new_width, new_height="none provided"):
    """Resizes the image to have the new_width as its width, and
    new_height as its height."""
    
    ### Check if new_height was provided
    if new_height == "none provided":
        ## Calculate new_height to keep proportions the same
        
        new_height = new_width * image.height // image.width
        print("Calculating the new height as:", new_height)
        
    
    new_image = Image.new("RGB", (new_width, new_height))
    
    for y in range(new_image.height):
        
        for x in range(new_image.width):
            
            old_x = x * image.width / new_image.width
            old_y = y * image.height / new_image.height
            
            pixel = image.getpixel((old_x, old_y))
            new_image.putpixel((x, y), pixel)
            
    return new_image

    

if __name__ == "__main__":
    main()
    