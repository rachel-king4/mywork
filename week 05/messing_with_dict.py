# messing with dictionaries
# Author: Rachel King

car = {
    "make" : "ford",
    "model" : "mondeo",
    "year" : 2006,
    "owner" : {
        "name" : "rachel",
        "owner-driver-number" : 1123
    }
}

print(car["owner"]["name"])