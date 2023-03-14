# salaries.py
# this program makes an array of numbers and manipulates the matrix
# Author: Rachel King

import numpy as np
min_salary = 20000
max_salary = 80000
number_of_entries = 10

np.random.seed(1)    # this is so the "random" numbers are the same each time to make it easier to debug
salaries = np.random.randint(min_salary, max_salary, number_of_entries)
#salaries_plus = salaries + 5000
salaries_mult = salaries * 1.05    #add 5% by multiplying by 1.05

#print(salaries)
#print(salaries_plus)
#print(salaries_mult)

new_salaries = salaries_mult.astype(int)
print(new_salaries)