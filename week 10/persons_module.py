# persons_module.py
# Author: Rachel King

import datetime as dt

def gethealthdata(person):
    print("get health data: ", person['firstname'])

def displayperson(person):
    print(person)



if __name__ == '__main__':
    person1 = {
        'firstname' : 'rachel',
        'lastname' : 'king',
        'dob' : dt.date(2010,1,1),
        'height' : 180,
        'width' : 100
    }
displayperson(person1)
gethealthdata(person1)