import random
from turtle import Turtle, Screen


class Snake:
    def __init__(self):
        self.start_snakes = 3
        self.x = self.y = 0
        self.snake_list = []
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.setup(height=600, width=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")

    def add_snake(self):
        for snake in range(self.start_snakes):
            self.snake_list.append(Turtle("circle"))
            for i in self.snake_list[1:]:
                i.shapesize(0.5)
                print(i.pensize())

            self.snake_list[0].shape("classic")
            self.snake_list[snake].penup()
            self.snake_list[snake].pencolor("white")
        for pos in range(len(self.snake_list)):
            self.snake_list[pos].goto(self.x, self.y)
            self.x -= 10

    def extend(self):
        self.start_snakes+=1
        self.snake_list.append(Turtle("circle"))
        self.snake_list[self.start_snakes-1].setheading(self.snake_list[self.start_snakes-2].heading())
        self.snake_list[self.start_snakes-1].pencolor("white")
        self.snake_list[self.start_snakes-1].penup()
        self.snake_list[self.start_snakes - 1].shapesize(0.5)
        self.snake_list[self.start_snakes-1].goto(self.x, self.y)
        self.x -= 10


    def move(self):
        for move in range(len(self.snake_list) - 1, 0, -1):
            self.x = self.snake_list[move - 1].xcor()
            self.y = self.snake_list[move - 1].ycor()
            self.snake_list[move].goto(self.x, self.y)
        self.snake_list[0].fd(10)
