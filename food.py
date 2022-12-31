import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.x = random.randint(-270, 270)
        self.y = random.randint(-270, 270)
        self.goto(self.x, self.y)
        self.color("red")
        self.shapesize(0.5)
