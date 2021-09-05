import time
from turtle import Turtle


class Ball(Turtle):
    def __init__(self, radius, color, speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius / 10)
        self.radius = radius
        self.color(color)
        self.speed(speed)
        self.x_move = 10
        self.y_move = 10
        self.movement_speed = 0.1

    def move(self):
        self.penup()
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce(self, direction):
        if direction == 'y':
            self.y_move *= -1
        if direction == 'x':
            self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.movement_speed = 0.1
        self.bounce('x')
