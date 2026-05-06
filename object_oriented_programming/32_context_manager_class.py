# 32. Context Manager using Class
# __enter__ and __exit__ help use object with 'with' statement.

class FileWriter:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "w", encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print("File closed automatically")

with FileWriter("sample_output.txt") as file:
    file.write("This file was created using a custom context manager.\n")

print("Writing completed")
