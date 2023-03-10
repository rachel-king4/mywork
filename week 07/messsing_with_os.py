# messing_with_os.py
# Author: Rachel King

import os
FILENAME = "messing_with_files.py"

if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        for line in f:
            print(line, end = "")

else:
    print(FILENAME, "does not exist")