# 23. Operator Overloading
# Special methods allow operators to work with objects.
# __add__ controls + operator behavior.

class Cart:
    def __init__(self, items):
        self.items = items

    def __add__(self, other):
        return Cart(self.items + other.items)

    def display(self):
        print("Cart Items:", self.items)

cart1 = Cart(["Laptop", "Mouse"])
cart2 = Cart(["Keyboard", "Monitor"])

cart3 = cart1 + cart2
cart3.display()
