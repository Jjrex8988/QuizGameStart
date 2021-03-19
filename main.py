from data import question_data
from question_model import Question
from quiz_brain import QuizBrains

question_bank = []
for key in question_data:
    question_text = key['question']
    question_answer = key['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrains(question_bank)


while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")