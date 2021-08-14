from blackjack_art import logo
from os import system
import random

# Get a random card from the deck
def get_card() :
    card =[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card)

start = True if input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ") == 'y' else False
while start :
    system('cls')
    print(logo)
    print("\nWelcome to the Blackjack game!")

    # player data
    player_card = []
    player_score = 0

    # computer data
    computer_card = []

    # generate random card to player and computer
    for i in range(2):
        player_card.append(get_card())
        computer_card.append(get_card())

    another_card = True
    while another_card :
        # generate player and computer scores
        player_score = sum(player_card)
        computer_score = sum(computer_card)

        print(f"\tYour cards : {player_card}, current score : {player_score}")
        print(f"\tComputer's first card : {computer_card[0]}")

        another_card = True if input("Type 'y' to get another card, type 'n' to pass : ")=='y' else False

        if another_card :   # Hit
            player_card.append(get_card())
            # if after adding new card, the sum is greater than 21, then check if there is an ace, if yes, then change the score of the ace to 1
            if player_score > 21 and 11 in player_card:
                player_card[player_card.index(11)] = 1
            
            # if player score is over 21, player loses
            if sum(player_card) > 21 :    
                print(f"\n\tYour final hand : {player_card}, final score : {sum(player_card)}")
                print(f"\tComputer's final hand : {computer_card}, final score : {sum(computer_card)}")
                print("\nYou lose!")
                another_card = False
        else :              # Stand
            print(f"\tYour cards : {player_card}, current score : {sum(player_card)}")
            print(f"\tComputer's first card : {computer_card[0]}")
            
            # if after adding new card, the sum is greater than 21, then check if there is an ace, if yes, then change the score of the ace to 1
            if computer_score > 21 and 11 in computer_card:
                computer_card[computer_card.index(11)] = 1

            if sum(computer_card) > sum(player_card) :
                print(f"\n\tYour final hand : {player_card}, final score : {sum(player_card)}")
                print(f"\tComputer's final hand : {computer_card}, final score : {sum(computer_card)}")
                print("\nYou lose!")
                another_card = False
            else :
                while sum(computer_card) < 16 :
                    computer_card.append(get_card())
                print(f"\n\tYour final hand : {player_card}, final score : {sum(player_card)}")
                print(f"\tComputer's final hand : {computer_card}, final score : {sum(computer_card)}")
                if sum(computer_card) > 21 :
                    print("\nYou win!")
                    another_card = False
                elif sum(computer_card) == 21 and sum(player_card) < 21 :
                    print("\nYou lose!")
                    another_card = False
                elif sum(computer_card) == sum(player_card) :
                    print("\nYou draw!")
                    another_card = False
                else :
                    if sum(computer_card) > sum(player_card) :
                        print("\nYou lose!")
                        another_card = False
                    else :
                        print("\nYou win!")
                        another_card = False
    start = True if input("Do you want to play again? Type 'y' or 'n' : ") == 'y' else False