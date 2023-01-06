from turtle import Turtle


class Game_over(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.write("Game Over", align="center", font=("courier", 24, "bold"))
