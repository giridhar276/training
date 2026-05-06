# 31. Exception Handling inside Class
# Methods can handle errors using try-except.

class Divider:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def divide(self):
        try:
            result = self.a / self.b
            print("Result:", result)
        except ZeroDivisionError:
            print("Cannot divide by zero")
        except Exception as e:
            print("Error:", e)

obj1 = Divider(10, 2)
obj2 = Divider(10, 0)

obj1.divide()
obj2.divide()
