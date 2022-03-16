# Soma Szabo
# INF20
# 16-03-2022
# Quiz Time

# Imports

from random import shuffle, choice


# Classes

class Question:
    def __init__(self, question: str, answer: str, alts: list) -> None:
        self.question = question
        self.answer = answer
        self.alts = alts

    def check_answer(self, ans: str):
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
        self.points = 0

    def answer(self, quest):
        if quest.check_answer():
            print("You did well")
            self.points += 1
        else:
            print("Wrong LOL")

    def get_question(self):
        return self.questions


if __name__ == "__main__":
    alts = ["not this", "nor this", "nope", "nah", "wrong one"]
    q1 = Question("What is correct?", "this", alts)

    q1.ask_question()
