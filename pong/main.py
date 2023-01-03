import time
from turtle import Screen
from paddles import Paddles
from ball import Ball
from scoreboard import *

'''required methods'''
def right_up():
    """Makes left paddle move up"""
    paddles.left_paddle.fd(20)


def right_down():
    """Makes paddle move down"""
    paddles.left_paddle.bk(20)

def left_up():
    """Makes right paddle move up"""
    paddles.right_paddle.fd(20)


def left_down():
    """Makes right paddle move down"""
    paddles.right_paddle.bk(20)


'''screen setup'''

screen = Screen()
screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor("black")

"""Objects"""

paddles = Paddles()
ball = Ball()
score = Score()

"""Variables"""

Ended = False
r_scores = 0
l_scores = 0

"""keys setup"""
screen.listen()
screen.onkeypress(key="w", fun=right_up)
screen.onkeypress(key="s", fun=right_down)
screen.onkeypress(key="Up", fun=left_up)
screen.onkeypress(key="Down", fun=left_down)
"""Function calls"""
paddles.Right_paddle()

""" Mian loop """
while not Ended:
    # -------makes right paddle auto move
    # -------paddles.p_auto_move()
    ball.move()
    # Collision detectors
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.update()
    if paddles.right_paddle.distance(ball) < 50 and ball.xcor() > 340:
        ball.r_update()
    if ball.distance(paddles.left_paddle) < 50 and ball.xcor() < -340:
        ball.l_update()

    if ball.xcor() > 350:
        # Ball will reset if it misses the paddle
        l_scores += 1
        score.lp(l_scores)
        ball.reset_ball()
        ball.update()
    if ball.xcor() < -350:
        # Ball will reset if it misses the paddle
        r_scores += 1
        score.rp(r_scores)
        ball.reset_ball()
        ball.update()


    time.sleep(.001)
    screen.update()
"""screen exit"""
screen.exitonclick()