import nltk

movie = "I like the movie Mr. & Mrs. Smith! Brad Pitt, Angelina Jolie, etc. are in it."


def main():
    
    ## Use our own sentence tokenizer
    sentences = naive_sentence_tokenizer(movie)
    for s in sentences:
        print(s)
        
        
    ## Use NLTK's sentence tokenizer
    print("------------")
    sentences = nltk.sent_tokenize(movie)
    for s in sentences:
        print(s)
        
        
    ## Can also get a list of words/punctuations from a text
    words = nltk.word_tokenize(movie)
    print(words)


def naive_sentence_tokenizer(text):
    """Should return a list of sentences from the text."""
    
    list_of_sentences = []
    sentence = ""
    
    for char in text:
        sentence += char
        
        if char in ".!?":
            list_of_sentences.append(sentence)
            sentence = ""
    
    return list_of_sentences


main()