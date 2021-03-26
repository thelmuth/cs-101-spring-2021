"""
Imagine we have a CSV full of quiz and exam scores.
We want to calculate the final grade in the class for every student.
The average of your quiz scores is worth 40% of your grade in the class.
The average of your exam scores is worth 60% of your grade in the class.

"""

import csv

def main():
    
    file = open("cs010grades.csv", "r")
    reader = csv.reader(file) # This allows us to read in each line of the
    ## CSV as lists
    
#     for line in reader:
#         print(line)
    
    ### We want to read in and skip over the header of the CSV:
    header = next(reader, None)
    
    print("Here's the header", header)
    
    for line in reader:
    
        # Want to grab the relevant parts of each line:
        name = line[0]
        quizzes = line[1:11] ### NOTE: This is a list of strings
        exams = line[11:]
    
#         print(name)
#         print(quizzes)
#         print(exams)
#         print()

        ## Write a function that takes a list of strings representing integers
        ## and finds the average of those integers.
        average_quiz_score = average_list_of_strings(quizzes)
        average_exam_score = average_list_of_strings(exams)
        
        print("Average quiz: {:0.5f}".format(average_quiz_score))
        print("Average exam: {:0.5f}".format(average_exam_score))
#         print()

        final_grade = 0.4 * average_quiz_score + 0.6 * average_exam_score
        
        print(name, "has a grade of {:0.4f}".format(final_grade))
        print()
        
        
def average_list_of_strings(list_of_strings):
    """Find the average of the number represented by this list of strings."""
    
    total = 0
    for string in list_of_strings:
        total += int(string)
        
    return total / len(list_of_strings)
    
    

if __name__ == "__main__":
    main()
    