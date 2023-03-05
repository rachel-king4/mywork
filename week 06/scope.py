# scope.py
# more messing with functions
# to demonstrate the defining and using of functions
# Author: Rachel King

x = 999

def fun(num):
    print(num)


fun(x)

def fun2(x2):
    print(f"in fun2 x {x2}")
    global x
    x = 21
    print(f"in fun2 x {x2}")


fun2(x)
print(f"after fun2 x is {x}")
