# 3. One Class with Multiple Methods
# A class can contain many methods.

class Employee:
    def display_name(self):
        print("Name: Arjun")

    def display_city(self):
        print("City: Hyderabad")

    def display_salary(self):
        print("Salary: 50000")

emp = Employee()
emp.display_name()
emp.display_city()
emp.display_salary()
