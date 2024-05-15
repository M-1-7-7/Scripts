from openpyxl import workbook
from openpyxl import load_workbook
import os
import re

#  copied all Excel files to a single directory let’s say xls_files. 
xls_file_list = os.listdir('xls_files')
pos_find = []

#Create Dirty Word list from the dirty word input file from user
Dirty_words = []
with open('Dity_word.txt', 'r') as file:
    lines = file.readlines()
    for i in lines:
        Dirty_words.append(i.strip())

# iterate over all files in the directory and load each Excel File to a workbook
for xls_file in xls_file_list:
    path = 'xls_files' + '/' + xls_file
    workbook = load_workbook(path)
    sheets = workbook.sheetnames
    for sheet in sheets:
        data= ''
        current_sheet = workbook[sheet]
        for i in range(1, current_sheet.max_row+1):
            for j in range(1, current_sheet.max_column+1):
                cell_obj = current_sheet.cell(row=i, column=j)
                data= data+ ';' + str(cell_obj.value)
        for word in Dirty_words:
            for match in re.finditer(word, data):
                x = xls_file + " : CONTAINS : " + word + " : IN SHEET : " + sheet
                pos_find.append(x)
        
pos_find= list(set(pos_find))

for i in pos_find:
    print(i)
    print("------------------------------------------------")