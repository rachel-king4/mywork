# messing_with_json.py
# Author: Rachel King

import json

electric_bill = {
    'name' : 'Andrew',
    'amount' : '9999'
}

with open("store_data.json", "wt") as f:
    json.dump(electric_bill, f)   #writes the dictionary