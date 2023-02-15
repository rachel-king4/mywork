# average.py
# this program prompts user to enter a number
# program keeps prompting user until user enters 0
# it prints out each number entered and the average of them
# Author: Rachel King

numbers= []

number = int(input("enter number (0 to quit): "))

while number != 0:
    numbers.append(number)

    number = int(input("enter another (0 to quit):"))

for value in numbers:
    print(value)

average = float(sum(numbers)) / len(numbers)
print(f"The average is {average}")