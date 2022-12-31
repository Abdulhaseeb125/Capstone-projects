from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        self._score = 0

        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)

    def Refresh(self):
        self._score += 1
        self.write(f"Score = {self._score}", font=("", 20, "normal"), align="center")

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over \n Score = {self._score}", align="center", font=("Arial", 20, "normal"))
