# Soma Szabo
# INF20
# 15-09-2021
# Räkna ränta

money = int(input("Hur mycket startkapital har du?"))
intrest = int(
    input("Hur stort sparränta har du? Ange i procent utan procenttecken!"))
intrest /= 100
intrest += 1
for i in range(1, 51):
    if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 10 or i == 15 or i == 20 or i == 30 or i == 40 or i == 50:
        print(f"Du har {round(money*(intrest**i))}kr efter {i}år")
