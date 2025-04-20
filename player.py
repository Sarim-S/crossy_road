from turtle import Turtle
STARTING_POS = (0, -280)
MOVE_AMOUNT = 10
FINISH_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.generate()

    def generate(self):
        self.shape("turtle")
        self.up()
        self.setheading(90)
        self.goto(STARTING_POS)

    def move(self):
        if self.ycor() < FINISH_Y:
            self.forward(MOVE_AMOUNT)

    def done_level(self):
        if self.ycor() == FINISH_Y:
            self.goto(STARTING_POS)
            return True

