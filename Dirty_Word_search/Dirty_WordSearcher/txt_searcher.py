import os
import sys

# Function to search for text files recursively in a directory
class txt_finder():
    #user input variables from GUI
    dirty_words_txt = sys.argv[1]
    input_directory = sys.argv[2]
    output_directory = sys.argv[3]
    positive_output_file = output_directory + "Positive_TXT_Results.txt"
    not_analysed_output_file = output_directory + "Cannot_Anayse_TXT_List.txt"  

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
    text_files = find_text_files(input_directory)

    # Load dirty words from file
    dirty_words = load_dirty_words(dirty_words_txt)

    #create output directories for results
    if not os.path.exists(positive_output_file):
        with open(positive_output_file, "w") as file:
            file.write("THESE FILES HAVE ALL RETURNED A POSITIVE HIT\n------------\n------------\n")

    if not os.path.exists(not_analysed_output_file):
        with open(not_analysed_output_file, "w") as file:
            file.write("THIS FILE WHERE NOT ABLE TO BE ANALYSED BY THE SCRIPT\n------------\n------------\n")

    # Perform search in text files
    for text_file in text_files:
        try:
            with open(text_file, 'r', encoding='utf-8') as file:  # Specify the encoding here
                for line_num, line in enumerate(file, start=1):
                    words_in_line = line.strip().split()
                    for word in dirty_words:
                        # Check if word matches exactly the length specified
                        if any(len(word) == len(w) and word.lower() == w.lower() for w in words_in_line):
                            pos_string = f"File: {text_file} - Line: {line_num} - Contains dirty word: {word}"
                            #print(f"File: {pdf_file} - Page: {page_num} - Contains dirty word: {word}")
                            with open(positive_output_file, "a") as file:
                                file.write(pos_string + "\n")
                            print()
        except Exception as e:
            not_string = f"Error processing {text_file}: {e}"
            with open(not_analysed_output_file, "a") as file:
                file.write(not_string + "\n")
            

while __name__ == "__main__":
    txt_finder()
