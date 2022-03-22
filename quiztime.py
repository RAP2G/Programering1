# Soma Szabo
# INF20
# 16-03-2022
# Quiz Time

# Imports

from random import shuffle, randint


# Classes

class Question:
    def __init__(self, question: str, answer: str, alts: list) -> None:
        """
        This class takes in a name:str, an answer:str and alternative answers:list

        """
        self.question = question
        self.answer = answer
        self.alts = alts

    def check_answer(self, ans: str):
        """
        Checks if the answer given is correct

        """
        if self.answer.lower() == ans.lower():
            return True
        else:
            return False

    def ask_question(self):
        print(self.question)
        print()
        if len(self.alts) <= 3:
            answers = [self.answer]
            for i in self.alts:
                answers.append(i)
            shuffle(answers)
            print("Answers: ", end="")
            for x in answers:
                if x == answers[len(answers)-1]:
                    print(f"        {x}")
                else:
                    print(f"        {x}", end="")
        else:
            answers = [self.answer]
            shuffle(self.alts)
            for i in range(3):
                answers.append(self.alts[i])
            shuffle(answers)
            print("Answers: ", end="")
            for x in answers:
                if x == answers[len(answers)-1]:
                    print(f"    {x}")
                else:
                    print(f"    {x}", end="")


class Quiz:

    def __init__(self, name: str, questions: list) -> None:
        self.name = name
        self.questions = questions
        self.asked = []
        self.points = 0

    def ask_question(self):
        question_number = randint(0, len(self.questions)-1)
        question = self.questions[question_number]
        self.asked.append(self.questions.pop(question_number))
        question.ask_question()
        if question.check_answer(input(f"Answer: ")):
            print("Well Done")
            return True
        else:
            print("Wrong Answer")
            return False

    def get_name(self):
        return self.name

    def reset(self):
        self.questions.extend(self.asked)
        self.asked = []

    def get_quiz_length(self):
        return len(self.questions)

    def get_asked_length(self):
        return len(self.asked)


def create_quiz(name, quiz_file):
    questions = []
    with open(f"{quiz_file}") as file:
        for ques in file.readlines():
            params = ques.split("/")
            questions.append(
                Question(params[0], params[1], params[2].split(",")))
    return Quiz(name, questions)


def game(quiz: list):
    points = 0
    for i in quiz:
        print(i.get_name(), end="   ")
    print("")
    quiz_chouice = int(input("Which quiz would you like to play? "))-1
    current_quiz = quiz[quiz_chouice]
    for i in range(current_quiz.get_quiz_length()):
        if current_quiz.ask_question():
            points += 1
    print("")
    print(f"{points}/{current_quiz.get_asked_length()} points")
    current_quiz.reset()


def main():
    while True:
        quizzes = []
        quizzes.append(create_quiz("Quiz1", "quiz_1.txt"))
        game(quizzes)
        inp = input("Would you like to continue?y/n")
        if inp.lower() == "n":
            break


if __name__ == "__main__":
    main()
