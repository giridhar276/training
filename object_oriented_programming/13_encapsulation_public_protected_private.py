# 13. Encapsulation: Public, Protected, Private
# public: normal variable
# protected: starts with _ ; convention says use carefully
# private: starts with __ ; name mangling is applied

class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner          # public
        self._balance = balance     # protected
        self.__pin = pin            # private

    def show_balance(self):
        print("Owner:", self.owner)
        print("Balance:", self._balance)

    def verify_pin(self, entered_pin):
        if entered_pin == self.__pin:
            print("PIN verified")
        else:
            print("Invalid PIN")

account = BankAccount("Alice", 10000, 1234)
account.show_balance()
account.verify_pin(1234)

print(account.owner)       # Allowed
print(account._balance)    # Works, but not recommended outside class
# print(account.__pin)     # Error: private variable not directly accessible
