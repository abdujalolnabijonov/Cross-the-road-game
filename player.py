from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(0, -270)
        self.left(90)

    def up_player(self):
        self.forward(10)

    def down_player(self):
        self.back(10)

    def right_player(self):
        self.right(90)
        self.forward(10)
        self.left(90)

    def left_player(self):
        self.left(90)
        self.forward(10)
        self.right(90)
