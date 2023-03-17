# read in two numbers and multiply them
# Author: Rachel King

def read_num(message = "Enter a number: "):
    num = False
    while (not num):
        try:
            num = int(input(message))
        except ValueError:
            print("That was not a number: ",end="")
    return num
            
num1 = read_num()
num2 = read_num("Enter another number: ")

answer = num1 * num2

print(f"answer is {answer}")