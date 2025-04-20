from turtle import Turtle
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self, level_number=1):
        super().__init__()
        self.write_level(level_number)

    def write_level(self, level_number):
        self.clear()
        self.up()
        self.goto(-230, 270)
        self.write(f"Level:  {level_number}", align="center", font=FONT)
        self.ht()

    def game_over(self, final_level):
        self.home()
        self.write("Game over :(", align="center", font=FONT)
        self.goto(0, -100)
        self.write(f"LEVEL : {final_level}", align="center", font=FONT)

    def print_lives(self, lives):
        life_display = ""
        for i in range(lives):
            life_display += "♥ "
        self.clear()
        self.up()
        self.goto(230, 270)
        self.write(f"Lives:  {life_display}", align="center", font=("Times New Roman", 15, "normal"))

