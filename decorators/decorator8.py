#check age before applying loan

def check_age(func):
    def wrapper(name, age):
        if age >= 21:
            return func(name, age)
        else:
            print(f"{name} is not eligible for loan")
    return wrapper

@check_age
def apply_loan(name, age):
    print(f"Loan application accepted for {name}")

apply_loan("Ravi", 25)
apply_loan("Kiran", 18)