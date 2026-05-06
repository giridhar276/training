# 28. Composition: HAS-A Relationship
# Example: A Car HAS-A Engine.

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()   # Car contains Engine object

    def start_car(self):
        self.engine.start()
        print("Car started")

car = Car()
car.start_car()
