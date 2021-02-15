"""
tweet.py
Written by CS-101
This program inputs a tweet from the user, and finds and prints the
first hashtag in the tweet.

NOTE: This is called a docstring.
"""


def main():
    
    #tweet = input("Enter a tweet: ")
    
    tweet = ""
    index = tweet.find("#")
    
    part_tweet = tweet[index : ]
    print("part_tweet", part_tweet)

    ## Alternative:
#     index_space = tweet.find(" ", index)
    
    index_space = part_tweet.find(" ")
    
    print(index_space)
    
    hashtag = part_tweet[ : index_space]
    
    print("Here's the hashtag:", hashtag)
    
if __name__ == "__main__":
    main()


### Table of test cases
### Input    |   Expected Output
### "Computer science #rules #python #cs-101"  |  "#rules"
### "Computer science #rules"  |  "#rules" ## semantics error, gives #rule
### "Computer science #rules#python#cs-101 end"  | "#rules" or "#rules#python#cs-101"
### "Computer science"  |  ""
### ""  |  ""

