from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.Level = 1
        self.penup()
        self.goto(-250, 210)
        self.hideturtle()
        self.write(f"Level {self.Level}", font=("arial", 20, "normal"))


    def level_up(self):
        self.clear()
        self.Level += 1
        self.write(f"Level {self.Level}", font=("arial", 20, "normal"))

    def Game_over(self):
        self.goto(-70, 0)
        self.write("Game Over.", font=("arial", 20, "normal"))
