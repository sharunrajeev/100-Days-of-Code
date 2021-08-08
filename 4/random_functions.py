# Random Number Generator 
import random

start, end = int(input("Enter the start and end of the range: ")), int(input())

# using randint
random_integer = random.randint(start, end)

# using random()
random_float = random.random()
# returns a random floating point number in the range 0.00 to 1.00

n = 10
# for random numbers between 0 and n 
random_float = random.random() * n