import turtle
from turtle import Turtle, Screen
from random import randint

is_race_on = False
sc = Screen()
sc.setup(width=500, height=400)
user_bet = sc.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter your color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

turtles = []
for i in range(6):
    turtles.append(Turtle(shape='turtle'))
    turtles[i].color(colors[i])
    turtles[i].penup()
    # goto - positions the turtle to the (x,y) position
    turtles[i].goto(x=-230, y=100-(i*40))

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You have won the bet! The {winning_color} is the winner.')
            else:
                print(f'You have lost the bet! The {winning_color} is the winner.')
        random_distance = randint(0,10)
        turtle.forward(random_distance)

sc.exitonclick()
