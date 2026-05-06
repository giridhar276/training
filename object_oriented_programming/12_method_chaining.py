# 12. Method Chaining
# Returning self allows calling multiple methods in one line.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.status = "Available"

    def apply_discount(self, percentage):
        self.price = self.price - (self.price * percentage / 100)
        return self

    def mark_sold(self):
        self.status = "Sold"
        return self

    def display(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Status:", self.status)
        return self

product = Product("Headphones", 2000)
product.apply_discount(10).mark_sold().display()
