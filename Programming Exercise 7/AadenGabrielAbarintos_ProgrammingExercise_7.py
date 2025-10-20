# AadenGabrielAbarintos_ProgrammingExercise_7.py
# This program allows the user to enter a paragraph,
# including sentences that begin with numbers.
# The program then displays each individual sentence and
# counts how many sentences are in the paragraph.

# Import the regular expression module
import re


# Define the main function
def main():
    
    # Ask the user to input their paragraph
    paragraph = input("Enter a paragraph: ")

    # Split the paragraph
    sentences = split_sentences(paragraph)

    # Display the data
    print("Individual Sentences:")
    print()

    for n, s in enumerate(sentences, 1):
        print(f"{n}. {s}")
    
    # Display the total number sentences in the paragraph
    print(f"\nTotal number of sentences: {len(sentences)}")


# Define the split_sentences function
def split_sentences(paragraph):

    # Create the pattern to split the paragraph.
    pattern = r'(?<=[.!?])\s+(?=[A-Z0-9])'

    # Return the paragraph as a list of split sentences.
    return re.split(pattern, paragraph)

# Run the main function
main()