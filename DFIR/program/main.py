
import platform
import os
import subprocess

os_host = platform.system()
file_path = os.path.dirname(os.path.normpath(__file__))

def analyse_full_disk():
    print("What artifacs would you like analysed? ")
    while True:
        try:
            artifact_type = int(input("1. find malware, 2. fing xxx: "))
            if artifact_type not in [1,2]:
                raise ValueError("please enter valid option '1, 2 ...'")
            break
        except ValueError as e:
            print(e)
    print("thank you, you chose: ", artifact_type)

    if artifact_type == 1:
        malware_anaysis()
    #elif artifact_type == 2:
    #    xxx()

def analyse_memory():
    print("What artifacs would you like analysed? ")
    while True:
        try:
            artifact_type = int(input("1. find xxx, 2. find xxx: "))
            if artifact_type not in [1,2]:
                raise ValueError("please enter valid option '1, 2 ...'")
            break
        except ValueError as e:
            print(e)
    print("thank you, you chose: ", artifact_type)

    if artifact_type == 1:
        mem_anaysis()

def malware_anaysis():
    if os_host == "Windows":
        path = file_path + "\\Win_Malware_Analysis.py"
    elif os_host == "Linux":
        path = file_path + "\\Lin_Malware_Analysis.py"
    elif os_host == "Darwin":
        path = file_path + "/CLI_Tool_Template.py"

    with open(path) as file:
            exec(file.read())

def main():
    print("what evidence do you have? ")
    while True:
        try:
            evidence_type = int(input("1. for full disk image, 2. for memory image: "))
            if evidence_type not in [1,2]:
                raise ValueError("please enter valid option '1' or '2'")
            break
        except ValueError as e:
            print(e)
    print("thank you, you chose: ", evidence_type)

    if evidence_type == 1:
        analyse_full_disk()

    elif evidence_type == 2:
        analyse_memory()

if __name__ == "__main__":
    main()
