# Soma Szabo
# INF20
# 07-12-2021
# Fahrenheit is a myth
tempNov = []
tempOCt = []
with open("november.txt", "r", encoding="utf-8") as values:
    for line in values.readlines():
        tempNov.append(int(line))

with open("october.txt", "r", encoding="utf-8") as values:
    for line in values.readlines():
        tempOCt.append(int(line))


def tempStuff(temp):
    print("")
    print(
        f"The highset temperature in that month was {sorted(temp, reverse=True)[0]}")
    print(
        f"The lowest temperature in that month was {sorted(temp)[0]}")
    print(f"The average temperature in that month was {sum(temp)/len(temp)}")
    print("")


# tempStuff(tempOCt)
# tempStuff(tempNov)
