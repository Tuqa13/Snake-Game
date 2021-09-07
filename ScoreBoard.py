from turtle import Turtle

FONT = ("Courier", 20, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.x = 0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.write(f"Score:  {self.x}", align="center", font=FONT)
        self.speed("fastest")

    def increment(self):
        self.x += 1
        self.clear()
        self.write(f"Score:  {self.x}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("Red")
        self.write("Game Over!", align="center", font=FONT)