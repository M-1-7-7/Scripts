import os
import re
from collections import defaultdict

# Function to find text files
def find_text_files(directory):
    """
    This function finds all text files (files with .txt extension)
    within the specified directory and its subdirectories.

    Args:
        directory (str): Path to the directory to search.

    Returns:
        list: List containing the full paths to all text files found.
    """
    text_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.txt'):
                text_files.append(os.path.join(root, file))
    return text_files

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

text_files = find_text_files(computer_root)

# Dictionary to store findings for summary
findings_summary = defaultdict(lambda: defaultdict(int))

def read_file(file_path):
    """
    Attempt to read a file with multiple encodings.
    
    Args:
        file_path (str): Path to the file to read.

    Returns:
        str: Decoded file content, or None if decoding fails.
    """
    encodings = ['utf-8', 'latin-1', 'ISO-8859-1']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read().lower()
        except UnicodeDecodeError:
            continue
    return None

def process_text_file(file_path):
    """
    Process text files to find dirty words.

    Args:
        file_path (str): Path to the text file to process.
    """
    try:
        file_text = read_file(file_path)
        if file_text is None:
            print(f"Error: Could not decode {file_path}")
            return
        for word in dirty_words:
            word_pattern = r'\b' + re.escape(word) + r'\b'
            matches = re.findall(word_pattern, file_text)
            if matches:
                findings_summary[(file_path, 'Text')][word] += len(matches)
    except FileNotFoundError:
        print(f"Error: File not found {file_path}")
    except PermissionError:
        print(f"Permission error processing {file_path}")
    except Exception as e:
        print(f"Unexpected error processing {file_path}: {e}")

for text_file in text_files:
    process_text_file(text_file)

# Print summary of findings
for (file, source), words in findings_summary.items():
    words_summary = ', '.join([f"{word}: {count}" for word, count in words.items()])
    print(f"File: {file} - {source} - Contains dirty words - {words_summary}")
