# random_generator.py
# this program prints out a random number between 1 and 10
# modified to allow user to input range
# Author: Rachel King

import random

a = int(input("Enter beginning of range: "))
b = int(input("Enter end of range: "))


number = random.randint(a,b)
print(number)