import os
import sys 

FILEPATH = "todos_item.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    with open(filepath,'w') as file:
        file.writelines(todos_arg)

def find_file_in_executable_dir(filename):
    # Get the base path of the executable
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))

    # Construct the full path to the file
    file_path = os.path.join(base_path, filename)
    print("file_path:",file_path)
    # Check if the file exists
    if os.path.exists(file_path):
        return file_path
    else:
        return None