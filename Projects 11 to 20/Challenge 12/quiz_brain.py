import random


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def start_game(self):
        valid = ["easy", "medium", "hard"]
        print("Trivia Game")
        while True:
            diff = input("Choose difficulty (Easy, Medium, Hard): ").lower()
            if diff in valid:
                break
            print("Invalid choice. Please choose Easy, Medium, or Hard.")
        while True:
            try:
                num_q = int(input("Choose number of questions: \n"))
                break
            except ValueError:
                print("Numbers only please.")

        random.shuffle(self.question_list)
        filtered_questions = [q for q in self.question_list if q.difficulty == diff]
        self.question_list = filtered_questions[:num_q]

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
            return False
        else:
            print("Wrong answer.")
            print(f"Your current score is: {self.score}/{self.question_number}")
            return True




