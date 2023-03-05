# courses_and_grades_extra.py
# this program reads in a student name
# and keeps reading in their modules and grades until user enters a blank module name
#e keeps a list of their courses and grades in a dict
# and prints out the data
# Author: Rachel King

import json
results = {}    # create an empty dictionary

student_name = input("Please enter student name: ")
while student_name != "":   # prompts student name entry until user enters blank
    module_name = input("Please enter module: ")
    while module_name != "":    # prompts module name entry until user enters blank
        grade = input("Please enter grade for this module: ")
        results.update({student_name + "  -  " + module_name : grade})  # updates the dictionary each time the loop runs
        module_name = input("Please enter module: ")

    student_name = input("Please enter student name: ")

print (json.dumps(results, indent = 4))