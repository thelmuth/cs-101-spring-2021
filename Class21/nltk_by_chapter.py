import nltk
import matplotlib.pyplot as plt

def main():

    ### Read in Pride and Prejudice
    filename = "PrideAndPrejudice.txt"
    file = open(filename, "r")
    pap = file.read()
    
    ## We need to get a list containing each chapter of the book as a string.
    chapters = get_chapters(pap)
    print("The number of chapters is", len(chapters))
    
    ## Now, for each chapter, we need to repeat the process above to
    ## find the most common character in each chapter.
    
    most_common_character_per_chapter = []
    
    for ch_index in range(len(chapters)):
        chapter = chapters[ch_index]
        proper_in_chapter = find_proper_nouns_in_text(chapter)
        filtered_proper = filter_out_titles(proper_in_chapter)
        
        chapter_fd = nltk.FreqDist(filtered_proper)
        
        # First, let's see the 3 most common proper nouns in each chapter
#         print(ch_index, chapter_fd.most_common(3))
        
        character_list = chapter_fd.most_common(1)
        character = character_list[0][0]
        
        print(ch_index, character)
        
        most_common_character_per_chapter.append(character)
        
    ## Now, we have a list containing the most common character in each chapter
    ## where the index in the list is the chapter number
        
    print(most_common_character_per_chapter)
        
    ## Now, we can make a plot, where, for each unique character, we
    ## want the character on the y-axis and the chapters they're most common
    ## in as points.
    
    print("Now making plot of characters...")
    
    unique_characters = unique(most_common_character_per_chapter)
    
    for character in unique_characters:
        
        # Need a list of chapters where the character is most common.
        # Write a function
        chapter_numbers = get_indices(most_common_character_per_chapter, character)
        
        print(character, chapter_numbers)
        
        character_list = [character] * len(chapter_numbers)
        
        
        plt.plot(chapter_numbers, character_list, marker="o", linestyle="none")
        
    plt.xlabel("Chapter")
    plt.show()
        

def get_indices(a_list, target):
    """Returns a list of all indices where target appears in a_list"""
    
    indices = []
    for index in range(len(a_list)):
        if a_list[index] == target:
            indices.append(index)
    
    return indices
        
        
def filter_out_titles(words):
    """Removes titles Mr., Mrs., Miss, from the list of words."""
    
    filtered_words = []
    for word in words:
        if word not in ["Mr.", "Mrs.", "Miss", "Lady", "Bennet"]:
            filtered_words.append(word)
    
    return filtered_words
    
    
def get_chapters(text):
    """Returns a list of the chapters in text.
    Requires each chapter to start with the string Chapter."""
    
    chapters = []
    chapter_index = 0
    
    while chapter_index != -1:
        
        ## We want to find the next occurence of Chapter in the text.
        
        chapter_index = text.find("Chapter", 5) # 5 is the index into text where find should start looking
    
        chapter = text[ : chapter_index]
        chapters.append(chapter)
        
#         print(chapter[:12])
#         print(len(text))
        
        ## Removes first chapter from text
        text = text[chapter_index : ]
        
    return chapters
    
    
    
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