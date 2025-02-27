from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Snake snack snaking ")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_on = True

screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.down, 'Down')


while game_on:
    screen.update()
    time.sleep(0.1)


    snake.move()

    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q{self.question_number}: {curr_question.text} (True/False): ")
        self.check_answer(user_ans, curr_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)
        # same as
        #return True if self.question_number < len(self.question_list) else False

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("Correct answer.")
            self.score += 1
            print(f"Your current score is: {self.score}/{self.question_number}")


    if snake.snake_head.xcor() > 395 or snake.snake_head.xcor() < -395 or snake.snake_head.ycor() > 395 or snake.snake_head.ycor() < -395:
        scoreboard.game_over()
        game_on = False

    for i in snake.snake[1:]:
        if snake.snake_head.distance(i) < 10:
            game_on = False
            scoreboard.game_over()


# screen.onkey(key="d", fun=turn_clockwise)
# screen.onkey(key="a", fun=turn_counterclockwise)
# screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()

