

import sys

# Different Python objects
name = "Python"
numbers = [10, 20, 30, 40, 50]
student = {"name": "Ravi", "age": 25}
marks = (80, 90, 85)

# sys.getsizeof() returns memory in bytes
print("String memory:", sys.getsizeof(name), "bytes")
print("List memory:", sys.getsizeof(numbers), "bytes")
print("Dictionary memory:", sys.getsizeof(student), "bytes")
print("Tuple memory:", sys.getsizeof(marks), "bytes")