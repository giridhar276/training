#Check if file exists before reading

import os

def file_exists(func):
    def wrapper(filename):
        if os.path.exists(filename):
            return func(filename)
        else:
            print("File not found:", filename)
    return wrapper

@file_exists
def read_file(filename):
    with open(filename, "r") as file:
        print(file.read())

read_file("reports/summary.txt")