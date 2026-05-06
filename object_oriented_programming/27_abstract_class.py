# 27. Abstract Class
# Abstract class defines common rules for child classes.
# Child class must implement abstract methods.

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")

class UPIPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")

payments = [CreditCardPayment(), UPIPayment()]

for payment in payments:
    payment.pay(1000)
