# Soma Szabo
# INF20
# 15-09-2021
# Räkna antal bokstäver

word = input("Mata in ett ord eller en mening: ")
letter = input("Skriv in ett bokstav: ")
amount = 0
sentence = False
for i in word:
    if i == letter:
        amount += 1
    if i == " ":
        sentence = True
else:
    if sentence:
        print(f"Det finns {amount} stycken {letter} i din mening.")
    elif sentence==False:
        print(f"Det finns {amount} stycken {letter} i ditt ord.")