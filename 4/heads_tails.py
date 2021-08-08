# Heads or Tails generator
# This program is a virtual coin flip game.
from random import randint

def toss_coin() :
    if randint(0,1) :
        print("Heads")
    else :
        print("Tails")

print("Tossing coin ...")
toss_coin()