import subprocess
import PyPDF2 
import os

import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from spire.doc import *
from spire.doc.common import *
from pptx import Presentation
from pptx.exc import PackageNotFoundError
from datetime import datetime
# Window Configuration
root = Tk()
root.geometry("800x600")
root.title("Dirty Word Searcher")
frm = ttk.Frame(root, padding=10)
frm.grid()
# user input variriables
DW_Var=tkinter.StringVar()
start_dir_Var=tkinter.StringVar()
out_dir_Var=tkinter.StringVar()
dirty_words_txt = DW_Var.get()
begin_search_dir = start_dir_Var.get()
output_search_dir = out_dir_Var.get()
# buttons states
Excel_Button_Val = IntVar() 
PDF_Button_Val = IntVar() 
PowerPoint_Button_Val = IntVar() 
Doc_Button_Val = IntVar() 
TXT_Button_Val = IntVar() 
All_Other_Type_Button_Val = IntVar()
All_Document_Type_Button_Val = IntVar() 
# Other variables
script_directory = os.path.dirname(os.path.abspath(__file__)) 

# Functions that will execute specificly to the checkboxes ticked by the user
def scan_all_docs():
    print("Scanning all docs")
    scan_excel_doc()
    scan_pdf_doc()
    scan_powerpoint_doc()
    scan_word_doc()
    scan_txt_doc()
    find_all_other_files()
    
def scan_excel_doc():
    print("Scanning excel docs")
    #user input variables from GUI
    positive_output_file = out_dir_Var.get() + "Positive_TXT_Results.out"
    not_analysed_output_file = out_dir_Var.get() + "Cannot_Anayse_TXT_List.out"  

    def find_text_files(directory):
        text_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith('.txt'):
                    text_files.append(os.path.join(root, file))
        return text_files

    #Create Dirty Word list from the dirty word input file from user
    Dirty_words = []
    with open(DW_Var.get(), 'r') as file:
        lines = file.readlines()
        for i in lines:
            Dirty_words.append(i.strip())

    # Search for text files on the entire computer
    text_files = find_text_files(start_dir_Var.get())

    # Load dirty words from file

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
                    for word in Dirty_words:
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
    
    print("On to the next")

def scan_pdf_doc():
    print("Scanning pdf docs")
    positive_output_file = out_dir_Var.get() + "Positive_PDF_Results.out"
    not_analysed_output_file = out_dir_Var.get() + "Cannot_Anayse_PDF_List.out"  

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
    with open(DW_Var.get(), 'r') as file:
        lines = file.readlines()
        for line in lines:
            Dirty_words.append(line.strip())

    # Search for PDF files on the entire computer
    #computer_root = "C:\\"  # Change this to the root directory of your computer
    pdf_files = find_pdf_files(start_dir_Var.get())

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

    print("On to the next")

def scan_powerpoint_doc():
    positive_output_file = out_dir_Var.get() + "Positive_Powerpoint_Results.out"
    not_analysed_output_file = out_dir_Var.get() + "Cannot_Anayse_Powerpoint_List.out"  
    def find_powerpoint_files(directory):
        powerpoint_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(('.ppt', '.pptx')):
                    powerpoint_files.append(os.path.join(root, file))
        return powerpoint_files

    Dirty_words = []
    with open(DW_Var.get(), 'r') as file:
        lines = file.readlines()
        for line in lines:
            Dirty_words.append(line.strip())

    powerpoint_files = find_powerpoint_files(start_dir_Var.get())

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

