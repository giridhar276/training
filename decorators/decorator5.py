
#List files only if directory exists
import os

def directory_exists(func):
    def wrapper(folder):
        if os.path.isdir(folder):
            return func(folder)
        else:
            print("Directory does not exist:", folder)

    return wrapper

@directory_exists
def list_files(folder):
    files = os.listdir(folder)

    for file in files:
        print(file)

list_files("reports")