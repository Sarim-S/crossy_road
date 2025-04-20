from turtle import Turtle
import random
COLOURS = ["red", "yellow", "green", "blue", "purple"]
START_X = 290
START_SPEED = 5
INCREMENT = 5
CAR_WIDTH = 40


class Cars:
    car_list = []

    def __init__(self):
        self.generate()
        self.speed = START_SPEED

    def generate(self):
        chance = random.randint(1, 6)
        if chance == 1:
            chris = Turtle("square")
            chris.up()
            chris.color(random.choice(COLOURS))
            chris.setheading(180)
            chris.shapesize(stretch_len=2)
            chris.goto(START_X, random.randint(-250, 250))
            self.car_list.append(chris)

    def start_movement(self):
        for car in self.car_list:
            car.forward(random.randint(self.speed, self.speed + 2))

    def check_collision(self, player):
        for car in self.car_list:
            if player.distance(car) < 20:
                return True

    def level_up(self):
        self.speed += INCREMENT
