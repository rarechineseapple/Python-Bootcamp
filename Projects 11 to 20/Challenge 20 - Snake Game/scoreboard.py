from turtle import Turtle

# constants

ALIGNED = "center"
FONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 375)
        self.write(f"Scoreboard = {self.score}", align=ALIGNED, font=FONT)
        self.hideturtle()


    def increase_score(self):

        self.score += 1
        self.clear()
        self.write(f"Scoreboard = {self.score}", align=ALIGNED, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", align=ALIGNED, font=FONT)

