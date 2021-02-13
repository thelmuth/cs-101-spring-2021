
def main():
    
    #tweet = input("Enter a tweet: ")
    
    tweet = "Computer science #rules #python #cs-101"
    index = tweet.find("#")
    
    part_tweet = tweet[index : ]
    
    print(part_tweet)
    
    
    
    
if __name__ == "__main__":
    main()
