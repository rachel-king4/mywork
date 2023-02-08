# div.py
# this program reads in two numbers and divides the first one by the second one to give the integer result and the remainder
# Author: Rachel King

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))

answer = int(x//y) 
remainder = x%y

# print("{} divided by {} is {} with remainder {}".format( x, y, answer, remainder))
print(f"{x} divided by {y} is {answer} with remainder {remainder}")