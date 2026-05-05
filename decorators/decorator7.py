
#Convert result to uppercase

def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase
def get_message():
    return "welcome to python"

print(get_message())