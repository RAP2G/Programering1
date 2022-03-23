# Soma Szabo
# INF20
# 16-03-2022
# Quiz Time

# Imports

from random import shuffle, randint
from os import listdir
from os.path import isfile, join


# Classes


class Question:
    def __init__(self, question: str, answer: str, alts: list) -> None:
        """
        This class requires three parameters: a question:str, an answer:str and alternative answers:list

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
        """
        This method print out the question and the answers which the user can choose from.

        """
        print(self.question)
        print()
        if len(self.alts) <= 3:
            """
            Prints out the real answer and all available alternatives if there are 3 or less alternatives
            """
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
            """
            Prints out the answer and 3 random alternatives from a shuffled list of alternatives
            """
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
        """
        This class requires two parameters: a name:str and a list of question objects:list
        """
        self.name = name
        self.questions = questions
        self.asked = []
        self.points = 0

    def ask_question(self):
        """
        Calls on the ask_question method of a random question object.
        Then asks the user for input which is then validated using the question objects check_answer method.
        Returns true if check_answer is true
        Returns false otherwise
        """
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
        """
        Returns the name of object
        """
        return self.name

    def reset(self):
        """
        'Resets' the quiz by appending all of the asked questions back to the question list
        """
        self.questions.extend(self.asked)
        self.asked = []

    def get_quiz_length(self):
        """
        Returns the length of the list questions 

        """
        return len(self.questions)

    def get_asked_length(self):
        """
        Returns the length of the list questions 

        """
        return len(self.asked)


def load_quiz():
    name = ""
    questions = []
    quizzes = []
    onlyfiles = [f for f in listdir(
        "Quiz_Folder") if isfile(join("Quiz_Folder", f))]
    for i in onlyfiles:
        with open(f"Quiz_Folder/{i}") as file:
            name = file.readline().strip()
            for ques in file.readlines():
                params = ques.split("/")
                questions.append(
                    Question(params[0], params[1], params[2].strip().split(",")))
        quizzes.append(Quiz(name, questions))
        questions = []
    return quizzes


def create_quiz():
    quizzes = []
    while True:
        print("Would you like to create a quiz? y/n ")
        inp = input("Answer: ")
        if inp.lower() == "y":
            name = input("Name your quiz: ")
            questions = []
            while True:
                question = input("Input a question: ")
                answer = input("Input the answer to the question: ")
                alternatives = []
                while True:
                    alternatives.append(input("Input an alternative answer: "))
                    inp = input(
                        "Would you like to add another alternative? y/n ")
                    if inp.lower() == "y":
                        pass
                    else:
                        break
                questions.append(Question(question, answer, alternatives))
                inp = input("Would you like to add another question? y/n ")
                if inp.lower() == "y":
                    pass
                else:
                    break
            quizzes.append(Quiz(name, questions))
            with open(f"Quiz_Folder/{name}.txt", "a") as f:
                f.write(f"{name}\n")
                for i in questions:
                    alts = i.alts
                    savable_alts = ''
                    for k in alts:
                        if k == alts[len(alts)-1]:
                            savable_alts += k
                        else:
                            savable_alts += f"{k},"
                    save_string = f"{i.question}/{i.answer}/{savable_alts}\n"
                    f.write(save_string)
        else:
            return quizzes
            break


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
    quizzes = []
    quizzes.extend(create_quiz())
    quizzes.extend(load_quiz())
    while True:
        game(quizzes)
        inp = input("Would you like to continue?y/n ")
        if inp.lower() == "n":
            print("Good bye!")
            break


if __name__ == "__main__":
    main()
