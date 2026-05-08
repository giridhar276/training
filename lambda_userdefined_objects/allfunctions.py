#Check if folder exists before saving file

import os

def check_folder(func):
    def wrapper(folder, filename, content):
        if not os.path.exists(folder):
            os.makedirs(folder)
            print("Folder created:", folder)
        return func(folder, filename, content)
    return wrapper
