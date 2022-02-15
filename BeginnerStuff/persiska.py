# Soma Szabo
# INF20
# 15-09-2021
# Svenska som persika

word = input("Mata in ett ord eller en mening: ")

for i in word:
    if i != 'a' and i != 'e' and i != 'u' and i != 'i' and i != 'o' and i != "ö" and i != "å" and i != "ä" and i != 'A' and i != 'E' and i != 'U' and i != 'I' and i != 'O' and i != "Ö" and i != "Å" and i != "Ä":
        print(i, end="")

vowel = ["a", "e", "i", "u", "o", "ö", "ä", "å",
         "A", "E", "U", "I", "O", "Ö", "Ä", "Å"]

for i in word:
    for n in vowel:
        if i == n:
            break
    else:
        print(i, end="")
