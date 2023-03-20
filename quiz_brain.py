
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            if self.question_number != 0:
                print(f"Your current score is :{self.score}/{self.question_number}\n")
            return True
        else:
            print(f"\n\nYou completed the quiz.\nYour final score is :{self.score}/{self.question_number}")
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        a = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(a,current_question.answer)

    def check_answer(self, user_answer, right_answer):
        if user_answer.lower() == right_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Your answer is wrong!")
        print(f"The correct answer is {right_answer}.")


