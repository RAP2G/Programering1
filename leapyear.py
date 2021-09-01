# Soma Szabo
# INF20
# 01-09-2021
# Skottår

year = int(input("Mata in ett årtal! "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Det är ett skottår")
else:
    print("Det är inte ett skottår")
