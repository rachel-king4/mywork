# convert.py
# this program takes an input in dollars and cents (eg 9 dollars and 44 cent) and outputs the absolute value in cents
# Author: Rachel King

number = float(input("Please enter an amount:"))
number_two_decimal_places = "{:.2f}".format(number)
number_in_cent = int(abs(number*100))

print(f"The amount in cent is: {number_in_cent}")

