

def my_decorator(func):
    def wrapper():
        print("before function execution")
        func()
        print("after function execution")
    return wrapper


@my_decorator
def greet():
    print("hello, welcome to world of programming")

greet()