


import time

def check_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        total_time = end_time - start_time

        print(f"{func.__name__} took {total_time:.4f} seconds")

        return result

    return wrapper


@check_time
def squares_using_for_loop():
    numbers = range(1, 1000000)

    squares = []
    for num in numbers:
        squares.append(num * num)

    return squares


@check_time
def squares_using_list_comprehension():
    numbers = range(1, 1000000)

    squares = [num * num for num in numbers]

    return squares


@check_time
def squares_using_map():
    numbers = range(1, 1000000)

    squares = list(map(lambda num: num * num, numbers))

    return squares


squares_using_for_loop()
squares_using_list_comprehension()
squares_using_map()