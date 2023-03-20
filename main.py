from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_ques = Question(text = question_text, answer = question_answer)
    question_bank.append(new_ques)
# print(question_bank[5].answer)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()