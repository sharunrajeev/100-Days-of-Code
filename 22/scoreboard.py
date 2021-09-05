from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def score(self, player):
        if player == 'left':
            self.l_score += 1
        if player == 'right':
            self.r_score += 1

    def score_display(self):
        self.clear()
        self.goto(0, 200)
        self.write(f'{self.l_score}   {self.r_score}', align='center', font=('Courier', 50, 'normal'))
