import os
import simple_commands
import rick
import makeqr
import error
import help

def main_program():     #the programs main function
    current_dir = str(os.getcwd())  #gets current directory and puts it as a string in current_dir
    user_input = input(current_dir + " $")
    user_input_array = user_input.split()
    command = user_input_array[0]

    if command == "clear":
        simple_commands.clear() #clears all previous commands

    if command == "pwd":
        simple_commands.pwd()   #prints working
        main_program()

    if command == "mkdir":
        new_folder_name = user_input_array[1]
        os.mkdir(new_folder_name)
        main_program()

    if command == "makeqr":
        content = input("content: ")
        name = input("name: ")
        scalestr = input("scale: ")
        scaleInt = int(scalestr)
        makeqr.makeqrcode(content, name, scaleInt)
        main_program()

    if command == "quit":
        quit()

    if command == "help":
        help.help()
        main_program()

    if command == "rick":
        rick.special_surprise()
        main_program()
    
    else:
        error.errors.command_not_recognised(command)
        main_program()

main_program()
