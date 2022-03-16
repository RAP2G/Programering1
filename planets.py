# Soma Szabo
# INF20
# 08-03-2022
# Planeter och Månar

# Classes


class Planets:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.moons = []

    def get_name(self):

        return self.name

    def get_size(self):
        return self.size

    def get_moons(self):
        return self.moons

    def add_moon(self, moon):
        self.moons.append(moon)

    def certain_size(self, size):
        print(
            f"The following moons around {self.get_name()} that are larger than {size} sqkm:")
        for i in self.moons:
            if size < i.get_size():
                print(i.get_name())

    def print_moons(self):
        if len(self.get_moons()) > 1:
            print(f"{self.get_name()} is orbited by the moons ", end="")
            for x in self.get_moons():
                if x == self.get_moons()[len(self.get_moons())-1]:
                    print(f"and {x.get_name()}")
                elif x == self.get_moons()[len(self.get_moons())-2]:
                    print(f"{x.get_name()} ", end="")
                else:
                    print(f"{x.get_name()}, ", end="")
        elif len(self.get_moons()) == 1:
            print(
                f"{self.get_name()} is orbited by the moon {self.get_moons()[0].get_name()}")
        else:
            print(f"{self.get_name()} has no moons.")


class Moons:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.orbit = None

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_orbit(self):
        return self.orbit

    def add_orbit(self, orbit):
        self.orbit = orbit

    def print_orbit(self):
        print(f"{self.get_name()} orbits {self.get_orbit().get_name()}")


def main():
    planets = []
    moons = []
    tellus = Planets("Tellus", 5.1006*10**8)
    mars = Planets("Mars", 1.4437*10**8)
    jupiter = Planets("Jupiter", 6.142*10**10)
    luna = Moons("Luna", 3.794*10**7)
    phobos = Moons("Phobos", 1.548)
    deimos = Moons("Deimos", 483)
    io = Moons("Io", 4.191*10**7)
    europa = Moons("Europa", 3.09*10**7)

    tellus.add_moon(luna)
    luna.add_orbit(tellus)
    mars.add_moon(phobos)
    mars.add_moon(deimos)
    phobos.add_orbit(mars)
    deimos.add_orbit(mars)
    jupiter.add_moon(io)
    jupiter.add_moon(europa)
    io.add_orbit(jupiter)
    europa.add_orbit(jupiter)

    planets.append(tellus)
    planets.append(mars)
    planets.append(jupiter)
    moons.append(luna)
    moons.append(phobos)
    moons.append(deimos)
    moons.append(io)
    moons.append(europa)

    tellus.print_moons()
    jupiter.print_moons()
    mars.print_moons()
    luna.print_orbit()
    jupiter.certain_size(
        int(input("How big is the moon you are looking for?")))


if __name__ == "__main__":
    main()
