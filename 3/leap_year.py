# Program to find leap year

# Accept year from user
year = int(input("Enter year: "))

# To find whether year is leap year or not
# Condition 1: If the number is divisible by 4, it is a leap year
# Condition 2: If the number is not divisible by 4, it is not a leap year
# Condition 3: If the number is divisible by 100, it is not a leap year
# Condition 4: If the number is not divisible by 400, it is a leap year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")
