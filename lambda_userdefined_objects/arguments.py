# fixed arguments
def display(a,b):
    print(a,b)
display(10,20)

# default arguments 
def display(a = 0,b = 0,c =0):
    print(a,b,c)
display()
display(10)
display(10,20)
display(10,20,30)


# keyword arguments
def display(b,a,c):
    print(a,b,c)
display(c=30,a=10,b=20)

# varaible length arguments
# in python, if any variable begins with * .... it is treated as tuple
def display(*data):
    print("value:",data[3:7])
    for val in data:
        print(val)
display(10,20,30,40,50,45,2,56,32,67,2,6732,5,32,5,32,46,32,54,4332,6)

def displayinfo(**kwargs):
    print(kwargs)

displayinfo(chap1 = 10 , chap2 = 20)