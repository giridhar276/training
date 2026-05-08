

name = "python programming"
if "python" in name:
    print("substring found")
    print("inside if ")
    print("still inside if ")
else:
    print("not found")
    print("inside else")
    print("still inside else")


# if-elif-elif-elif-else
lang = input("Enter any languages:")
if "python" in lang:
    print("its python")
elif "java" in lang:
    print("its java")
elif "C" in lang:
    print("its c")
else:
    print("its someother language")


alist = [10,20,30]
if 20 in alist:
    print("True")
else:
    print("False")


book = {"chap1":10 ,"chap2":20}
if "chap1" in book.keys():
    print("key found")
else:
    print("key is not found")

if 10 in book.values():
    print("value is found")
else:
    print("value found")