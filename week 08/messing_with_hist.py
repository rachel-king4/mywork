# messing_with_hist.py
# Author: Rachel King

import numpy as np
import matplotlib.pyplot as plt

'''np.random.seed(1)
norm_data = np.random.normal(size=10000)

plt.hist(norm_data)
plt.show()'''

fruit = np.array(["Apples", "Oranges", "Bananas"])
numbers = np.array([23,77,500])

plt.pie(numbers, labels=fruit)
plt.legend()
plt.show()
