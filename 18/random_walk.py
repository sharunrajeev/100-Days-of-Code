import turtle as t
from random import randint

pt = t.Turtle()
pt.pensize(5)
pt.speed(10)
t.colormode(255)
directions = [0, 90, 180, 270]


def get_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    generated_color = (r, g, b)
    return generated_color


count = 0
while count != 50:
    pt.color(get_random_color())
    pt.forward(30)
    pt.setheading(directions[randint(0, 3)])
    count += 1

sc = t.Screen()
sc.exitonclick()
