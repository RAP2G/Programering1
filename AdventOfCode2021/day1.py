intag = []
# with open("input.txt", "r", encoding="utf-8") as values:
#     for line in values.readlines():
#         intag.append(int(line))
with open("puzzle_01.txt", "r", encoding="utf-8") as values:
    for line in values.readlines():
        intag.append(int(line))
amount = 0


def part_1():
    for i in range(1, len(intag)):
        global amount
        a = intag[i]
        b = intag[i-1]
        if a > b:
            amount += 1
    else:
        print(amount)


def part_2():
    summs = []
    for i in range(2, len(intag)):
        a = intag[i]
        b = intag[i-1]
        c = intag[i-2]
        summs.append(a+b+c)
    for i in range(1, len(summs)):
        global amount
        a = summs[i]
        b = summs[i-1]
        if a > b:
            amount += 1
    else:
        print(amount)


part_2()
