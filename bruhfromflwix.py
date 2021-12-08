if __name__ == "__main__":
    f = open("wins.txt", "r", encoding="utf8")
    print(f.read())
    f.close()

    with open("wins.txt", "r", encoding="utf8") as wins:
        # print(wins.read())
        # print(wins.readline())
        print(wins.readlines())
        # print(wins.read(12))

        for line in wins.readlines():
            print(line)

    # Olika sätt att hentera filen
    with open("inf20.txt", "w", encoding="utf8") as inf20:
        # r - read
        # x - create, får error om filen finns
        # w - write, skapar filen om den ej finns
        # a - append, skapar filen om den ej finns
        print("Mata in alla elever i inf20, skriv # om du vill avsluta")
        while True:
            elev = input("Elev: ")
            if "#" in elev:
                break
            else:
                inf20.write(f"{elev}\n")

    with open("inf20.txt", "r", encoding="utf8") as inf20:
        print("Elever i INF20")
        for elev in inf20.readlines():
            print(elev, end="")
