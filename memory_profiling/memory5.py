
#Find which line uses more memory

import tracemalloc

tracemalloc.start()

list1 = [i for i in range(100000)]
list2 = [i * i for i in range(200000)]
list3 = [str(i) for i in range(300000)]

snapshot = tracemalloc.take_snapshot()

top_stats = snapshot.statistics("lineno")

print("Top memory consuming lines:")

for stat in top_stats[:5]:
    print(stat)

tracemalloc.stop()