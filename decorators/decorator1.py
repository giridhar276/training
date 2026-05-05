#Check if folder exists before saving file

import os

def check_folder(func):
    def wrapper(folder, filename, content):
        if not os.path.exists(folder):
            os.makedirs(folder)
            print("Folder created:", folder)
        return func(folder, filename, content)
    return wrapper

@check_folder
def save_file(folder, filename, content):
    path = os.path.join(folder, filename)
    with open(path, "w") as file:
        file.write(content)
    print("File saved:", path)

save_file("reports", "summary.txt", "This is my report")