lantern_fish = {
    "zero": 0,
    "one": 0,
    "two": 0,
    "three": 0,
    "four": 0,
    "five": 0,
    "six": 0,
    "seven": 0,
    "eight": 0
}
with open("input6.txt", "r", encoding="utf-8") as values:
    for line in values.read():
        if line == "0":
            lantern_fish["zero"] += 1
        elif line == "1":
            lantern_fish["one"] += 1
        elif line == "2":
            lantern_fish["two"] += 1
        elif line == "3":
            lantern_fish["three"] += 1
        elif line == "4":
            lantern_fish["four"] += 1
        elif line == "5":
            lantern_fish["five"] += 1
        elif line == "6":
            lantern_fish["six"] += 1
        elif line == "7":
            lantern_fish["seven"] += 1
        elif line == "8":
            lantern_fish["eight"] += 1


def part_1():
    for i in range(1, 257):
        new_fish = lantern_fish["zero"]
        lantern_fish["zero"] = lantern_fish["one"]
        lantern_fish["one"] = lantern_fish["two"]
        lantern_fish["two"] = lantern_fish["three"]
        lantern_fish["three"] = lantern_fish["four"]
        lantern_fish["four"] = lantern_fish["five"]
        lantern_fish["five"] = lantern_fish["six"]
        lantern_fish["six"] = lantern_fish["seven"]+new_fish
        lantern_fish["seven"] = lantern_fish["eight"]
        lantern_fish["eight"] = new_fish
    print(lantern_fish["eight"]+lantern_fish["seven"]+lantern_fish["six"]+lantern_fish["five"] +
          lantern_fish["four"]+lantern_fish["three"]+lantern_fish["two"]+lantern_fish["one"]+lantern_fish["zero"])


part_1()
