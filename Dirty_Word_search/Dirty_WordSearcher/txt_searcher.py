import os

# Function to search for text files recursively in a directory
def find_text_files(directory):
    text_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.txt'):
                text_files.append(os.path.join(root, file))
    return text_files

# Function to load dirty words from file
def load_dirty_words(file_path):
    dirty_words = []
    with open(file_path, 'r', encoding='utf-8') as file:  # Specify the encoding here
        for line in file:
            dirty_words.append(line.strip())
    return dirty_words

# Search for text files on the entire computer
computer_root = "C:\\"  # Change this to the root directory of your computer
text_files = find_text_files(computer_root)

# Load dirty words from file
dirty_words_file = 'Dity_word.txt'  # Adjust this to the path of your dirty words file
dirty_words = load_dirty_words(dirty_words_file)

# Perform search in text files
for text_file in text_files:
    try:
        with open(text_file, 'r', encoding='utf-8') as file:  # Specify the encoding here
            for line_num, line in enumerate(file, start=1):
                words_in_line = line.strip().split()
                for word in dirty_words:
                    # Check if word matches exactly the length specified
                    if any(len(word) == len(w) and word.lower() == w.lower() for w in words_in_line):
                        print(f"File: {text_file} - Line: {line_num} - Contains dirty word: {word}")
    except Exception as e:
        pass
