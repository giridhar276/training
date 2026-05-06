# 14. Getter and Setter Methods
# Getter reads private data.
# Setter safely updates private data.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Salary must be positive")

emp = Employee("Kavya", 40000)
print("Old Salary:", emp.get_salary())

emp.set_salary(50000)
print("New Salary:", emp.get_salary())
