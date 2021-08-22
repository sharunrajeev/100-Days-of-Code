from turtle import Turtle, Screen

arrow_head = Turtle()
arrow_head.shape('arrow')
for _ in range(4):
    arrow_head.forward(100)
    arrow_head.left(90)

screen = Screen()
screen.exitonclick()

