
#Memory comparison: for loop vs list comprehension vs map

import sys

numbers = range(1, 100000)

# For loop
squares_for = []
for num in numbers:
    squares_for.append(num * num)

# List comprehension
squares_list = [num * num for num in range(1, 100000)]

# Map
squares_map = list(map(lambda num: num * num, range(1, 100000)))

print("For loop memory:", sys.getsizeof(squares_for), "bytes")
print("List comprehension memory:", sys.getsizeof(squares_list), "bytes")
print("Map memory:", sys.getsizeof(squares_map), "bytes")