# Love Calculator 
# using the logic Take both people's names and 
# check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.

# Welcome message
print("Welcome to the Love Calculator!")

# user inputs
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# convert to lower case
name1 = name1.lower()
name2 = name2.lower()

# count the "true" letters in name1 and name2
count_true = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e") + name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")

# count the "love" letters in name1 and name2
count_love = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e") + name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

# calculate love percentage
love_percentage = count_true * 10 + count_love

# print love percentage
if love_percentage < 10 or love_percentage > 90 :
    print(f"Your score is {love_percentage}, you go together like coke and mentos.")
elif love_percentage > 40 and love_percentage < 50 :
    print(f"Your score is {love_percentage}, you are alright together.")
else :
    print(f"Your score is {love_percentage}.")