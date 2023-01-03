from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.y = None
        self.x = None
        self.inc_dec_y = 0.5
        self.inc_dec_x = 0.5
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        self.x = self.xcor()
        self.y = self.ycor()
        self.goto(self.x + self.inc_dec_x, self.y + self.inc_dec_y)

    def update(self):
        self.inc_dec_y *= -1

    def r_update(self):
        self.inc_dec_x *= -1
        self.inc_dec_y *= -1

    def l_update(self):
        self.inc_dec_x *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.r_update()




