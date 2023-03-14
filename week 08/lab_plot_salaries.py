# lab_plot_salaries.py
# this program plots salaries data
# Author: Rachel King

import numpy as np
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
number_of_entries = 100

np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, number_of_entries)
ages = np.random.randint(low=21, high=65, size=number_of_entries)

#plt.scatter(ages, salaries)

xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints

#plt.plot(xpoints, ypoints, color='r')
norm_data = np.random.normal(size=10000)
plt.hist(norm_data)
plt.show()

'''plt.title("random plot")
plt.xlabel("Salaries")
plt.ylabel("Age")
plt.legend()
#plt.show()

plt.savefig('prettier-plot.png')'''