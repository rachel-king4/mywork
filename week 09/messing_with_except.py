# messing_with_except.py
# Author: Rachel King

import sys

#print(sys.argv)

filename = sys.argv[1]
try:
    with open(filename) as f:
        print(f.read())
    var = 10/0
except FileNotFoundError:
    print("file (", filename,") does not exist", sep='')
except:
    print("an exception occurred")