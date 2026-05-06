# 16. Single Inheritance
# Child class inherits properties/methods from one parent class.

class Vehicle:
    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    def drive(self):
        print("Car is moving")

car = Car()
car.start_engine()  # inherited method
car.drive()         # child method
