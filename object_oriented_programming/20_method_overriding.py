# 20. Method Overriding
# Child class can redefine parent class method.

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

animals = [Animal(), Dog(), Cat()]

for animal in animals:
    animal.sound()
