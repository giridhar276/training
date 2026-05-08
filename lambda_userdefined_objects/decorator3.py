import os
def file_exists(func):
    def wrapper(filename):
        if os.path.exists(filename):
            func(filename)
        else:
            print("file is not found", filename)
    return wrapper
    

@file_exists
def read_file(filename):
    with open(filename,"r") as file:
        print(file.read())


read_file("emp.log")