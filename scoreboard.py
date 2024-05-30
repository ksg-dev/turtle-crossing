from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
GAMEOVER = ("Courier", 40, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score}", font=FONT)

    def level(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=GAMEOVER)
