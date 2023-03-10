# lab_messing_with_files.py
# this program counts how many times it was run
# Author: Rachel King

FILENAME = "count.txt"
def read_number():
    with open(FILENAME) as f:
        number = int(f.read())
        return number

def write_number(number):
    with open(FILENAME, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))

# main
num = read_number()
num += 1
print(f"we have run this program {num} times")
write_number(num)