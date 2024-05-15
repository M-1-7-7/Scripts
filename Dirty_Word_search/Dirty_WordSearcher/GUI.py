from tkinter import *
from tkinter import ttk
import tkinter
import os
from tkinter import messagebox 
# Window Configuration
root = Tk()
root.geometry("800x600")
frm = ttk.Frame(root, padding=10)
frm.grid()
DW_Var=tkinter.StringVar()
start_dir_Var=tkinter.StringVar()
out_dir_Var=tkinter.StringVar()

# Dictionary to create multiple buttons
Excel_Button_Val = IntVar() 
PDF_Button_Val = IntVar() 
PowerPoint_Button_Val = IntVar() 
Doc_Button_Val = IntVar() 
TXT_Button_Val = IntVar() 
All_Document_Type_Button_Val = IntVar() 

# Functions that will execute specificly to the checkboxes ticked by the user
def scan_all_docs():
    print("Scanning all docs")
    scan_excel_doc()
    scan_pdf_doc()
    scan_powerpoint_doc()
    scan_word_doc()
    scan_txt_doc()

def scan_excel_doc():
    print("Scanning excel docs")

def scan_pdf_doc():
    print("Scanning pdf docs")
    
def scan_powerpoint_doc():
    print("Scanning powerpoint docs")
    
def scan_word_doc():
    print("Scanning word docs")
    
def scan_txt_doc():
    print("scanning txt docs")

def check_user_input():
    user_input_good = ""
    user_input_bad = ""
    # check if directory exists
    if not os.path.exists(start_dir_Var.get()): 
        user_input_bad += "!!!Please enter a valid STARTING DIRECTORY!!!\n"
    else:
        user_input_good += "starting directory is existing :)\n"

    if not os.path.exists(out_dir_Var.get()): 
        user_input_bad += "!!!Please enter a valid OUTPUT DIRECTORY!!!\n"
    else:
        user_input_good += "Output directory is existing :)\n"

    # check if we can read dirty word file
    try:
        with open(DW_Var.get(), "r"):
            user_input_good += "we can open dirty word txt :)\n"
    except PermissionError:
        user_input_bad += "!!!Not Accesable!!!\n"
    if len(user_input_bad) >0:
        messagebox.showerror("Your Input Status", user_input_bad)
    else:    
        print(user_input_good)

# Functions from GUI Buttons
def search_files():
    #dirty_word_file=DW_Var.get()
    #start_directory=start_dir_Var.get()
    #out_directory=out_dir_Var.get()
    # Ensure the files and Dirs entered by user are going to work
    check_user_input()

    #For Dev Only
    #print("This is my dirty word file: ", dirty_word_file)
    #print("This is my starting dir: ", start_directory)
    #print("This is my output dir: ", out_directory)

    if All_Document_Type_Button_Val.get() == 1:
        print("Scanning all docs")
        scan_excel_doc()
        scan_pdf_doc()
        scan_powerpoint_doc()
        scan_word_doc()
        scan_txt_doc()

    if All_Document_Type_Button_Val.get() == 0:
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

#Main Screen
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

    search_btn.grid(column=8, row=10)
    reset_btn.grid(column=9, row=10)
    quit_btn.grid(column=10, row=10)

    root.mainloop()
    
if __name__ == "__main__":
    main_screen()
