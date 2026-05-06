# 8. Class Variables
# Class variables are shared by all objects.

class Employee:
    company_name = "ABC Technologies"   # class variable

    def __init__(self, name):
        self.name = name                 # instance variable

    def display(self):
        print("Name:", self.name)
        print("Company:", Employee.company_name)

emp1 = Employee("Raj")
emp2 = Employee("Priya")

emp1.display()
emp2.display()
