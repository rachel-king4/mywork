# normalise.py
# this program reads in a string and strips and leading or trailing spaces
# also converts string to lowercase and output length of input and output strings
# Author: Rachel King

raw_string = input("Please enter a string:")
normalised_string = raw_string.strip().lower()

length_of_raw_string = len(raw_string)
length_of_normalised = len(normalised_string)

print(f"That string normalised is: {normalised_string}")
print(f"we reduced the input string from {length_of_raw_string} to {length_of_normalised} characters")