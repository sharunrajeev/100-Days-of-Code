import turtle as t
from random import randint


def get_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    generated_color = (r, g, b)
    return generated_color


pt = t.Turtle()
pt.speed('fastest')
t.colormode(255)
for i in range(72):
    pt.color(get_random_color())
    pt.circle(100)
    pt.setheading(5*i)
sn = t.Screen()
sn.exitonclick()

