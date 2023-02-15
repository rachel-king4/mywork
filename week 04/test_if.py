# test_if.py
# this program is messing with ifs
# Author: Rachel King

b = 1
if False: 
    print("we are in the if statement")
    b = 22

print("sanity", b)

c = 1 
if c == 1:
    print("c is one")
else:
    print("c is not one")

d = 4
if d < 0:
    print("d is negative")
elif d >= 10:
    print("d is 10 or higher")
else:
    print("d is between 0 and 9 inclusive")

print("sanity", b)