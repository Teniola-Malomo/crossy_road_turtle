import random
from turtle import Turtle

COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(COLOURS[random.randint(0, 5)])
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        random_y = random.randint(-250, 250)
        self.goto(300, random_y)
        self.setheading(180)
        self.current_speed = STARTING_MOVE_DISTANCE

    # def car_collection(self):
    #     for i in range(20):
    #         car = CarManager()
    #         self.cars.append(car.make_car())

    def move(self):
        new_x = self.xcor() - self.current_speed
        self.goto(new_x, self.ycor())

    def increase_speed(self):
        self.current_speed += MOVE_INCREMENT


    # self.cars = []
    #
    # def make_cars(self):
    #     for i in range(7):
    #         cars = CarManager
    #         self.cars.append(cars)

# COLOURS[random.randint(0, 6)]

    # def random_color(self):
    #     r = random.randint(0, 255)
    #     g = random.randint(0, 255)
    #     b = random.randint(0, 255)
    #     colour = (r, g, b)
    #     return colour


