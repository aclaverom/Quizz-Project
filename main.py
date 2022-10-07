
from quiz_brain import QuizzBrain
from question_model import Question
from data import question_data

question_bank =[]
end_of_game = False 
for question in question_data:
    question_text = question["question"] 
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[0].answer)

quiz = QuizzBrain(question_bank)


while quiz.still_have_question ():
    quiz.next_question()
    
  
print("You`ve completed the quizz")    
print(f"Your final score was : {quiz.score} /{quiz.question_number} ")