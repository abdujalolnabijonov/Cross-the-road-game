from turtle import Screen
from player import Player
from cars import Cars
import time
from game_over import Game_over
from scoreboard import Score, Height_score

screen = Screen()
screen.tracer(0)
screen.setup(900, 600)
screen.bgcolor("black")
screen.listen()


player = Player()
cars = Cars()
score = Score()


screen.onkey(player.up_player, "w")
screen.onkey(player.down_player, "s")
screen.onkey(player.right_player, "d")
screen.onkey(player.left_player, "a")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    cars.create_segments()
    cars.move_segments()

    for ca in cars.all_cars:
        if ca.distance(player) < 23:
            game_over = Game_over()
            game_is_on = False
    if player.ycor() > 310:
        player.goto(0, -270)
        cars.speed_up()
        score.update_score()


screen.exitonclick()
