import random

def run_guessing_game(secret_number):
    guess = -1 # why am I doing this?
    while (guess != secret_number):
        guess = input("Can you guess it?\n")
        # guess is a string. It needs to be an int
        # (The error message with tell you this too)
        if guess > secret_number:
            print("Fill me in Liz")
        else:
            print("You'll probably need three if/else branches")


max_number = 100
print("I'm thinking of a number between 0 and", max_number)
secret_number = random.randint(0, 100)
run_guessing_game(secret_number)