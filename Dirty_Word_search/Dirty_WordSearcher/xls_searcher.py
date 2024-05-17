import os
import openpyxl

# pip install openpyxl

# Function to search for Excel files recursively in a directory
def find_excel_files(directory):
    excel_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.xlsx'):
                excel_files.append(os.path.join(root, file))
    return excel_files

# Function to load dirty words from file
def load_dirty_words(file_path):
    dirty_words = []
    with open(file_path, 'r') as file:
        for line in file:
            dirty_words.append(line.strip())
    return dirty_words

# Search for Excel files on the entire computer
computer_root = "C:\\"  # Change this to the root directory of your computer
excel_files = find_excel_files(computer_root)

# Load dirty words from file
dirty_words_file = 'Dity_word.txt'  # Adjust this to the path of your dirty words file
dirty_words = load_dirty_words(dirty_words_file)

# Perform search in Excel files
for excel_file in excel_files:
    try:
        wb = openpyxl.load_workbook(excel_file)
        # Iterate over each sheet in the workbook
        for sheet_name in wb.sheetnames:
            sheet = wb[sheet_name]
            # Iterate over each cell in the sheet
            for row in sheet.iter_rows():
                for cell in row:
                    if cell.value is not None and isinstance(cell.value, str):
                        # Split the cell contents into words
                        words = cell.value.lower().split()
                        # Search for dirty words in the split words
                        for word in words:
                            if word in dirty_words:
                                print(f"File: {excel_file} - Sheet: {sheet_name} - Cell: {cell.coordinate} - Contains dirty word: {word}")
    except Exception as e:
        print(f"Error processing {excel_file}: {e}")
