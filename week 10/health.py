# health.py
# use person module
# Author: Rachel King

from persons_module import *


person1 = {
        'firstname' : 'rachel',
        'lastname' : 'king',
        'dob' : dt.date(2010,1,1),
        'height' : 180,
        'width' : 100
}
displayperson(person1)
gethealthdata(person1)