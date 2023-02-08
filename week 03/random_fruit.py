# random_fruit.py
# this program prints out a random fruit
# Author: Rachel King

import random

fruits = ["Apple", "Orange", "Banana", "Pear"]

index = random.randint(0, len(fruits)-1)

fruit = fruits[index]
print(f"A Random Fruit: {fruit}")