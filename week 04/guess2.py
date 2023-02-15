# guess2.py
# this program prompts user to guess a number 
# program keeps prompting user until user gets it right
# it tells the user if their guess is too high or too low after each guess
# Author: Rachel King

number_to_guess = 30

guess = int(input("Please guess the number:"))
while guess != number_to_guess:
    if guess < number_to_guess:
        print("too low")
    else:
        print("too high")
    guess = int(input("Please guess again:"))

print("Well done! Yes the number was ", number_to_guess)