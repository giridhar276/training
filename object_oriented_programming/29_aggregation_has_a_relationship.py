# 29. Aggregation
# Aggregation means one object uses another object, but both can exist independently.

class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state

class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display(self):
        print("Name:", self.name)
        print("City:", self.address.city)
        print("State:", self.address.state)

addr = Address("Hyderabad", "Telangana")
emp = Employee("Giridhar", addr)
emp.display()
