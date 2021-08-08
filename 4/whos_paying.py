# Program to find who is going to pay in a food pool.
from random import randint

# Inputs friends names with commas in between.
friends = input("Enter name of your friends in food pool.\n")
# Splits the friends names into a list.
friends_list = friends.split(',')
# prints random friend name from the list.
print(f"{friends_list[randint(0,len(friends_list))]} is going to buy the meal today!")