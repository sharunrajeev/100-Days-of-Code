from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.goto(0, -280)
        self.left(90)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)

    def top(self):
        if self.ycor() == 280:
            self.goto(0, -280)
            return True
        else:
            return False
