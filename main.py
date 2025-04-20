from turtle import Screen
import time
from player import Player, STARTING_POS
from car import Cars
from Scoreboard import Scoreboard

number_of_cycles = 0
level = 1
lives = 3

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.listen()
screen.tracer(0)

scoreboard = Scoreboard(level_number=level)
life_counter = Scoreboard()
life_counter.print_lives(lives)

tim = Player()

car = Cars()

game_on = True

while game_on:
    car.generate()
    car.start_movement()
    screen.onkey(fun=tim.move, key="Up")
    screen.update()
    number_of_cycles += 1
    time.sleep(0.05)

    # detect collisions
    if car.check_collision(tim):
        time.sleep(0.25)
        lives -= 1
        tim.goto(STARTING_POS)
        life_counter.print_lives(lives)
        if lives == 0:
            screen.clear()
            scoreboard.game_over(level)
            break

    # check if done level
    if tim.done_level():
        time.sleep(0.5)
        level += 1
        scoreboard.write_level(level)
        car.level_up()


screen.exitonclick()
