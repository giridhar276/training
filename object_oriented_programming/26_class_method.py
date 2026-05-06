# 26. Class Method
# Class method receives cls and can access class variables.

class Employee:
    company = "ABC Technologies"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    def display(self):
        print(self.name, "works at", Employee.company)

emp1 = Employee("Asha")
emp2 = Employee("Vikram")

emp1.display()
Employee.change_company("XYZ Solutions")
emp2.display()
