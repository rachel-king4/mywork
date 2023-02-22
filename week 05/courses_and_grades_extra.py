# courses_and_grades_extra.py
# this program reads in a student name
# and keeps reading in their modules and grades until user enters a blank module name
# and a list of their courses and grades in a dict
# and prints out the data
# Author: Rachel King

'''student_name = input("Please enter student name:")
module_name = input("Please enter module:")


while module_name != "":
    
    grade = input("Please enter grade for this module:") 

    module_name = input("Please enter module:")'''


student_name = input("Please enter student name:")

while student_name != "":

    module_name = input("Please enter module:")
    while module_name != "":
    
        grade = input("Please enter grade for this module:") 

        module_name = input("Please enter module:")
    

    student_name = input("Please enter student name:")