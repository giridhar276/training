# 21. super() Function
# super() calls parent class constructor/method.

class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

class Manager(Employee):
    def __init__(self, name, team_size):
        super().__init__(name)       # call parent constructor
        self.team_size = team_size

    def display(self):
        super().display()            # call parent method
        print("Team Size:", self.team_size)

mgr = Manager("Suresh", 8)
mgr.display()
