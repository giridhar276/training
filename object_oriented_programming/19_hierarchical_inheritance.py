# 19. Hierarchical Inheritance
# One parent class can have multiple child classes.

class Employee:
    def company_policy(self):
        print("Follow company rules")

class Developer(Employee):
    def write_code(self):
        print("Developer writes code")

class Tester(Employee):
    def test_code(self):
        print("Tester tests code")

dev = Developer()
tester = Tester()

dev.company_policy()
dev.write_code()

print("---")
tester.company_policy()
tester.test_code()
