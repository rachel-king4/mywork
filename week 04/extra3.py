# extra3.py
# this program generates a random number between 0 and 100 for user to guess
# this program prompts user to guess a number 
# program keeps prompting user until user gets it right
# it tells the user if their guess it too high or too low after each guess
# Author: Rachel King

import random

number_to_guess = random.randint(0,100)

guess = int(input("Please guess the number:"))
while guess != number_to_guess:
    if guess < number_to_guess:
        print("too low")
    else:
        print("too high")
    guess = int(input("Please guess again:"))

print("Well done! Yes the number was ", number_to_guess)