import os
from spire.doc import *
from spire.doc.common import *

# Function to search for Word files recursively in a directory
def find_word_files(directory):
    word_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.doc') or file.lower().endswith('.docx'):
                word_files.append(os.path.join(root, file))
    return word_files

# Specify the input and output directory paths
input_directory = "C:\\"
output_directory = "C:\\PATH\\TO\\OUTPUT\\DIRECTORY"

# Create Positive folder if it doesn't exist
positive_folder = os.path.join(output_directory)
if not os.path.exists(positive_folder):
    os.makedirs(positive_folder)

# Get a list of Word files in the input directory
word_files = find_word_files(input_directory)

# Create Dirty Word list from the dirty word input file from user
Dirty_words = []
with open('Dity_word.txt', 'r') as file:
    lines = file.readlines()
    for i in lines:
        Dirty_words.append(i.strip())

# Process each Word file
for eachfile in word_files:
    # Create an object of the Document class
    document = Document()
    # Load a Word document
    document.LoadFromFile(eachfile)
    # Find all instances of specific text
    for word in Dirty_words:
        textSelections = document.FindAllString(word, False, True)
        # Loop through all the instances
        for selection in textSelections:
            # Get the current instance as a single text range
            textRange = selection.GetAsOneRange()
            # Highlight the text range with a color
            textRange.CharacterFormat.HighlightColor = Color.get_Yellow()
    # Save the modified document
    output_file = os.path.join(positive_folder, "POSITIVE - " + os.path.basename(eachfile))
    document.SaveToFile(output_file, FileFormat.Docx2016)
    # Close the document
    document.Close()
