import time
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Check if snake collides with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.add_point()
        scoreboard.score_board()

    # Check if snake collides with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # Check if snake collides with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            scoreboard.game_over()
            game_is_on = False
screen.exitonclick()
