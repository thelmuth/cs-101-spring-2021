import nltk
import matplotlib.pyplot as plt

def main():

    ### Read in Pride and Prejudice
    filename = "PrideAndPrejudice.txt"
    file = open(filename, "r")
    pap = file.read()
    
#     sentence = "I went to to the school for a lunch lunch meeting."
#     output_repeated_words(sentence)

#     output_repeated_words(pap)
    
    
    ### Find sentences with 2 characters in them
#     elizabeth_and_darcy = sentences_containing_both_characters(pap, "Elizabeth", "Darcy")
#     
#     for sent in elizabeth_and_darcy:
#         print(sent)


#     bingley_and_jane = sentences_containing_both_characters(pap, "Bingley", "Jane")
#     
#     for sent in bingley_and_jane:
#         print(sent)

#     cow = sentences_containing_both_characters(pap, "cow", "a")
#     
#     for sent in cow:
#         print(sent)

    ### Make a plot of the most frequent proper nouns in the text.
    ### Who are the most important characters?

    print("Finding proper nouns; this can be slow...")

    proper_nouns = find_proper_nouns_in_text(pap)

#     print(proper_nouns)

    ### How many times does Elizbeth appear in PaP?
    elizabeth = get_occurences(proper_nouns, "Elizabeth")
    print("Elizabeth appears", elizabeth, "times in PaP")
    
    ### How about Darcy?
    darcy = get_occurences(proper_nouns, "Darcy")
    print("Darcy appears", darcy, "times in PaP")
    
    ### Make a list of all unique proper nouns in our list
    unique_proper_nouns = unique(proper_nouns)
    
#     print(unique_proper_nouns)

    ## Now, write a function that tells us the number of times each unique
    ## proper noun appears in the list of proper_nouns
    ## Ex: if our unique_proper_nouns list is ["Mr.", "Bennet", ...]
    ## then our new list should be            [434,    210,   .... ]
    ## to indicate that Mr. appears 434 time, Bennet appears 210 times, etc.
    
    proper_noun_counts = get_counts(proper_nouns)
#     print(proper_noun_counts)
    
    plt.bar(unique_proper_nouns, proper_noun_counts)
    plt.show()
    
    
    
    
def get_counts(words):
    """Returns a frequency list corresponding to the unique words in list words."""
    
    freq_list = []
    unique_words = unique(words)
    
    for word in unique_words:
        count = get_occurences(words, word)
        freq_list.append(count)

    return freq_list



def get_occurences(words, target):
    """Returns the number of times that target appears in words."""
    
    count = 0
    for word in words:
        if target == word:
            count += 1
    
    return count
            



def sentences_containing_both_characters(text, character1, character2):
    """Returns a list of sentences that contain the words character1 and character2"""
    
    sentences = nltk.sent_tokenize(text)
    found_sentences = []
    
    for sentence in sentences:
        if character1 in sentence and character2 in sentence:
            found_sentences.append(sentence)
            
    return found_sentences








def output_repeated_words(text):
    """"Prints any words in text that are repeated."""
    
    words = nltk.word_tokenize(text)
    
    for index in range(0, len(words) - 1):
        if words[index] == words[index + 1]:
            print(index, words[index])
    
    
    
    
    
    
    
    
    
    
    
    
################################
## Functions below here written in lab

def find_proper_nouns_in_text(text):
    """Finds and returns a list of all proper nouns in text."""
    
    words = nltk.word_tokenize(text)
    words_with_pos = nltk.pos_tag(words)
    
    all_proper_nouns = []
    for word, pos in words_with_pos:
        if pos == "NNP":
            all_proper_nouns.append(word)
            
    return all_proper_nouns








def unique(list_with_dupes):
    """ Returns the given list with all duplicates removed. """
    
    clean_list = []
    
    for entry in list_with_dupes:
        if entry not in clean_list:
            clean_list.append(entry)
            
    return clean_list


main()