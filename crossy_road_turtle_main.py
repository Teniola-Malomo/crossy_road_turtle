import time
from turtle import Screen
from player import Player
from my_turtle_crossing_game.car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Crossy Road Turtle")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkeypress(player.move_up, "Up")

scoreboard = Scoreboard()

car_collection = []
game_on = True
counter = 6
car_speed = 0.1
while game_on:
    time.sleep(car_speed)
    screen.update()

    if counter % 6 == 0:
        car = CarManager()
        car_collection.append(car)
        counter = 0

    for car in car_collection:
        if (car.xcor() - 30) <= player.xcor() <= (car.xcor() + 25) and (car.ycor() - 15) <= player.ycor() <= (car.ycor() + 20):
            game_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.reset_position()
        scoreboard.new_level()
        car_speed *= 0.7

    for car in car_collection:
        car.move()
        if car.xcor() < -400:
            car_collection.remove(car)

    counter += 1

screen.exitonclick()