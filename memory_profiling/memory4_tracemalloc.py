
#Current memory → memory currently used
#Peak memory    → maximum memory used during execution


import tracemalloc

tracemalloc.start()

numbers = [num for num in range(100000)]

current, peak = tracemalloc.get_traced_memory()

print("Current memory usage:", current / 1024, "KB")
print("Peak memory usage:", peak / 1024, "KB")

tracemalloc.stop()