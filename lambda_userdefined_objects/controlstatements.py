# display numbers from 1 to 5
for val in range(1,6):
    print(val)
# range(start,stop,step)
for val in range(5,0,-1):
    print(val)
    
# iterating string
name = "python"
for char in name:
    print(char)

# iterating list
alist = [10,20,30]
for val in alist:
    print(val)

# reading dictionary
book = {"chap1":10 ,"chap2":20}
for key in book:
    print(key)

for value in book.values():
    print(value)

# set operations
aset = {10,10,10,10,20,20,30}
for val in aset:
    print(val)