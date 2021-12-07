intag = []
with open("input3.txt", "r", encoding="utf-8") as values:
    for line in values.readlines():
        intag.append((line.strip()))

test = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]


def converter(num):
    decimal = 0
    for i in range(len(num)):
        decimal += int(num[i])*2**(len(num)-i-1)
    print(decimal)
    return decimal

def part_1(test):
    gamma =[]
    epsilon = []
    for n in range(0,len(test[1])):
        one = []
        zero = [] 
        for i in range(0,len(test)):
            element = test[i]
            num = int(element[n])
            if num == 1:
                one.append(num)
            elif num == 0:
                zero.append(num)
        if len(zero)>len(one):
            gamma.append(0)
            epsilon.append(1)
        elif len(one)>len(zero):
            gamma.append(1)
            epsilon.append(0)
    else:
        print("")
        print(gamma)
        print(epsilon)
        print(converter(epsilon)*converter(gamma))

def part_2():
    co = test.copy()
    ox = test.copy()
    
    for n in range(0,len(ox[1])):
        not_sorted = True
        one = []
        zero = [] 
        for i in range(0,len(ox)):
            element = ox[i]
            num = int(element[n])
            if num == 1:
                one.append(num)
            elif num == 0:
                zero.append(num)
        if len(zero)==len(one):
            while not_sorted:
                for x in ox:
                    if x[n] == "0":
                        ox.remove(x)
                for i in range(0,len(ox)):
                    sort_after =[]
                    element = ox[i]
                    num = int(element[n])
                    if num == 0:
                        sort_after.append(num)
                if len(sort_after) == 0:
                    not_sorted =False

        elif len(zero)>len(one):
            while not_sorted:
                for x in ox:
                    if x[n] == "1":
                        ox.remove(x)
                for i in range(0,len(ox)):
                    sort_after =[]
                    element = ox[i]
                    num = int(element[n])
                    if num == 1:
                        sort_after.append(num)
                if len(sort_after) == 0:
                    not_sorted =False


        elif len(one)>len(zero):
            while not_sorted:
                for x in ox:
                    if x[n] == "0":
                        ox.remove(x)
                for i in range(0,len(ox)):
                    sort_after =[]
                    element = ox[i]
                    num = int(element[n])
                    if num == 0:
                        sort_after.append(num)
                if len(sort_after) == 0:
                    not_sorted =False
        if len(ox)==1:
            break


    for n in range(0,len(co[1])):
        not_sorted = True
        one = []
        zero = [] 
        for i in range(0,len(co)):
            element = co[i]
            num = int(element[n])
            if num == 1:
                one.append(num)
            elif num == 0:
                zero.append(num)
        if len(zero)==len(one):
            while not_sorted:
                for x in co:
                    if x[n] == "1":
                        co.remove(x)
                for i in range(0,len(co)):
                    sort_after =[]
                    element = co[i]
                    num = int(element[n])
                    if num == 1:
                        sort_after.append(num)
                if len(sort_after) == 0:
                    not_sorted =False

        elif len(zero)>len(one):
            while not_sorted:
                for x in co:
                    if x[n] == "0":
                        co.remove(x)
                for i in range(0,len(co)):
                    sort_after =[]
                    element = co[i]
                    num = int(element[n])
                    if num == 0:
                        sort_after.append(num)
                if len(sort_after) == 0:
                    not_sorted =False


        elif len(one)>len(zero):
            while not_sorted:
                num
                for x in co:
                    if x[n] == "1":
                        co.remove(x)
                for i in range(0,len(co)):
                    sort_after =[]
                    element = co[i]
                    num = int(element[n])
                    if num == 1:
                        sort_after.append(num)
                if len(sort_after) == 0:
                    not_sorted =False
        if len(co)==1:
            break
    print("")
    print(co)
    print(ox)
    print(int(co[0],2)*int(ox[0],2))
part_1(test)
part_2()

