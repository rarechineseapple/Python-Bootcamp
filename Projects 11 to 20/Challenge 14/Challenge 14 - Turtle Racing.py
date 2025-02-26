import random
from turtle import Turtle, Screen

# timmy_turtle = Turtle()
# timmy_turtle.shape("turtle")
# timmy_turtle.penup()
# timmy_turtle = Turtle()

start_race = False
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtle_position = [-70, -40, -10, 20, 50, 80, 110]
turtle_stable = []

for i in range(0, 7):
    timmy = Turtle(shape="turtle")
    timmy.color(colors[i])
    timmy.penup()
    timmy.goto(x=-240, y = turtle_position[i])
    turtle_stable.append(timmy)

# x = turtles_stable.keys()
# print(x)

screen = Screen()
screen.setup(500, 400)
bet = screen.textinput(title= "Place your bet!", prompt= "Pick a turtle color: ")

if bet:
    start_race = True

while start_race:

    for racer in turtle_stable:
        if racer.xcor() > 240:
            start_race = False
            win_turtle = racer.pencolor()
            if win_turtle == bet:
                print(f"You won")
            else:
                print(f"You lost. The {win_turtle} is the winner.")


        rand_dist = random.randint(0,10)
        racer.forward(rand_dist)

# timmy_turtle.goto(x=-240, y= -100)

screen.listen()

screen.exitonclick()