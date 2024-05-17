import os
from pptx import Presentation
from pptx.exc import PackageNotFoundError

# Function to find PowerPoint files
def find_powerpoint_files(directory):
  """
  This function finds all PowerPoint presentations (files with .ppt or .pptx extensions)
  within the specified directory and its subdirectories.

  Args:
      directory (str): Path to the directory to search.

  Returns:
      list: List containing the full paths to all PowerPoint presentations found.
  """
  powerpoint_files = []
  for root, dirs, files in os.walk(directory):
    for file in files:
      if file.lower().endswith(('.ppt', '.pptx')):
        powerpoint_files.append(os.path.join(root, file))
  return powerpoint_files

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
    print("Error: 'Dity_word.txt' not found. Please ensure the file exists.")
  return dirty_words

# Load Dirty Words file
dirty_words = load_dirty_words('Dity_word.txt')
if not dirty_words:
  print("Warning: 'Dity_word.txt' is empty or contains only empty lines. No dirty words found.")

# Specify directory path (consider user input or relative paths)
computer_root = "C:\\"  # Replace with desired directory

powerpoint_files = find_powerpoint_files(computer_root)
print(dirty_words)
for powerpoint_file in powerpoint_files:
  try:
    prs = Presentation(powerpoint_file)

    slide_number = 1  # Keep track of slide number (starts from 1)
    for slide in prs.slides:
      for shape in slide.shapes:
        if hasattr(shape, "text"):
          shape_text = shape.text.lower()
          for word in dirty_words:
            if word in shape_text and len(shape_text.split()) >= len(word):
              start_index = shape_text.find(word)
              end_index = start_index + len(word)
              if (start_index == 0 or shape_text[start_index-1].isspace()) and \
                 (end_index == len(shape_text) or shape_text[end_index].isspace()):
                print(f"File: {powerpoint_file} - Slide: {slide_number} - Contains dirty word: {word}")
                break  # Exit inner loop after finding a match
      slide_number += 1  # Increment slide number for the next slide

  except PermissionError as e:
    if 'Package not found' not in str(e):
      print(f"Insufficient system privileges to read contents of {powerpoint_file}")
  except PackageNotFoundError:
    print(f"Insufficient system privileges to read contents of {powerpoint_file}")
  except Exception as e:
    print(f"Error processing {powerpoint_file}: {e}")