def scan_word_doc():
    #script_loc = script_directory + "\\word_searcher.py"
    print("Scanning word docs")
    #user input variables from GUI
    new_out_dir = out_dir_Var.get() + "\\RESULTS\\"

    # Function to search for Word files recursively in a directory
    def find_word_files(directory):
        word_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith('.doc') or file.lower().endswith('.docx'):
                    word_files.append(os.path.join(root, file))
        return word_files

    #Create Dirty Word list from the dirty word input file from user
    Dirty_words = []
    with open(DW_Var.get(), 'r') as file:
        lines = file.readlines()
        for i in lines:
            Dirty_words.append(i.strip())
    
    # Create Positive folder if it doesn't exist
    if not os.path.exists(new_out_dir):
        os.makedirs(new_out_dir)

    # Get a list of Word files in the input directory
    word_files = find_word_files(start_dir_Var.get())

    # Process each Word file
    for eachfile in word_files:
        # Create an object of the Document class
        document = Document()
        # Load a Word document
        document.LoadFromFile(eachfile)
        # Find all instances of specific text
        for word in Dirty_words:
            textSelections = document.FindAllString(word, False, True)
            # Loop through all the instances
            for selection in textSelections:
                # Get the current instance as a single text range
                textRange = selection.GetAsOneRange()
                # Highlight the text range with a color
                textRange.CharacterFormat.HighlightColor = Color.get_Yellow()
                # Save the modified document
                output_file = os.path.join(new_out_dir, "POSITIVE - " + os.path.basename(eachfile))
                document.SaveToFile(output_file)
        # Close the document
        document.Close()
    print("finished scan")

def scan_txt_doc():
    script_loc = script_directory + "\\txt_searcher.py"
    print("scanning txt docs")
    subprocess.run(["python", script_loc, DW_Var.get(), start_dir_Var.get(), out_dir_Var.get()])
    print("On to the next")

def find_all_other_files():
    positive_output_file = out_dir_Var.get() + "\\RESULTS\\"
    start_dir = start_dir_Var.get()
    print("finding all other files")
    # Lists for all the file types
    list_of_lists = {
    "jpeg": [], 
    "png": [],
    "bmp": [],
    "tiff": [],
    "mp3": [],
    "mp4": [],
    "avi": [],
    "mov": [],
    "msg": []
    }

    interesting_extensions = [".jpeg", ".png", ".bmp", ".tiff", ".mp3", ".mp4", ".avi", ".mov", ".msg"]
    
    for i in interesting_extensions:
        #positive_output_file = positive_output_file + i + "_Files_Found.out"
        targer_array = i.replace(".", "")
        #if not os.path.exists(positive_output_file):
            #with open(positive_output_file, "w") as file:
                #file.write("THESE FILES HAVE BEEN FOUND\n------------\n------------\n")
        for root, dirs, files in os.walk(start_dir):
            for file in files:
                if file.lower().endswith(i):
                    file_found = os.path.join(root, file)
                    list_of_lists[targer_array].append(file_found)

    if len(list_of_lists["jpeg"]) > 1:
        file_list = positive_output_file + "jpegs_found.out"
        if not os.path.exists(file_list):
            with open(file_list, "w") as file:
                file.write("THESE FILES HAVE BEEN FOUND\n------------\n------------\n")

        for i in list_of_lists["jpeg"]:
            with open(file_list, "a") as file:
                    file.write(i + "\n")

    if len(list_of_lists["png"]) > 1:
        file_list = positive_output_file + "png_found.out"
        if not os.path.exists(file_list):
            with open(file_list, "w") as file:
                file.write("THESE FILES HAVE BEEN FOUND\n------------\n------------\n")

        for i in list_of_lists["png"]:
            with open(file_list, "a") as file:
                    file.write(i + "\n")

    if len(list_of_lists["bmp"]) > 1:
        file_list = positive_output_file + "bmp_found.out"
        if not os.path.exists(file_list):
            with open(file_list, "w") as file:
                file.write("THESE FILES HAVE BEEN FOUND\n------------\n------------\n")

        for i in list_of_lists["bmp"]:
            with open(file_list, "a") as file:
                    file.write(i + "\n")
    
    if len(list_of_lists["tiff"]) > 1:
        file_list = positive_output_file + "tiff_found.out"
        if not os.path.exists(file_list):
            with open(file_list, "w") as file:
                file.write("THESE FILES HAVE BEEN FOUND\n------------\n------------\n")

        for i in list_of_lists["tiff"]:
            with open(file_list, "a") as file:
                    file.write(i + "\n")

    if len(list_of_lists["mp3"]) > 1:
        file_list = positive_output_file + "mp3_found.out"
        if not os.path.exists(file_list):
            with open(file_list, "w") as file:
                file.write("THESE FILES HAVE BEEN FOUND\n------------\n------------\n")

        for i in list_of_lists["mp3"]:
            with open(file_list, "a") as file:
                    file.write(i + "\n")
    
    if len(list_of_lists["mp4"]) > 1:
        file_list = positive_output_file + "mp4_found.out"
        if not os.path.exists(file_list):
            with open(file_list, "w") as file:
                file.write("THESE FILES HAVE BEEN FOUND\n------------\n------------\n")

        for i in list_of_lists["mp4"]:
            with open(file_list, "a") as file:
                    file.write(i + "\n")
    
    if len(list_of_lists["avi"]) > 1:
        file_list = positive_output_file + "avi_found.out"
        if not os.path.exists(file_list):
            with open(file_list, "w") as file:
                file.write("THESE FILES HAVE BEEN FOUND\n------------\n------------\n")

        for i in list_of_lists["avi"]:
            with open(file_list, "a") as file:
                    file.write(i + "\n")

    if len(list_of_lists["mov"]) > 1:
        file_list = positive_output_file + "mov_found.out"
        if not os.path.exists(file_list):
            with open(file_list, "w") as file:
                file.write("THESE FILES HAVE BEEN FOUND\n------------\n------------\n")

        for i in list_of_lists["mov"]:
            with open(file_list, "a") as file:
                    file.write(i + "\n")
    
    if len(list_of_lists["msg"]) > 1:
        file_list = positive_output_file + "msg_found.out"
        if not os.path.exists(file_list):
            with open(file_list, "w") as file:
                file.write("THESE FILES HAVE BEEN FOUND\n------------\n------------\n")

        for i in list_of_lists["msg"]:
            with open(file_list, "a") as file:
                    file.write(i + "\n")

    print("On to the next")

