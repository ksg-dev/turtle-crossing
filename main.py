import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

player = Player()
cars = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.up, "Up")


playing = True
while playing:
    time.sleep(0.1)
    screen.update()

    cars.make_car()
    cars.move()

    # Detect collision w car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            playing = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.finish():
        player.go_to_start()
        cars.level_up()
        scoreboard.level()


screen.exitonclick()
