from turtle import Turtle, Screen
colors = ["#E3170A", "#A9E5BB", "#FCF6B1", "#F7B32B", "#2D1E2F", "#297045", "#204E4A"]
pt = Turtle()
pt.pensize(5)
side = 4
while side != 11:
    angle = 360/side
    pt.color(colors[side-4])
    for _ in range(side):
        pt.right(angle)
        pt.forward(100)
    side += 1

sc = Screen()
sc.exitonclick()
