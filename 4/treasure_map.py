# Treasure map
# This program will mark place where there is treasure.

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
# Combibing all the rows into a list.
map = [row1, row2, row3]
# Printing map with next line at end of each row
print(f"{row1}\n{row2}\n{row3}")
# User input
position = input("Where do you want to put the treasure? ")
map[int(position[1])-1][int(position[0])-1] = "X"
print(f"{row1}\n{row2}\n{row3}")