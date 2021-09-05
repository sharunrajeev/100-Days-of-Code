import random
from turtle import Turtle
from random import randint

# Constants
COLORS = ['red', 'orange', 'yellow', 'green', 'violet', 'blue']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.y_position = 0
        self.cars = []
        self.car_speed = 10

    def create_car(self):
        random_chance = randint(0, 5)
        if random_chance == 1:
            car = Turtle('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            self.random_y_position()
            car.goto(350, self.y_position)
            self.cars.append(car)

    def random_y_position(self):
        self.y_position = randint(-20, 20) * 10

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def incr_speed(self):
        self.car_speed += STARTING_MOVE_DISTANCE
