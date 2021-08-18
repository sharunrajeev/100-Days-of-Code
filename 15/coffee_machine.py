# Digital coffee maker program
# This program accepts coffee types from the user, accepts payment, payback any balance and also manage resources.

# Imports resources and menu from assets
from assets import *

# Variable to store empty resources.
empty_res = []


# Function to check if we have ample resources to perform the action
def we_have_resources(coffee_type):
    if resources['water'] < MENU[coffee_type]['ingredients']['water']:
        empty_res.append('water')
        return False
    elif resources['milk'] < MENU[coffee_type]['ingredients']['milk']:
        empty_res.append('milk')
        return False
    elif resources['coffee'] < MENU[coffee_type]['ingredients']['coffee']:
        empty_res.append('coffee')
        return False
    else:
        return True


# Variable to end the program
end = False
# Variable to keep track of the money
amount = 0

# The main function
while not end:
    print("Coffee maker Assistant")
    c_type = input("What would you like? (espresso, latte, cappuccino) : ")  # Coffee type is accepted from the user
    menu = MENU  # Coffee details are taken from assets
    if c_type == 'report':
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${amount:.2f}\n")
    elif c_type == 'espresso' or c_type == 'latte' or c_type == 'cappuccino':
        if we_have_resources(c_type):
            print('Please insert coins.')
            quarters = int(input('How many quarters ? : '))
            dimes = int(input('How many dimes ? : '))
            nickels = int(input('How many nickels ? : '))
            pennies = int(input('How many pennies ? : '))
            input_amount = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
            if input_amount > MENU[c_type]['cost']:
                print(f"Here is {(input_amount - MENU[c_type]['cost']):.2f} change.")
                print(f"Here is your {c_type} ☕ Enjoy!")
                amount += MENU[c_type]['cost']
            else:
                print("Sorry that's not enough money. Money refunded.")
            resources['water'] -= MENU[c_type]['ingredients']['water']
            resources['milk'] -= MENU[c_type]['ingredients']['milk']
            resources['coffee'] -= MENU[c_type]['ingredients']['coffee']
        else:
            print(f"Sorry there is not enough {','.join(empty_res)}")
    elif c_type == 'exit':
        print("Have a nice day!")
        end = True
        empty_res.clear()
    else:
        print("Wrong input. Program exiting...")
        empty_res.clear()
        end = True
