# raise_an_exception.py
# Author: Rachel King

try:
    input_var = input("Enter a number: ")
    number = int(input_var)
    if (number < 0):
        raise ValueError("Negative value entered")
    print("Number multiplied by 2 is:", number*2)
except ValueError:
    print("Please enter a number")

