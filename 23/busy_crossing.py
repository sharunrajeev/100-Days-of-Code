import time
from turtle import Screen
from player import Player
from car_managers import CarManager
from scoreboard import ScoreBoard
is_playing = True

sc = Screen()
sc.screensize(canvwidth=600, canvheight=600, bg='#000027')
sc.tracer(0)

# Torto the player name
torto = Player()
manager = CarManager()
scoreboard = ScoreBoard()

# Torto movements
sc.onkeypress(torto.move_up, key="Up")
sc.onkeypress(torto.move_down, key="Down")
sc.listen()

while is_playing:
    time.sleep(0.1)
    sc.update()
    manager.create_car()
    manager.move()

    # Detect collision
    for car in manager.cars:
        if car.distance(torto) < 20:
            scoreboard.game_over()
            is_playing = False

    # Successful crossing
    if torto.top():
        manager.incr_speed()
        scoreboard.level_up()

sc.exitonclick()
