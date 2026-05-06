# 6. self Keyword
# self refers to the current object.
# It helps each object maintain its own data.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(self.name, "scored", self.marks)

s1 = Student("Anu", 90)
s2 = Student("Manu", 75)

s1.show()   # self refers to s1
s2.show()   # self refers to s2
