
#Add GST to bill

def add_gst(func):
    def wrapper(amount):
        bill = func(amount)
        gst = bill * 0.18
        return bill + gst
    return wrapper

@add_gst
def calculate_bill(amount):
    return amount

print(calculate_bill(1000))