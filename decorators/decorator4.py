
#Create backup before modifying file

import os
import shutil

def backup_file(func):
    def wrapper(filename):
        if os.path.exists(filename):
            os.makedirs("backup", exist_ok=True)

            backup_path = os.path.join("backup", os.path.basename(filename))
            shutil.copy(filename, backup_path)

            print("Backup created:", backup_path)

        return func(filename)

    return wrapper

@backup_file
def update_file(filename):
    with open(filename, "a") as file:
        file.write("\nNew line added")

    print("File updated")

update_file("reports/summary.txt")