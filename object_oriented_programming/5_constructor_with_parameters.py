# 5. Constructor with Parameters
# We can pass values while creating object.

class Employee:
    def __init__(self, name, city):
        self.name = name      # instance variable
        self.city = city      # instance variable

    def display(self):
        print("Name:", self.name)
        print("City:", self.city)

emp1 = Employee("Ravi", "Mumbai")
emp2 = Employee("Sita", "Chennai")

emp1.display()
print("---")
emp2.display()
