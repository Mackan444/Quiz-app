# Marcus Lycke
# Teinf-20
# Quiz
# 16-03-2022

from Quiz_questions import question_data
from Quiz import Question
from Quiz import Quiz

#Classes

question_bank = []
for q in question_data:
    question_text = q["question"]
    question_answer = q["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)

while quiz.remaining_questions():
    quiz.next_question()

print("Game Over. Well played!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}\n")

"""

    ║   ║ ║
    ║║ ║║ ║
    ║ ║ ║ ║
    ║   ║.╚════

"""
"""
from secrets import choice
from Resources import Questions, Quiz


def main():
    question_bank = []

    question1 = Questions("Who is tallest in the class/Tim/Tim, Jesper, Marcus, Oliver")
    question2 = Questions("")
    question3 = Questions("")
    question4 = Questions("")
    question5 = Questions("")

    
    question_bank.append(question1)
    question_bank.append(question2)
    question_bank.append(question3)
    question_bank.append(question4)
    question_bank.append(question5)


    quiz = Quiz("The Quiz", question_bank, 0)

    print(f"Welcome to {quiz.get_name()}\n")

    while len(question_bank) != 0:
        current_question = choice(question_bank)
        print(current_question.get_question)
"""