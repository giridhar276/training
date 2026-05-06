# 2. Class and Object
# Class is a blueprint/template.
# Object is a real instance created from the class.

class Employee:
    def display_details(self):
        print("Employee Name: Riya")
        print("Department: HR")

# Creating object of Employee class
emp1 = Employee()

# Calling method using object
emp1.display_details()
