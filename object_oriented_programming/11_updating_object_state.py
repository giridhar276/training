# 11. Updating Object State
# Object attributes can be changed using methods.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(amount, "deposited")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(amount, "withdrawn")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Current Balance:", self.balance)

account = BankAccount("Ramesh", 5000)
account.deposit(2000)
account.withdraw(1000)
account.display_balance()
