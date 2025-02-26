from turtle import Turtle, Screen

timmy_turtle = Turtle()
timmy_turtle.shape("turtle")

def move_forwards():
    timmy_turtle.forward(10)

def move_backwards():
    timmy_turtle.backward(10)

def turn_clockwise():
    timmy_turtle.right(10)

def turn_counterclockwise():
    timmy_turtle.left(10)

def clear_screen():
    timmy_turtle.clear()
    timmy_turtle.penup()
    timmy_turtle.home()
    timmy_turtle.pendown()

screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="a", fun=turn_counterclockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()