
# traditionl way
# fixed arguments
def display(a,b):
    c = a + b
    return c
output = display(10,20)
print(output)


# pythonic way
# lambda function 
# labmda is the replacement of single liner function
# Advantage : lambda function is faster compared with the regular function
# syntax: 
#funtioname = lambda variables : expression

display = lambda a,b : a + b
output = display(10,20)
print(output)



# 2. Square of a number
square = lambda x: x ** 2
print(square(4))  # 16

# 3. Length of a string
length = lambda s: len(s)
print(length("python"))  # 6


# 4. Multiply three numbers
mul = lambda a, b, c: a * b * c
print(mul(2, 3, 4))  # 24


# 5. Convert to uppercase
upper = lambda s: s.upper()
print(upper("hello"))  # HELLO


# 6. Reverse string
reverse = lambda s: s[::-1]
print(reverse("lambda"))  # adbmal






# 1. Max of two numbers
maximum = lambda a, b: a if a > b else b
print(maximum(10, 20))  # 20




# 2. Pass or Fail
result = lambda marks: "Pass" if marks >= 35 else "Fail"
print(result(30))  # Fail




# 3. Even or Odd
even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even_odd(9))  # Odd



# 4. Positive, Negative or Zero
sign = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(sign(-5))  # Negative





# 5. Grade categorization
grade = lambda m: 'A' if m >= 90 else 'B' if m >= 75 else 'C'
print(grade(80))  # B


# 6. Adult or Minor
age_check = lambda age: "Adult" if age >= 18 else "Minor"
print(age_check(17))  # Minor

# 7. Number is multiple of 3
multiple_of_3 = lambda x: "Yes" if x % 3 == 0 else "No"
print(multiple_of_3(9))  # Yes

# 8. Leap year check
leap_year = lambda y: "Leap" if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) else "Not Leap"
print(leap_year(2020))  # Leap

# 9. Compare lengths
compare_len = lambda a, b: "Equal" if len(a) == len(b) else "Not Equal"
print(compare_len("hi", "by"))  # Equal

# 10. Password strength
password_check = lambda pwd: "Strong" if len(pwd) >= 8 else "Weak"
print(password_check("pass123"))  # Weak














alist = [10,20,30,40,50]


blist = []
for val in alist:
    blist.append( val + 5)
print(blist)
#output: [15,25,35,45,55]





alist = [10,20,30,40,50]
#output: [15,25,35,45,55]

# map(function,iterable)
increment = lambda x : x + 5
print(list(map(increment, alist)))


print(list(map( lambda x : x + 5, alist)))



#Convert to strings
nums = [1, 2, 3, 4, 5]
to_str = list(map(lambda x: str(x), nums))
print(to_str)  # ['1', '2', '3', '4', '5']


#Convert floats to ints
floats = [2.5, 3.6, 4.1]
ints = list(map(lambda x: int(x), floats))
print(ints)  # [2, 3, 4]



#Uppercase names
names = ["alice", "bob", "carol"]
upper_names = list(map(lambda x: x.upper(), names))
print(upper_names)  # ['ALICE', 'BOB', 'CAROL']



#Extract domain from email
emails = ["user1@gmail.com", "user2@yahoo.com"]
domains = list(map(lambda x: x.split("@")[1], emails))
print(domains)





names = ["Alice", "Bob"]
greeted = list(map(lambda x: "Mr./Ms. " + x, names))
print(greeted)



#############################


numbers = [1,2,3,4,5,6]
# filter(function,iterable)
result = list(filter(lambda x: x%2 ==0 , numbers))
print(result)




numbers = [1,2,3,4,5,6]
# filter(function,iterable)
def check(x):
    if x %2 == 0:
        return x
result = list(filter(check , numbers))
print(result)




##########################
# filter only python files from a folder
###########################


import os 
path = "."
py_files = []
files = os.listdir(path)
for file in files:
    if file.endswith(".py"):
        py_files.append(file)
print(py_files)

### using lambda with filter
import os 
path = "."
files = os.listdir(path)
py_files = list(filter(lambda f: f.endswith(".py"), files))
print(py_files)