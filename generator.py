from random import randint, choice
from planets import Moons, Planets

planet_names = ["Khanoros", "Wartos XI", "Barumi 96",
                "Ladurdan IX", "Poolanbula 152", "Thryornia Zengsea", "Venenella"]
moon_names = ["Travaler", "Lionama", "Endor", "Hiltamon", "Etnasa", "Megazol LI9", "Oulzamar", "Petram SL4", "Hipzarion", "Duntana",
              "Cortinas NX1", "Mahina", "Capricornus UR4", "Sammador", "Hipzarion", "Lakas", "Strilles WK7", "Aret KT5", "Straxirus MP0"]

planets = []
moons = []
for i in planet_names:
    planets.append(Planets(i, randint(2e6, 9e10)))

for i in moon_names:
    moons.append(Moons(i, randint(2, 2e6)))


for i in planets:
    fail_condition = 0
    moon_number = randint(1, 3)
    while moon_number > 0:
        moon = choice(moons)
        if moon.get_orbit() == None:
            i.add_moon(moon)
            moon.add_orbit(i.get_name())
            moon_number -= 1
        else:
            fail_condition += 1
        if fail_condition == len(moons):
            break
    i.print_moons()
