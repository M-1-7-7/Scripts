# import packages
import PyPDF2
import re

files = ["Industry-Placement-Form.pdf"]


#Create Dirty Word list from the dirty word input file from user
Dirty_words = []
with open('Dity_word.txt', 'r') as file:
    lines = file.readlines()
    for i in lines:
        Dirty_words.append(i.strip())

# extract text and do the search
for file in files:
    # open the pdf file
    reader = PyPDF2.PdfReader(file)
    # get number of pages
    num_pages = len(reader.pages)
    for page in reader.pages:
        text = page.extract_text() 
        # print(text)
        for word in Dirty_words:
            if word.lower() in text.lower():
                print(file, " : CONTAINS : ", word)
                print("----------------------")
        break
