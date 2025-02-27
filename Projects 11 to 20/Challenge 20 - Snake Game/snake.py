from turtle import Turtle

# Constants
SNAKE_POSITION = [(0, 0), (-20.0, 0), (-40.0, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        # self.snake_position = [(0, 0), (-20.0, 0), (-40.0, 0)]
        self.snake = []
        # for i in self.snake_position:
        #     square = Turtle("square")
        #     square.color("white")
        #     square.penup()
        #     square.goto(i)
        #     self.snake.append(square)
        self.create_snake()
        self.snake_head = self.snake[0]


    def create_snake(self):
        for i in SNAKE_POSITION:
            self.add_segment(i)

    def move(self):
        for snake_num in range(len(self.snake) - 1, 0, -1):
            next_x = self.snake[snake_num - 1].xcor()
            next_y = self.snake[snake_num - 1].ycor()
            self.snake[snake_num].goto(next_x, next_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def add_segment(self, position):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.snake.append(square)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def up(self):
        if self.snake_head.heading() == 270:
            return
        else:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() == 90:
            return
        else:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_head.heading() == 0:
            return
        else:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_head.heading() == 180:
            return
        else:
            self.snake_head.setheading(0)
