#Generator uses less memory
#Output will show that generator takes very less memory because it does lazy loading.


import sys

list_data = [num * num for num in range(1, 100000)]

generator_data = (num * num for num in range(1, 100000))

print("List memory:", sys.getsizeof(list_data), "bytes")
print("Generator memory:", sys.getsizeof(generator_data), "bytes")