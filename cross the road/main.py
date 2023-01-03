import time
from turtle import Screen, Turtle
from Random_hurdles import *
from scoreboard import Score


# METHODS
def up():
    Timmy.fd(10)


def down():
    Timmy.bk(10)


screen = Screen()
Timmy = Turtle()
rand = Random_Turtle()

screen.tracer(0)
screen.setup(800, 500)
screen.bgcolor("grey")

Timmy.shape("turtle")
Timmy.penup()
Timmy.setheading(90)
Timmy.goto(0, -220)

screen.listen()
screen.onkeypress(key="Up", fun=up)
screen.onkeypress(key="Down", fun=down)

level = Score()
Ended = False
while not Ended:
    time.sleep(0.1)
    screen.update()
    rand.turtle_generator()
    rand.car_move()
    for car in range(len(rand.Hurdles)):
        if rand.Hurdles[car].distance(Timmy) < 20:
            level.Game_over()
            Ended = True
    if Timmy.ycor() > 210:
        level.level_up()
        rand.speed += 3
        Timmy.goto(0, -220)

screen.exitonclick()
