from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(-350, 280)
        self.write(f"Level : {self.level}", align='left', font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level : {self.level}", align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER !", align='center', font=FONT)
