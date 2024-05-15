from pptx import Presentation
import os
import re
files = [x for x in os.listdir("C:\\Users\\ABB58612\\Documents\\Dirty_WordSearcher\\ppt_files\\") if x.endswith(".pptx")] 
Dirty_words = []
with open('Dity_word.txt', 'r') as file:
    lines = file.readlines()
    for i in lines:
        Dirty_words.append(i.strip())
for eachfile in files:
    prs = Presentation("C:\\Users\\ABB58612\\Documents\\Dirty_WordSearcher\\ppt_files\\" + eachfile) 
    for word in Dirty_words:
        for slide in prs.slides:
            for shape in slide.shapes:
                if hasattr(shape, "text"):
                    shape.text = shape.text.lower()                
                    if word in shape.text:
                        print(eachfile, " : CONTAINS : ", word)
                        print("----------------------")
            break
