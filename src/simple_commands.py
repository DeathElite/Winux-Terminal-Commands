import os

def clear():
    os.system('cls')

def pwd():
    current_path = os.getcwd()
    print(current_path)

def cd(path):
    os.chdir(path)
    print("changed to " + path)
