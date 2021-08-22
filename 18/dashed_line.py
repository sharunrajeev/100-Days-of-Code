from turtle import Turtle as te, Screen as sn
pointy = te()
for i in range(10):
    pointy.pendown()
    pointy.forward(10)
    pointy.penup()
    pointy.forward(10)
screen = sn()
screen.exitonclick()
