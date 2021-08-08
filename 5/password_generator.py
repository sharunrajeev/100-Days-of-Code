#Password Generator Project
import random

# list of characters to choose from
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Empty password string
password = ''
while nr_letters + nr_symbols + nr_numbers > 0 :    # total length of password > 0
    choice = random.randint(0,2)    # choose from letters, numbers, symbols
    if nr_letters != 0 and choice == 0 :    # if there are still letters left
        password += random.choice(letters)
        nr_letters -= 1
    if nr_symbols != 0 and choice == 1 :    # if there are still symbols left
        password += random.choice(symbols)
        nr_symbols -= 1
    if nr_numbers != 0 and choice == 0 :    # if there are still numbers left
        password += random.choice(numbers)
        nr_numbers -= 1
print(password)     # print the password

# or simply use random.shuffle(password) to shuffle the password