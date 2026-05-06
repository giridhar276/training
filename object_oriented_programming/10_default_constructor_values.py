# 10. Default Values in Constructor
# Constructor parameters can have default values.

class Product:
    def __init__(self, name, price, status="Available"):
        self.name = name
        self.price = price
        self.status = status

    def display(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Status:", self.status)

p1 = Product("Laptop", 60000)
p2 = Product("Mobile", 25000, "Sold")

p1.display()
print("---")
p2.display()
