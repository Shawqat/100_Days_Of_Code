from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions_bank = []

for question in question_data :
    questions_bank.append(Question(question["text"], question["answer"]))

ask = QuizBrain(questions_bank)

while ask.still_has_questions():
    ask.next_question()
