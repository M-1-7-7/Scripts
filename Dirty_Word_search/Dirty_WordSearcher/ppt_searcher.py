from pptx import Presentation
import os
from pptx.exc import PackageNotFoundError

def find_powerpoint_files(directory):
    powerpoint_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.ppt', '.pptx')):
                powerpoint_files.append(os.path.join(root, file))
    return powerpoint_files

Dirty_words = []
with open('Dity_word.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        Dirty_words.append(line.strip())

computer_root = "C:\\"  
powerpoint_files = find_powerpoint_files(computer_root)

for powerpoint_file in powerpoint_files:
    try:
        prs = Presentation(powerpoint_file)
        for word in Dirty_words:
            for slide in prs.slides:
                for shape in slide.shapes:
                    if hasattr(shape, "text"):
                        shape_text = shape.text.lower()
                        if word.lower() in shape_text:
                            print(f"File: {powerpoint_file} - Contains dirty word: {word}")
                            break  
    except PermissionError as e:
        if 'Package not found' not in str(e):
            print(f"Insufficient system privileges to read contents of {powerpoint_file}")
    except PackageNotFoundError as e:
        # Handle PackageNotFoundError gracefully
        pass  # Do nothing or print a custom message if needed
    except Exception as e:
        print(f"Error processing {powerpoint_file}: {e}")
