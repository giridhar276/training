
val = 10
print(val)


#string 
aname = "python programming"

print("language:", aname)
print(aname.upper())
print(aname.isupper())
print(aname)

aname = aname.upper()

#list
alist = [10,20,"java",["rita","gita"]]

print(alist)
alist.append(40)
print(alist)
alist.extend([50,60,70,70,80])
print(alist)
alist = [10,20,30]
alist.append(40)
print("After appending:",alist)
alist.extend([50,60,70,90])
print("After extending:",alist)


#tuple
atup = (10,20,30)
atup[0] = 100
print(atup.count(10))

#dictionary
book = {"chap1":10 ,"chap2":20 ,"chap3":30}
print(book.keys())
print(book.values())
print(book.items())

#set
aset = {10,20,20,20,10,10,20,30,30}
bset = {40,40,40,40,50,60}
print(aset)
print(aset.union(bset))
print(aset.intersection(bset))