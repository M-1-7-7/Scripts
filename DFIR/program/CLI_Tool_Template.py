##### NOTE #####
# Use this as a template for the user options
# for CLI.  
#
#
###################
class tool_selection:
    # Variables for the duration of the tool being selected
    Select_A_Tool = True
    tool_list = ["Tool 1", "Tool 2", "Tool 3", "Select Another Data Source", "Exit"]
    target_file = input("Please Select what artifact to load (use full path): ")
    print("YOUR TARGET FILE IS: \n" + target_file)

    # Tool specific functions for when the user selects what they want analysed in the data
    def Select_Data_Source():
        target_file = input("Please Select what artifact to load (use full path): ")
        print("YOUR TARGET FILE IS: \n" + target_file + "\n\n")

    def tool_0():
        print("you selected tool 0")

    def tool_1():
        print("you selected tool 1")

    def tool_2():
        print("you selected tool 2")


    while Select_A_Tool is True:
        # Print Tool List
        tool_list_index = []
        for i in tool_list:
            print(tool_list.index(i), ". ", i)
            tool_list_index.append(tool_list.index(i))

        # Ensure the user types in a valid options that is in the `tool list`
        while True:
            try:
                next_tool = int(input("What tool would you like to pass next? "))
                if next_tool not in tool_list_index:
                    raise ValueError("please enter valid option: ")
                break
            except ValueError as e:
                print(e)

        if next_tool == 0:
            tool_0()
        elif next_tool == 1:
            tool_1()
        elif next_tool == 2:
            tool_2()
        elif next_tool == 3:
            Select_Data_Source()
        elif next_tool == 4:
            print("Exiting toll selector now... \n\n")

        # Ensure the user types in a valid option either to continue or quit the malware finder tool
        while True:
            try:
                bool_select_tool =  input("Would you like to select another tool? \n(Y)es or (N)o: ")
                if bool_select_tool not in ["Y","N"]:
                    raise ValueError("please enter valid option 'Y' or 'N'")
                break
            except ValueError as e:
                print(e)
        
        # Check if user wants to continue with malware finder
        if bool_select_tool == "N":
            Select_A_Tool = False
            print("going back to main menu ... \n\n")
        else:
            Select_A_Tool = True

if __name__ == "__main__":
    tool_selection()
