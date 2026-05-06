# 1. Procedural Programming vs Object Oriented Programming
# Procedural style: write direct statements/functions.
# OOP style: group data + behavior inside a class.

print("Procedural output:")
print("Hello from normal code")

class Display:
    # Method: function written inside a class
    def show_message(self):
        print("Hello from OOP code")

print("\nOOP output:")
obj = Display()       # Object creation
obj.show_message()    # Calling method using object
