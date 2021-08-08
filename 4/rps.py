# Rock paper scissors project
# Day 4 project
from random import randint

# Starting assets
def get_image(n) :
    if n == 0 :
        return '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
    elif n == 1 :
        return '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
    else :
        return '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? \n0 for Rock\n1 for Paper\n2 for Scissors. "))
computer_choice = randint(0,2)

print(f"You chose \n { get_image(choice) } \nThe computer chose \n { get_image(computer_choice) }")

if choice == computer_choice :
    print("You won!")
else :
    print("You lost!")