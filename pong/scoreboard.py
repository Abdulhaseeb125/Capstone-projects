from turtle import Turtle

class Score:
    def __init__(self):
        self.lp_score = self.rp_score = 0
        self.l_p = Turtle()
        self.r_p = Turtle()
        self.l_p.color("white")
        self.r_p.color("white")
        self.r_p.penup()
        self.l_p.penup()
        self.l_p.goto(-50, 270)
        self.r_p.goto(50, 270)
        self.l_p.hideturtle()
        self.r_p.hideturtle()

    def lp(self,l_s):

        self.l_p.clear()
        self.l_p.write(arg=l_s, font=("Arial", 20, "normal"), align="center")

    def rp(self, r_s):
        self.r_p.clear()
        self.r_p.write(arg=r_s, font=("Arial", 20, "normal"), align="center")

