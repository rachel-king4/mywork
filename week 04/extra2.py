# extra2.py
# this program prompts user for an integer
# and keeps prompting for input until user inputs -1
# Author: Rachel King

number  = int(input("enter an integer:"))

while number != -1:
    if (number % 2) == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")

    number  = int(input("enter an integer:"))
    

