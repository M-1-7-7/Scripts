from pptx import Presentation
import os
from pptx.exc import PackageNotFoundError
import sys

class ppt_finder():
    #user input variables from GUI
    dirty_words_txt = sys.argv[1]
    input_directory = sys.argv[2]
    output_directory = sys.argv[3]
    
    positive_output_file = output_directory + "Positive_Powerpoint_Results.txt"
    not_analysed_output_file = output_directory + "Cannot_Anayse_Powerpoint_List.txt"  
    def find_powerpoint_files(directory):
        powerpoint_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(('.ppt', '.pptx')):
                    powerpoint_files.append(os.path.join(root, file))
        return powerpoint_files

    Dirty_words = []
    with open(dirty_words_txt, 'r') as file:
        lines = file.readlines()
        for line in lines:
            Dirty_words.append(line.strip())

    powerpoint_files = find_powerpoint_files(input_directory)

    #create output directories for results
    if not os.path.exists(positive_output_file):
        with open(positive_output_file, "w") as file:
            file.write("THESE FILES HAVE ALL RETURNED A POSITIVE HIT\n------------\n------------\n")

    if not os.path.exists(not_analysed_output_file):
        with open(not_analysed_output_file, "w") as file:
            file.write("THIS FILE WHERE NOT ABLE TO BE ANALYSED BY THE SCRIPT\n------------\n------------\n")

    for powerpoint_file in powerpoint_files:
        try:
            prs = Presentation(powerpoint_file)
            for word in Dirty_words:
                for slide in prs.slides:
                    for shape in slide.shapes:
                        if hasattr(shape, "text"):
                            shape_text = shape.text.lower()
                            if word.lower() in shape_text:
                                pos_string = f"File: {powerpoint_file} - Contains dirty word: {word}"
                                with open(positive_output_file, "a") as file:
                                    file.write(pos_string + "\n")
                                break  
        except PermissionError as e:
            if 'Package not found' not in str(e):
                not_string = f"Insufficient system privileges to read contents of {powerpoint_file}"
                with open(not_analysed_output_file, "a") as file:
                    file.write(not_string + "\n")
        except PackageNotFoundError as e:
            pass  
        except Exception as e:
            not_string = f"Error processing {powerpoint_file}: {e}"
            with open(not_analysed_output_file, "a") as file:
                file.write(not_string + "\n")
            

if __name__ == "__main__":
    ppt_finder()
