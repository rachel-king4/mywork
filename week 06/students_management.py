# students_grades.py
# program for gathering student grades data
# Author: Rachel King

def display_menu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(b) View Students")
    print("\t(c) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

def do_add(students):
    current_student = {}
    current_student["Name"] = input("Enter name: ")
    current_student["Modules"] = read_modules()
    students.append(current_student)


def read_modules():
    modules = []
    module_name = input(
            "\tEnter the first module name (blank to quit): ").strip()
    
    while module_name != "":
        module = {}
        module["Name"] = module_name
        module["Grade"] = int(input("\t\tEnter grade: "))
        modules.append(module)
        module_name = input(
            "\tEnter next module name (blank to quit): ").strip()
        
    return modules

def display_modules(modules):
    print("\tName       \tGrade")
    for module in modules:
        print("\t{}     \t {}".format(module["Name"], module["Grade"]))


def do_view(students):
    for current_student in students:
        print(current_student["Name"])
        display_modules(current_student["Modules"])


# main program

students = []

choice = display_menu()
while choice != "q":
    if choice == "a":
        do_add(students)
    elif choice == "v":
        do_view(students)
    elif choice != "q":
        print("\n\nPlease select either a,v or q")
    choice=display_menu()