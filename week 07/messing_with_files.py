# messing_with_files.py
# Author: Rachel King

FILENAME = "data.txt"
'''
with open(FILENAME, 'r') as f:
    data = f.read()
    #print(data, end = "")
    print(data.strip() )
    #print(data[:-1])'''


with open("data2.txt", "w+") as f:
    f.write("how now\n")
    f.write("brown cow")
    f.seek(0)
    data = f.read()
    print(data)

print("done")