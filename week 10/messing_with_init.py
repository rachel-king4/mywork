# messing_with_init.py
# Author: Rachel King

class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
    def full_name(self):
        if hasattr(self, 'middlename'):
            return self.firstname + " " + self.middlename + " " + self.lastname
        #return self.firstname + " " + self.middlename + " " + self.lastname
    def __str__(self):
        return self.full_name()
    def add_middle_name(self, middlename):
        self.middlename = middlename


if __name__ == '__main__':
    person1 = Person('Rachel', 'King')

    print(person1.firstname)

    print(person1.full_name())
    person1.add_middle_name("marie")

    print(person1)