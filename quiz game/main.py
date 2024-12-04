from question_model import QuizBrain
from data import question_data
from quiz_brain import Question

# Create a list of Question objects
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initialize QuizBrain
quiz = QuizBrain(question_bank)

# Run the quiz
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
