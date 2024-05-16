import os
import PyPDF2 

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
with open('Dity_word.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        Dirty_words.append(line.strip())

# Search for PDF files on the entire computer
computer_root = "C:\\"  # Change this to the root directory of your computer
pdf_files = find_pdf_files(computer_root)

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
                        print(f"File: {pdf_file} - Page: {page_num} - Contains dirty word: {word}")
                        break  # Move to the next word after finding the first dirty word
    except Exception as e:
        print(f"Error processing {pdf_file}: {e}")
