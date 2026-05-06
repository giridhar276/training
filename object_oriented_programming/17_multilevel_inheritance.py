# 17. Multilevel Inheritance
# Grandparent -> Parent -> Child

class Animal:
    def eat(self):
        print("Animal eats food")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def play(self):
        print("Puppy plays")

p = Puppy()
p.eat()
p.bark()
p.play()
