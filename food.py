from turtle import Turtle
import random

COLORS = ["#FF4848", "#FFD371", "#28FFBF", "#D62AD0", "#FC5404"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.x = random.randint(-270, 270)
        self.y = random.randint(-270, 270)
        self.create_food()

    def create_food(self):
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(0.5)
        self.shape("circle")
        self.speed("fastest")
        self.goto(x=self.x, y=self.y)

    def change_position(self):
        self.color(random.choice(COLORS))
        self.x = random.randint(-270, 270)
        self.y = random.randint(-270, 270)
        self.goto(x=self.x, y=self.y)

