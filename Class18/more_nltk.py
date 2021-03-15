import nltk
import random

movie = "I like the movie Mr. & Mrs. Smith! Brad Pitt, Angelina Jolie, etc. are in it."

buses = "I will book the bus ticket while I bus the table and read a book."

cs101 = "Today we learned about the natural language tool kit, parts of speech, and detokenizing. Every student sat in a chair." 

NOUNS = ["fork", "dog", "tray", "elevator", "sparkle", "python", "practice", "pizza",
         "government", "apple"]

def main():

    ## Can also get a list of words/punctuations from a text
#     words = nltk.word_tokenize(movie)
#     print(words)

    ### NLTK can identify the parts of speach (POS) of words
    ### It takes a tokenized list of words, instead of a single word

    words2 = nltk.word_tokenize(buses)
#     print(words2)

    pos = nltk.pos_tag(words2)
#     print(pos)
#     for tup in pos:
#         print(tup[0], " => ", tup[1])

    ## This will display all of the parts of speech
#     nltk.help.upenn_tagset()

    ## What if we want to look up a specific tag, such as VBP
#     nltk.help.upenn_tagset("VBP")

    ### Let's write a function that replaces nouns in a text with other random nouns.
#     new_sentence = replace_nouns(cs101)
#     print(new_sentence)
    
    
    ### Read in Pride and Prejudice
    filename = "PrideAndPrejudice.txt"
    file = open(filename, "r")
    pap = file.read()
    
    print(pap[:10000])
    
    
    
def replace_nouns(text):
    """For each noun in the text, replace it with a random noun from the list
    of nouns."""

    words = nltk.word_tokenize(text)
    words_pos = nltk.pos_tag(words)
    
    new_sentence_list = []

    ### This loops over tuples in the list, and assigns word to the first
    ### element of each tuple, and pos to the second element of each tuple.
    for word, pos in words_pos:
        
        # Look for nouns
        if pos == "NN":
            new_word = random.choice(NOUNS)
        else:
            new_word = word
        
        new_sentence_list.append(new_word)
    
    ### Instantiate our detokenizer, then use it on a list of words
    twd = nltk.tokenize.treebank.TreebankWordDetokenizer()
    sentence = twd.detokenize(new_sentence_list)
        
    return sentence



main()