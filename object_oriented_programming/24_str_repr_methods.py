# 24. __str__ and __repr__
# __str__ gives user-friendly output.
# __repr__ gives developer-friendly/debug output.

class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def __str__(self):
        return f"Employee: {self.name}"

    def __repr__(self):
        return f"Employee(emp_id={self.emp_id}, name='{self.name}')"

emp = Employee(101, "Rahul")
print(str(emp))
print(repr(emp))
print(emp)
