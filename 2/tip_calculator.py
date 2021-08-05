# Welcome message
print("Welcome to the Tip Calculator\n")

# User inputs 
# Total bill recieved
bill = float(input("What was your total bill? ₹"))
# Tip percentage they wish to tip
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
# Number of people attending
people = int(input("How many people to split the bill? "))

# Tip amount calculation
tip = bill * (tip / 100)
# Total bill = Bill + Tip
total_bill = bill + tip

# Final print statement
print(f"Each person should pay: ₹{round(total_bill/people,2)}")