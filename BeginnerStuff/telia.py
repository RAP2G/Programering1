# Soma Szabo
# INF20
# 01-09-2021
# Mobilabonemang

minuter = int(input("Hur länge tänker ni ringa varje månad? Ange i minuter! "))

if minuter <= 33:
    print("Du borde välja vår Kontant abonemang.")
elif 33 <= minuter <= 66:
    print("Du borde välja vår Normal abonemang.")
else:
    print("Du borde välja vår Plus abonemang.")
