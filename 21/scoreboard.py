from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0.0, 250.0)
        self.hideturtle()
        self.color('white')
        self.score_board()

    def add_point(self):
        self.score += 1

    def score_board(self):
        self.clear()
        self.write(arg=f'Score : {self.score}', align='center', font=('Arial', 24, 'normal'))

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(arg=f'Game Over', align='center', font=('Arial', 24, 'normal'))