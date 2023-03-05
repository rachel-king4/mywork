# lambda_functions.py
# more messing with functions
# anonymous functions
# Author: Rachel King

'''x = lambda arg1: arg1 ** 2

answer = x(4)
print(answer)'''


#businesstype = "standarad"
businesstype = "reduced"

valcalc = lambda amount: amount * 0.23

if businesstype == "reduced":
    valcalc = lambda amount: amount * 0.135

cash = 10 

print(valcalc(cash))

# sort a list
numbers = [2, 33, 55, 1, 4]
sortednumbers = sorted(numbers)

print(f"{numbers} sorted is {sortednumbers}")


# sort dictionary

data = [{'first': 'Guido', 'last': 'Van Rossum', 'YOB': 1956},
        {'first': 'Grace', 'last': 'Hopper', 'YOB': 1906},
        {'first': 'Alan', 'last': 'Turing', 'YOB': 1912}]

sorteddata = sorted(data, key=lambda x: x["first"])
for item in sorteddata:
    print(f"{data} sorted is {sorteddata}")