# lab_messing_with_os.py
# this program counts how many times it was run
# Author: Rachel King

FILENAME = "count.txt"
def read_number():
    with open(FILENAME) as f:
        number = int(f.read())
        return number

def write_number(number):
    with open(FILENAME, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))

import os.path
filename = "count.txt"
if not os.path.isfile(filename):
    print("File does not exist")
    # initialise file here
    write_number(0)


def read_number():
    try:
        with open(filename) as f:
            number = int(f.read())
            return number
    except IOError:
         # this file will be created when we write back.
         # no file assumes first time running 
         # ie 0 previous runs
        return 0
    

# main
num = read_number()
num += 1
print(f"we have run this program {num} times")
write_number(num)