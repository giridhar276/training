

import sys

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print("List memory:", sys.getsizeof(my_list), "bytes")
print("Tuple memory:", sys.getsizeof(my_tuple), "bytes")