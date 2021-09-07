from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, i):
        x = Turtle(shape="square")
        x.color("#FEFBF3")
        x.penup()
        x.goto(i)
        self.segment.append(x)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):

        for seg in range(len(self.segment) - 1, 0, -1):
            pos = self.segment[seg - 1]
            self.segment[seg].goto(pos.xcor(), pos.ycor())
        self.segment[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segment[0].heading() != 270:
            self.segment[0].setheading(90)

    def down(self):
        if self.segment[0].heading() != 90:
            self.segment[0].setheading(270)

    def left(self):
        if self.segment[0].heading() != 0:
            self.segment[0].setheading(180)

    def right(self):
        if self.segment[0].heading() != 180:
            self.segment[0].setheading(0)
