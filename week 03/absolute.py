# absolute.py
# this program takes in a number and gives its absolute value
# Author: Rachel King

# number is ambiguous but output implies dealing with floats
# casting the input to a float

number = float(input("Enter a number:"))
absolute_value = abs(number)    
print(f"The absolute value of {number} is {absolute_value}")