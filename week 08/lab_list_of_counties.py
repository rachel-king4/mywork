# lab_list_of_counties.py
# this program makes a list of counties and plots them
# Author: Rachel King

import numpy as np
import matplotlib.pyplot as plt

possible_counties = ['Mayo', 'Galway', 'Rosommon', 'Dublin','Donegal']
# pick 100 randomly from possible counties with the frequence set in p
counties = np.random.choice(
    possible_counties ,
    p=[0.1, 0.3, 0.2, 0.12, 0.28 ],
    size=(100)
)

# this returns a tuple of the unique values and how many times they appear
unique, counts = np.unique(counties, return_counts=True)

#plt.pie(counts, labels= unique)
plt.bar(unique, counts)
plt.show()