# Functions from GUI Buttons
def search_files():
    # Ensure the files and Dirs entered by user are going to work
    if All_Document_Type_Button_Val.get() == 1:
        print("Scanning all docs")
        scan_excel_doc()
        scan_pdf_doc()
        scan_powerpoint_doc()
        scan_word_doc()
        scan_txt_doc()

    elif All_Document_Type_Button_Val.get() == 0:
        if Excel_Button_Val.get() == 1:
            scan_excel_doc()

        if PDF_Button_Val.get() == 1:
            scan_pdf_doc()

        if PowerPoint_Button_Val.get() == 1:
            scan_powerpoint_doc()

        if Doc_Button_Val.get() == 1:
            scan_word_doc()

        if TXT_Button_Val.get() == 1:
            scan_txt_doc()

        if All_Other_Type_Button_Val.get() == 1:
            find_all_other_files()

# Validate user selections and inputs 
def check_checkboxes():
    if All_Document_Type_Button_Val.get() == 0 and PDF_Button_Val.get() == 0 and PowerPoint_Button_Val.get() == 0 and Doc_Button_Val.get() == 0 and TXT_Button_Val.get() == 0 and Excel_Button_Val.get() == 0:
        messagebox.showerror("Checkbox Status", "please check at least one checkbox")
        main_screen()
    else:
        search_files()

def check_user_input():
    user_input_bad = ""
    # check if directory exists
    if not os.path.exists(start_dir_Var.get()): 
        user_input_bad += "!!!Please enter a valid STARTING DIRECTORY!!!\n"
    else:
        print("starting directory is existing :)\n")

    if not os.path.exists(out_dir_Var.get()): 
        user_input_bad += "!!!Please enter a valid OUTPUT DIRECTORY!!!\n"
    else:
       print("Output directory is existing :)\n")

    # Check if the file is writable using os.access()
    if DW_Var.get().endswith('.txt'):
        if os.access(DW_Var.get(), os.W_OK):
            print(f"File '{DW_Var.get()}' is writable.") 
        elif FileNotFoundError:
            user_input_bad += "!!!Dirty Word File NOT FOUND!!!\n"
        elif PermissionError:
            user_input_bad += "!!!Please enter a valid FILE WHERE PROGRAM HAS PERMISIONS!!!\n"
    else:
        user_input_bad += "!!!Please enter a valid TXT FILE!!!\n"

    if len(user_input_bad) > 0:
        messagebox.showerror("Your Input Status", user_input_bad)
    else:
        check_checkboxes()

#reset values on the window
def reset_values():
    print("Resetting")
    DW_Var.set("")
    start_dir_Var.set("")
    out_dir_Var.set("")
    Excel_Button_Val.set(0) 
    PDF_Button_Val.set(0) 
    PowerPoint_Button_Val.set(0) 
    Doc_Button_Val.set(0) 
    TXT_Button_Val.set(0) 
    All_Document_Type_Button_Val.set(0) 

