# Number Guesser
# This game has two levels Easy and Hard.
# The user has to guess a number between 1 and 100.
# The user has Five tries to guess the number in easy mode.
# The user has Ten tries to guess the number in hard mode.

from game_logo import logo
from random import randint

print(logo)
print("Welcome to Number Guessing Game !")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ")
if difficulty == 'easy' :
    attempts = 10
elif difficulty == 'hard' :
    attempts = 5
guessed_number = randint(1,100)
while attempts > 0 :
    print(f"\nYou have {attempts} attempts left.")
    user_guess = int(input("Make a guess : "))
    if user_guess > guessed_number :
        print("Your guess is too high.")
    elif user_guess < guessed_number :
        print("Your guess is too low.")
    else :
        print(f"Good job! my guess was {guessed_number}")
        break
    print("Guess again.")
    attempts -= 1
if user_guess != guessed_number :
    print("You failed. The number I was thinking of was", guessed_number)