# is_even.py
# this program inputs number and tells user if number is even or odd
# Author: Rachel King

number  = int(input("enter an integer:"))

if (number % 2) == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")