intag = []
with open("input2.txt", "r", encoding="utf-8") as values:
    for line in values.readlines():
        intag.append(line)

ver = 0
hor = 0


def part_1():
    global hor
    global ver
    for i in range(0, len(intag)):
        command = intag[i].strip()
        command.lower()

        if "forward" in command:
            hor += int(command[len(command)-1])
        elif "up" in command:
            ver -= int(command[len(command)-1])
        elif "down" in command:
            ver += int(command[len(command)-1])
    else:
        print(hor)
        print(ver)
        print(ver*hor)


def part_2():
    global ver
    global hor
    aim = 0
    for i in range(0, len(intag)):
        command = intag[i].strip()
        command.lower()
        if "forward" in command:
            hor += int(command[len(command)-1])
            ver += aim*int(command[len(command)-1])
        elif "up" in command:
            aim -= int(command[len(command)-1])
        elif "down" in command:
            aim += int(command[len(command)-1])
    else:
        print(hor)
        print(ver)
        print(ver*hor)


part_2()
