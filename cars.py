from turtle import Turtle
import random

colors = ["green", "red", "brown", "white", "pink", "yellow"]
SPEED = 5


class Cars:

    def __init__(self):
        self.segment = Turtle()
        self.all_cars = []
        self.create_segments()
        self.speed = 5

    def move_segments(self):
        for car in self.all_cars:
            car.left(90)
            car.forward(self.speed)
            car.right(90)

    def create_segments(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            self.segment = Turtle()
            self.segment.shape("square")
            self.segment.shapesize(stretch_wid=2, stretch_len=1)
            self.segment.color(random.choice(colors))
            self.segment.penup()
            self.segment.left(90)
            new_y = random.randint(-265, 275)
            self.segment.goto(450, new_y)
            self.all_cars.append(self.segment)

    def speed_up(self):
        self.speed += 1
        self.move_segments()
