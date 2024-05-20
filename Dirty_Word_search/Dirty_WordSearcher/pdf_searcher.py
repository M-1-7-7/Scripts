import os
import re
import PyPDF2
from collections import defaultdict

# Function to find PDF files
def find_pdf_files(directory):
    """
    This function finds all PDF files within the specified directory and its subdirectories.

    Args:
        directory (str): Path to the directory to search.

    Returns:
        list: List containing the full paths to all PDF files found.
    """
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

# Function to load dirty words from file
def load_dirty_words(filename):
    """
    This function loads dirty words from a text file, removing any leading/trailing spaces
    and handling empty lines or an empty file gracefully.

    Args:
        filename (str): Path to the text file containing dirty words.

    Returns:
        list: List of cleaned dirty words (no leading/trailing spaces) or an empty list
              if the file is empty or contains only empty lines.
    """
    dirty_words = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Remove leading/trailing spaces and add to list (if not empty)
                cleaned_word = line.strip()
                if cleaned_word:
                    dirty_words.append(cleaned_word.lower())
    except FileNotFoundError:
        print("Error: 'Dirty_word.txt' not found. Please ensure the file exists.")
    return dirty_words

# Load Dirty Words file
dirty_words = load_dirty_words('Dirty_word.txt')
if not dirty_words:
    print("Warning: 'Dirty_word.txt' is empty or contains only empty lines. No dirty words found.")

# Specify directory path (consider user input or relative paths)
computer_root = "C:\\"  # Replace with desired directory

pdf_files = find_pdf_files(computer_root)

# Dictionary to store findings for summary
findings_summary = defaultdict(lambda: defaultdict(int))

def process_pdf_file(file_path):
    """
    Process PDF files to find dirty words.

    Args:
        file_path (str): Path to the PDF file to process.
    """
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                page_text = page.extract_text().lower()
                for word in dirty_words:
                    word_pattern = r'\b' + re.escape(word) + r'\b'
                    matches = re.findall(word_pattern, page_text)
                    if matches:
                        for match in matches:
                            findings_summary[file_path][word] += 1
    except PyPDF2.errors.PdfReadError:
        print(f"Error: Could not read, password protected? {file_path}")
    except FileNotFoundError:
        print(f"Error: File not found {file_path}")
    except PermissionError:
        print(f"Permission error processing {file_path}")
    except Exception as e:
        print(f"Unexpected error processing {file_path}: {e}")

for pdf_file in pdf_files:
    process_pdf_file(pdf_file)

# Print summary of findings
for file_path, words in findings_summary.items():
    words_summary = ', '.join([f"{word}: {count}" for word, count in words.items()])
    print(f"File: {file_path} - Contains dirty words - {words_summary}")
