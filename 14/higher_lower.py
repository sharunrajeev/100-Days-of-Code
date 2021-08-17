from random import randint
from data import data
from art import logo, vs
from os import system

end = False
score = 0
while not end :
    system('cls')
    print(logo)
    if score!=0 :
        print('You are right! Your score is ' + str(score))
    a = data[randint(0, 49)]
    b = data[randint(0, 49)]
    print(f"\nComapre A : {a['name']}, {a['description']}, from {a['country']}")
    print(vs)
    print(f"Compare B : {b['name']}, {b['description']}, from {b['country']}")
    print("Who has more followers? Type 'A' or 'B'\n")
    answer = input()
    if a['follower_count'] > b['follower_count'] and (answer == 'A' or answer == 'a') :
        score += 1
    elif a['follower_count'] < b['follower_count'] and (answer == 'B' or answer == 'b') :
        score += 1
    else :
        system('cls')
        print(logo)
        print('You are wrong. Your final score is '+str(score))
        end = True
