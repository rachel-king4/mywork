# lab_messing_with_json.py
# this program stores a dict as json file
# Author: Rachel King

import json
FILENAME = "testdict.json"
sample = dict(name = 'fred', age = 31, grades = [1,34,55])

def write_dict(obj):
    with open(FILENAME, 'wt') as f:
        json.dump(obj, f)

# test the function
write_dict(sample)