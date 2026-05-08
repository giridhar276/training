




def add():
    print("this is add function")

def sub():
    print("this is sub()")

def mult():
    print("this is mul()")


# cond1: if this program is executed directly , this condition beomes True
# cond2: if this program is imported to other program, this condition becomes False
if __name__ == "__main__":
    add()
    sub()
    mult()