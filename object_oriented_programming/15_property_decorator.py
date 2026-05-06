# 15. @property Decorator
# @property allows method to be accessed like an attribute.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            print("Invalid salary")

emp = Employee("John", 30000)
print(emp.salary)

emp.salary = 45000
print(emp.salary)
