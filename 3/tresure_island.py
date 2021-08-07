# Tresure Island

# Welcome screen
print("-------------------------Welcome to------------------------------")
print(" _                                     _     _                 _ \n| |                                   (_)   | |               | |\n| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |\n| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |\n| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |\n \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|\n\n")

print("You have been on an island for a few days and have found a treasure map.\n")
print('Choices are inside " " ')

# Choice 1
choice = input('You have reached the treasure cave! \nIn front of you there is two way "left" and "right". Choose a path.\n')

if choice == 'left' :
    # Choice 2
    choice = input('You need to cross the river. Do you wish to "swim" or "wait" for the falcon to take you to the other side of river?\n')
    if choice == 'wait' :
        # Choice 3
        choice = input('Walk straight and you will reach room with 3 door. "Red" "Blue" "Yellow". Choose any door to move forward.\n')
        if choice == 'Red' :
            print("You are in hell! Burned down Game Over!")
        elif choice == 'Blue' :
            print("There comes ferocious beasts! You have been eaten. Game Over!")
        elif choice == 'Yellow' :
            print("You have found the treasure! Congratulations!")
        else :
            print("There is nothing just dust. Game over!")
    else :
        print("You are attacked by Trout! Game Over!")
else :
    print('Oops! You fell into ditch! Game Over!')
