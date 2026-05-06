# 4. Constructor: __init__()
# __init__ executes automatically when object is created.

class Employee:
    def __init__(self):
        print("Constructor called automatically")

    def display(self):
        print("Employee object is ready")

emp = Employee()
emp.display()
