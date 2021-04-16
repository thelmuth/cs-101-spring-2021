from PIL import Image

def main():

    stars = Image.open("stars.jpg")
    
    stars.show()
    print(stars.width, stars.height)
    
    

if __name__ == "__main__":
    main()
    
