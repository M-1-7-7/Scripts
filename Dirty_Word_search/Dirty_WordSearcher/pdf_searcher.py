import os
import PyPDF2 
from datetime import datetime
import sys

class pdf_finder(): 
    #user input variables from GUI
    dirty_words_txt = sys.argv[1]
    input_directory = sys.argv[2]
    output_directory = sys.argv[3]
    positive_output_file = output_directory + "Positive_PDF_Results.txt"
    not_analysed_output_file = output_directory + "Cannot_Anayse_PDF_List.txt"  

    # Function to search for PDF files recursively in a directory
    def find_pdf_files(directory):
        pdf_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith('.pdf'):
                    pdf_files.append(os.path.join(root, file))
        return pdf_files

    # Load dirty words from file
    Dirty_words = []
    with open(dirty_words_txt, 'r') as file:
        lines = file.readlines()
        for line in lines:
            Dirty_words.append(line.strip())

    # Search for PDF files on the entire computer
    #computer_root = "C:\\"  # Change this to the root directory of your computer
    pdf_files = find_pdf_files(input_directory)

    #create output directories for results
    if not os.path.exists(positive_output_file):
        with open(positive_output_file, "w") as file:
            file.write("THESE FILES HAVE ALL RETURNED A POSITIVE HIT\n------------\n------------\n")

    if not os.path.exists(not_analysed_output_file):
        with open(not_analysed_output_file, "w") as file:
            file.write("THIS FILE WHERE NOT ABLE TO BE ANALYSED BY THE SCRIPT\n------------\n------------\n")

    # Perform search in PDF files
    for pdf_file in pdf_files:
        try:
            # Open the PDF file
            reader = PyPDF2.PdfReader(pdf_file)
            # Iterate over each page and extract text
            for page_num, page in enumerate(reader.pages, start=1):
                text = page.extract_text()
                # Split text into words and search for dirty words
                words = text.split()
                for word in Dirty_words:
                    for text_word in words:
                        if len(word) == len(text_word) and word.lower() == text_word.lower():
                            pos_string = f"File: {pdf_file} - Page: {page_num} - Contains dirty word: {word}"
                            #print(f"File: {pdf_file} - Page: {page_num} - Contains dirty word: {word}")
                            with open(positive_output_file, "a") as file:
                                file.write(pos_string + "\n")
                            break  # Move to the next word after finding the first dirty word
        except Exception as e:
            not_string = f"Error processing {pdf_file}: {e}"
            with open(not_analysed_output_file, "a") as file:
                file.write(not_string + "\n")

if __name__ == "__main__":
    pdf_finder()
