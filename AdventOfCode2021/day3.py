intag = []
with open("input3.txt", "r", encoding="utf-8") as values:
    for line in values.readlines():
        intag.append((line.strip()))

# test = ["00100", "11110", "10110", "10111", "10101", "01111",
#         "00111", "11100", "10000", "11001", "00010", "01010"]


def converter(num):
    decimal = 0
    for i in range(len(num)):
        decimal += int(num[i])*2**(len(num)-i-1)
    print(decimal)
    return decimal


def part_1(test):
    gamma = []
    epsilon = []
    for n in range(0, len(test[1])):
        one = []
        zero = []
        for i in range(0, len(test)):
            element = test[i]
            num = int(element[n])
            if num == 1:
                one.append(num)
            elif num == 0:
                zero.append(num)
        if len(zero) > len(one):
            gamma.append(0)
            epsilon.append(1)
        elif len(one) > len(zero):
            gamma.append(1)
            epsilon.append(0)
    else:
        print("")
        print(gamma)
        print(epsilon)
        print(converter(epsilon)*converter(gamma))


def part_2(test):
    co = test.copy()
    ox = test.copy()

    for n in range(0, len(ox[1])):
        if len(ox) == 1:
            break
        one = []
        zero = []
        for i in range(0, len(ox)):
            element = ox[i]
            num = int(element[n])
            if num == 1:
                one.append(num)
            elif num == 0:
                zero.append(num)
        if len(zero) == len(one):
            temp_list = []
            for i in ox:
                if i[n] == "1":
                    temp_list.append(i)
            ox = temp_list

        elif len(zero) > len(one):
            temp_list = []
            for i in ox:
                if i[n] == "0":
                    temp_list.append(i)
            ox = temp_list

        elif len(one) > len(zero):
            temp_list = []
            for i in ox:
                if i[n] == "1":
                    temp_list.append(i)
            ox = temp_list

    for n in range(0, len(co[1])):
        if len(co) == 1:
            break
        one = []
        zero = []
        for i in range(0, len(co)):
            element = co[i]
            num = int(element[n])
            if num == 1:
                one.append(num)
            elif num == 0:
                zero.append(num)
        if len(zero) == len(one):
            temp_list = []
            for i in co:
                if i[n] == "0":
                    temp_list.append(i)
            co = temp_list

        elif len(zero) > len(one):
            temp_list = []
            for i in co:
                if i[n] == "1":
                    temp_list.append(i)
            co = temp_list

        elif len(one) > len(zero):
            temp_list = []
            for i in co:
                if i[n] == "0":
                    temp_list.append(i)
            co = temp_list

    print("")
    print(int(co[0], 2))
    print(int(ox[0], 2))
    print(int(co[0], 2)*int(ox[0], 2))


# part_1(intag)
part_2(intag)
