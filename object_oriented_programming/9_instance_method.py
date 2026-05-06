# 9. Instance Method
# Instance method works with object data using self.

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print("Addition:", self.a + self.b)

    def multiply(self):
        print("Multiplication:", self.a * self.b)

calc = Calculator(10, 5)
calc.add()
calc.multiply()
