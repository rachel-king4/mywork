# lab_messing_with_json2.py
# this program reads in a dict object from a file
# Author: Rachel King

import json
FILENAME = "testdict.json"

def read_dict():
    # this will throw an error if the file does not exist
    # it should really just return an empty dict
    with open(FILENAME) as f:
        return json.load(f)
    

# test the function
some_dict = read_dict()
print(some_dict)