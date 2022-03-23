# Soma Szabo
# INF20
# 09-02-2022
# Teknikare


class NtiElev:

    def __init__(self, name, age, sex, _class):
        self.name = name
        self.age = age
        self.sex = sex
        self._class = _class
        self.pronoun = "hon" if self.sex == "tjej" else "han"
        self.pospro = "hennes" if self.sex == "tjej" else "hans"

    def __str__(self):
        return f"NTI Eleven heter {self.name}. {self.pronoun.capitalize()} är en {self.sex} och är {self.age} år gammal. {self.pronoun.capitalize()} går i klassen {self._class}"

    def return_name(self):
        return f"Eleven heter {self.name}."


class Teknikare(NtiElev):

    def __init__(self, name, age, sex, _class, favorite_game):
        super().__init__(name, age, sex, _class)
        self.favorite_game = favorite_game

    def __str__(self):
        return super().__str__() + f" {self.pospro.capitalize()} favorit spel är {self.favorite_game}"

    def gaming(self):
        return f"{self.name} spelar {self.favorite_game}."


class ITare(NtiElev):
    def __init__(self, name, age, sex, _class, mess):
        super().__init__(name, age, sex, _class)
        self.mess = mess

    def __str__(self):
        return super().__str__() + f" {self.pronoun.capitalize()} har varit stökigt {self.mess} gånger."


def main():
    soma = Teknikare("Soma", "17", "kille", "TEINF-20",
                     "The Legend Of Zelda Breath Of The Wild")
    armand = ITare("Armand", "17", "kille", "IT-20", "0")
    ellen = Teknikare("Ellen", "17", "tjej", "TEINF-20", "Stardew Valley")
    max = Teknikare("Max", "17", "kille", "TEINF-20", "Read Dead Redemption 2")
    ossian = Teknikare("Ossian", "17", "kille", "TEINF-20", "Elden Ring")
    NTI_Nacka = [soma, armand, ellen, max, ossian]
    for i in NTI_Nacka:
        print(i)
        if i == Teknikare:
            print(i.gaming())
        elif i == ITare:
            pass


if __name__ == "__main__":
    main()
