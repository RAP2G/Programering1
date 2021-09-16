# Soma Szabo
# INF20
# 08-09-2021
# For Loops

def ett_tvo_tre():
    x = int(input("Number 1: "))
    y = int(input("Number 2: "))
    if x < y:
        for n in range(x, y+1):
            print(n)
    elif y < x:
        for n in range(x, y-1, -1):
            print(n)


def fyra():
    tal = int(input("Give number: "))

    for n in range(0, 11):
        print(tal**n)


def fem():
    max_number = int(input("Max number: "))
    summa = 0
    for n in range(1, max_number+1):
        summa += n*n
    print(summa)


def sex():
    max_number = int(input("Max number: "))
    harmony = 0
    for n in range(1, max_number+1):
        harmony += 1/n
    print(harmony)


ett_tvo_tre()
ett_tvo_tre()
