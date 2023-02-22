# courses_and_grades.py
# this program stores a student name
# and a list of their courses and grades in a dict
# and prints out the data
# Author: Rachel King

student = {
    "name":"Mary",
    "modules": [
        {
            "courseName":"Programming",
            "grade": 45
        },
        {
            "courseName":"History",
            "grade":99
        }
    ]
}
print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))