# Main Screen
def main_screen():
    title = ttk.Label(frm, text="WELCOME TO DIRTY WORD SEARCHER!!!! :)")
    # User input fields
    DW_label = ttk.Label(frm, text = "Dirty Word Text file: ")
    DW_entry = ttk.Entry(frm, textvariable = DW_Var)
    start_dir_label = ttk.Label(frm, text = "Starting Directory for your search : ")
    start_dir_entry = ttk.Entry(frm, textvariable = start_dir_Var)
    out_dir_label = ttk.Label(frm, text = "Output Directory for your results : ")
    out_dir_entry = ttk.Entry(frm, textvariable = out_dir_Var)
    # Radio Buttons for file types

    # Function Buttons
    #show_doc_results = ttk.Button(frm, text="Show Doc Results", command=)
    #show_pptx_results = ttk.Button(frm, text="Show pptx Results", command=)
    #show_pdf_results = ttk.Button(frm, text="Show pdf Results", command=)
    #show_xls_results = ttk.Button(frm, text="Show xls Results", command=)
    search_btn = ttk.Button(frm, text="Search", command=search_files)
    reset_btn = ttk.Button(frm, text="Reset", command=reset_values)
    quit_btn = ttk.Button(frm, text="Quit", command=root.destroy)

    All_Excel_Button = Checkbutton(root, text = "All EXCEL Docs", 
                        variable = Excel_Button_Val, 
                        onvalue = 1, 
                        offvalue = 0, 
                        height = 2, 
                        width = 20) 
                                              
    All_PDF_Button = Checkbutton(root, text = "All PDF Docs", 
                        variable = PDF_Button_Val, 
                        onvalue = 1, 
                        offvalue = 0, 
                        height = 2, 
                        width = 20) 
                                                     
    All_PowerPoint_Button = Checkbutton(root, text = "All PowerPoint Docs", 
                        variable = PowerPoint_Button_Val, 
                        onvalue = 1, 
                        offvalue = 0, 
                        height = 2, 
                        width = 20) 
                                               
    All_Word_Button = Checkbutton(root, text = "All Word Docs", 
                        variable = Doc_Button_Val, 
                        onvalue = 1, 
                        offvalue = 0, 
                        height = 2, 
                        width = 20) 
                                              
    All_TXT_Button = Checkbutton(root, text = "All TXT Docs", 
                        variable = TXT_Button_Val, 
                        onvalue = 1, 
                        offvalue = 0, 
                        height = 2, 
                        width = 20) 

    All_Documet_Type_Button = Checkbutton(root, text = "All Document Types", 
                        variable = All_Document_Type_Button_Val, 
                        onvalue = 1, 
                        offvalue = 0, 
                        height = 2, 
                        width = 20) 
    All_Other_Type_Button = Checkbutton(root, text = "All Other Types", 
                        variable = All_Other_Type_Button_Val, 
                        onvalue = 1, 
                        offvalue = 0, 
                        height = 2, 
                        width = 20) 
    
   
    # Placement of elements on frame
    title.grid(column=0, row=0)

    DW_label.grid(column=0, row=3, sticky=E)
    DW_entry.grid(column=1, row=3, columnspan=4)
    start_dir_label.grid(column=0, row=4, sticky=E)
    start_dir_entry.grid(column=1, row=4, columnspan=4)
    out_dir_label.grid(column=0, row=5, sticky=E)
    out_dir_entry.grid(column=1, row=5, columnspan=4)
    
    All_Excel_Button.grid(row=2, sticky=W)
    All_PDF_Button.grid(row=3, sticky=W)
    All_PowerPoint_Button.grid(row=4, sticky=W)
    All_Word_Button.grid(row=5, sticky=W)
    All_TXT_Button.grid(row=6, sticky=W)
    All_Documet_Type_Button.grid(row=7, sticky=W)
    All_Other_Type_Button.grid(row=8, sticky=W)

    search_btn.grid(column=8, row=10)
    reset_btn.grid(column=9, row=10)
    quit_btn.grid(column=10, row=10)

    root.mainloop()
    
if __name__ == "__main__":
    main_screen()
