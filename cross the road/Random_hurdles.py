import random
import time

COLORS = ["red", "blue", "green", "orange", "yellow", "purple"]
from turtle import Turtle


class Random_Turtle:
    def __init__(self):
        self.speed = 5
        self.chance = None
        self.car = None
        self.Hurdles = []
        self.End = False

    def turtle_generator(self):
        self.chance = random.randint(1, 6)
        if self.chance == 1:
            self.car = Turtle("square")
            self.car.penup()
            self.car.shapesize(stretch_wid=1, stretch_len= 3)
            self.car.color(random.choice(COLORS))
            self.car.goto(x=400, y=random.randint(-170, 170))
            self.Hurdles.append(self.car)

    def car_move(self):
        for car in self.Hurdles:
            car.bk(self.speed)



