# Program to calculate sum of all even numbers from 1 to 100
# This program uses for loop with range function

sum = 0
for i in range(2, 101, 2):
    sum += i
print(sum)