from question_model import Question
from data import results_easy as Easy, results_medium as Medium, results_hard as Hard
from quiz_brain import QuizBrain

question_bank = []

#Question1 = Question("Hello","Goodbye")

for difficulty_list in (Easy, Medium, Hard):
    for i in difficulty_list:
        question_difficulty = i["difficulty"]
        question_text = i["question"]
        question_answer = i["correct_answer"]
        question_wrong = i["incorrect_answers"]
        question_bank.append(Question(question_difficulty, question_text, question_answer, question_wrong))
    #question_bank.append(Question(text = question_text, answer = question_answer)) # Keyword arguments
    #new_question = Question(question_text, question_answer) # Good for debugging
    #question_bank.append(new_question)

QuizBrain = QuizBrain(question_bank)
QuizBrain.start_game()

while QuizBrain.still_has_question():
    QuizBrain.next_question()
    if not QuizBrain.still_has_question():
        print("You've completed the quiz!")
        print(f"Your final score is: {QuizBrain.score}/{QuizBrain.question_number}")

