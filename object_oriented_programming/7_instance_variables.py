# 7. Instance Variables
# Instance variables are object-specific variables.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def display(self):
        print("Owner:", self.owner)
        print("Balance:", self.balance)

acc1 = BankAccount("Kiran", 10000)
acc2 = BankAccount("Meena", 25000)

acc1.display()
print("---")
acc2.display()
