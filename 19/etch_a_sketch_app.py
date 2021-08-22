from turtle import Turtle, Screen

pt = Turtle()
sc = Screen()


def move_forwards():
    pt.forward(10)


def move_backwards():
    pt.back(10)


def move_clockwise():
    heading = pt.heading() + 10
    pt.setheading(heading)


def move_anti_clockwise():
    heading = pt.heading() - 10
    pt.setheading(heading)


def clear_screen():
    pt.clear()
    pt.penup()
    pt.home()
    pt.pendown()


sc.onkeypress(key='w', fun=move_forwards)
sc.onkeypress(move_backwards, 's')
sc.onkeypress(move_anti_clockwise, 'a')
sc.onkeypress(move_clockwise, 'd')
sc.onkey(clear_screen, 'c')
sc.listen()
sc.exitonclick()
