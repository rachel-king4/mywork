# my_functions.py
# Author: Rachel King

import logging

logging.basicConfig(level=logging.DEBUG)


"""
function that returns the factorial number of an int
ie 7! = 7x6x5x4x3x2x1 = 5040"""

def factorial(num):
    if num < 0:
        logging.warn("factorial received a number less than 0")
        return -1
    if num == 1:
        return 1
    factorial =  1
    num += 1
    for i in range(1,num):
        logging.debug("before mult %d by %d", factorial, i)
        factorial *= i
        logging.debug("after mult %d ", factorial)
    return factorial

if __name__ == "__main__":
    print("in my functions ", __name__)
    assert factorial(7) == 5040