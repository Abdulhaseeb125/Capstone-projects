import time
from turtle import Turtle
X_COR = 368
class Paddles:
    def __init__(self):
        """
            Left paddle creation and setup
           along with right paddle creation only
        """
        self.increment = 0.5
        self.right_paddle = Turtle("square")
        self.left_paddle = Turtle("square")
        self.left_paddle.color("white")
        self.left_paddle.shapesize(stretch_wid=0.8, stretch_len=5)
        self.left_paddle.penup()
        self.left_paddle.goto(x=-360, y=0)
        self.left_paddle.setheading(90)



    def Right_paddle(self):
        """
        Right Paddle set up
        The auto mover.
        ":return:
        """
        self.right_paddle.penup()
        self.right_paddle.color("white")
        self.right_paddle.setheading(90)
        self.right_paddle.goto(360, 0)
        self.right_paddle.shapesize(stretch_len=5, stretch_wid=0.8)


    # def p_auto_move(self):
    #     """The  auto mover"""
    #     self.right_paddle.goto(360, self.right_paddle.ycor()+self.increment)
    #     if self.right_paddle.ycor() > 260:
    #         self.increment *= -1
    #     elif self.right_paddle.ycor() < -260:
    #         self.increment *= -1






