
#Check file size before processing

import os

def check_file_size(func):
    def wrapper(filename):
        if not os.path.exists(filename):
            print("File not found")
            return

        size = os.path.getsize(filename)

        if size == 0:
            print("File is empty")
        else:
            return func(filename)

    return wrapper

@check_file_size
def process_file(filename):
    print("Processing file:", filename)

process_file("reports/summary.txt")