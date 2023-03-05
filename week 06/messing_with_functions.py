# messing with functions
# to demonstrate the defining and using of functions
# Author: Rachel King

#x, y, z = (1, 2, 3)
#print(x, y, z, sep="", end="")
#print(f"{x}-{y} {z}")

def to_power(number, power=3):
    print(number)
    return (number ** power)

#ans  = cube(23)
#print(f"we got {ans}")
num = 45

print(f"and {num} is {to_power(num,2)}")