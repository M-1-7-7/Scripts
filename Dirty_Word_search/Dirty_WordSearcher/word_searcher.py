from spire.doc import *
from spire.doc.common import *

# Specify the input and output file paths
files = ["Word_files\\WiFi Considerations - LO2.8.docx"] 

#Create Dirty Word list from the dirty word input file from user
Dirty_words = []
with open('Dity_word.txt', 'r') as file:
    lines = file.readlines()
    for i in lines:
        Dirty_words.append(i.strip())

# Create an object of the Document class
document = Document()

# Load a Word document
for eachfile in files:
    document.LoadFromFile(eachfile)
    # Find all instances of a specific text
    for words in Dirty_words:
        textSelections = document.FindAllString(words, False, True)
        # Loop through all the instances
        for selection in textSelections:
            # Get the current instance as a single text range
            textRange = selection.GetAsOneRange()
            # Highlight the text range with a color
            textRange.CharacterFormat.HighlightColor = Color.get_Yellow()
            outputFile = "POSITIVE - " + eachfile
            document.SaveToFile(outputFile, FileFormat.Docx2016)

# Save the resulting document
document.Close()
