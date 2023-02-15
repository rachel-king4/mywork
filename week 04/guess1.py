# guess1.py
# this program prompts user to guess a number 
# program keeps prompting user until user gets it right
# Author: Rachel King

number_to_guess = 30

guess = int(input("Please guess the number:"))
while guess != number_to_guess:
    print("Wrong")
    guess = int(input("Please guess again:"))

print("Well done! Yes the number was ", number_to_guess)