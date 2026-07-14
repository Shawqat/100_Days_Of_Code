import random

class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list

    def still_has_questions(self):
        try:
            if self.questions_list[self.question_number]:
                return True
        except:
            print("Questions Ended!")
            return False
        
    def next_question(self):
        try:
            question = random.choice(self.questions_list)
            self.question_number += 1
            user_answer = input(f"Q{self.question_number}: {question.text} (True/False):\n").strip().capitalize()
            self.check_answer(user_answer, question.answer)

        except:
            return "error occur!"

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You've got it right")
            self.score += 1
            
        else:
            print("You've got it wrong!")
            print(f"The Correct answer: {correct_answer}")
        print(f"Your current score {self.score}")