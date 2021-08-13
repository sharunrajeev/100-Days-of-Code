# Program that mock the Blind Auction
# The highest bid gets the prize.

# to print logo 
from logo import logo
# system to clear the screen
from os import system
bid_collection = []
proceed = True
while proceed :
    system('cls')
    print("Welcome to the secret auction program.")
    print(logo)
    name = input("\nWhat is your name ? : ")
    bid = input("What's your bid ? : ")
    bid_collection.append({
        'name' : name,
        'bid' : bid
    })
    proceed = input("Are there any other bidders ? Type 'yes' or 'no' : ")
    if proceed == 'yes' :
        proceed = True
    else :
        proceed = False

max_bid = bid_collection[0]
for i in bid_collection :
    if i['bid'] > max_bid['bid'] :
        max_bid = i

print(f"\nThe highest bidder is {max_bid['name']} with bid amount of ₹{max_bid['bid']}")