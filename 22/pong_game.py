from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# Paddles
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# Ball
ball = Ball(10, 'white', 10)

# ScoreBoard
sb = Scoreboard()

game_is_running = True


# To exit the game
def stop_game():
    global game_is_running
    game_is_running = False


# Movements
screen.listen()
screen.onkeypress(right_paddle.go_up, 'Up')
screen.onkeypress(right_paddle.go_down, 'Down')
screen.onkeypress(left_paddle.go_up, 'w')
screen.onkeypress(left_paddle.go_down, 's')
screen.onkeypress(stop_game, 'e')


while game_is_running:
    time.sleep(ball.movement_speed)
    screen.update()
    ball.move()
    sb.score_display()

    # Detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce('y')

    # Detect collision with paddle
    if (ball.xcor() > 320 and ball.distance(right_paddle) < 50) or (
            ball.xcor() < -320 and ball.distance(left_paddle) < 50):
        ball.movement_speed *= 0.9
        ball.bounce('x')

    # scoring points
    if ball.xcor() > 390:
        sb.score('left')
        ball.reset_position()

    if ball.xcor() < -390:
        sb.score('right')
        ball.reset_position()

screen.exitonclick()
