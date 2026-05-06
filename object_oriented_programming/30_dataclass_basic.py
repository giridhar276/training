# 30. dataclass
# dataclass reduces boilerplate code for simple data containers.

from dataclasses import dataclass

@dataclass
class Employee:
    emp_id: int
    name: str
    department: str

emp = Employee(101, "Neha", "IT")
print(emp)
print(emp.name)
