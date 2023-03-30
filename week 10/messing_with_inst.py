# messing_with_inst.py
# Author: Rachel King

class Nameofclass:
    name = ""
    last = ""
    def getfullname(self):
        return self.name + ' ' + self.last

inst = Nameofclass()
inst2 = Nameofclass()

inst.name = 'rachel'
inst2.last = 'king'

person = inst

inst.last = 'bloggs'

print(person.getfullname())

str1 = "blah de blah"
str2 = str1
str1 += " with bells on top"

print(str2)