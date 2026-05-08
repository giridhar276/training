
import os
#from allfunctions import check_folder
import allfunctions
@allfunctions.check_folder
def save_file(folder, filename, content):
    path = os.path.join(folder, filename)
    with open(path, "w") as file:
        file.write(content)
    print("File saved:", path)

save_file("reports", "summary.txt", "This is my report")