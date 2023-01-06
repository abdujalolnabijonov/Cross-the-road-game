from turtle import Turtle, Screen

screen = Screen()

height_score=[]
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_score()


    def create_score(self):
        self.goto(-359, 275)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Total score is {self.score}", align="center", font=("courier", 12, "bold"))


    def update_score(self):
        self.score += 1
        self.update_scoreboard()
        height_score.append(self.score)

class Height_score:

    def __init__(self):
        self.turtle = Turtle()
        self.file_score()
        self.turtle.goto(-180, 275)
        self.turtle.color("white")
        self.turtle.write(f"Height score:{height_score}", align="center", font=("courier", 12, "bold"))
        self.turtle.hideturtle()

    def file_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(height_score))
