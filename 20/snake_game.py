import time
from turtle import Screen
from snake import Snake

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = 0
while game_is_on != 400:
    screen.update()
    time.sleep(0.5)
    snake.move()
    game_is_on += 1


screen.exitonclick()
