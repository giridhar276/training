# 25. Static Method
# Static method does not use self or cls.
# It behaves like a utility function inside a class.

class MathUtility:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(number):
        return number % 2 == 0

print(MathUtility.add(10, 20))
print(MathUtility.is_even(8))
