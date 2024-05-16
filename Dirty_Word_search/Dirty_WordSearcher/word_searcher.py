import os
import sys
from spire.doc import *
from spire.doc.common import *

class find_Word_documents():
    #user input variables from GUI
    dirty_words_txt = sys.argv[1]
    input_directory = sys.argv[2]
    output_directory = sys.argv[3]
    new_out_dir = output_directory + "\RESULTS\\"

    # Function to search for Word files recursively in a directory
    def find_word_files(directory):
        word_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith('.doc') or file.lower().endswith('.docx'):
                    word_files.append(os.path.join(root, file))
        return word_files

    # Function to load dirty words from file
    def load_dirty_words(file_path):
        dirty_words = []
        with open(file_path, 'r') as file:
            for line in file:
                dirty_words.append(line.strip())
        return dirty_words
    
    # Create Positive folder if it doesn't exist
    if not os.path.exists(new_out_dir):
        os.makedirs(new_out_dir)

    # Get a list of Word files in the input directory
    word_files = find_word_files(input_directory)

    # Create Dirty Word list from the dirty word input file from user
    dirty_words = load_dirty_words(dirty_words_txt)


    # Process each Word file
    for eachfile in word_files:
        # Create an object of the Document class
        document = Document()
        # Load a Word document
        document.LoadFromFile(eachfile)
        # Find all instances of specific text
        for word in dirty_words:
            textSelections = document.FindAllString(word, False, True)
            # Loop through all the instances
            for selection in textSelections:
                # Get the current instance as a single text range
                textRange = selection.GetAsOneRange()
                # Highlight the text range with a color
                textRange.CharacterFormat.HighlightColor = Color.get_Yellow()
                # Save the modified document
                output_file = os.path.join(new_out_dir, "POSITIVE - " + os.path.basename(eachfile))
                document.SaveToFile(output_file, FileFormat.Docx2016)
        # Close the document
        document.Close()

if __name__ == "__main__":
    find_Word_documents()
