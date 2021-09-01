# Soma Szabo
# INF20
# 01-09-2021
# Super bonus uppgift
import math


sida_1 = int(input("Ange sidan a:"))
sida_2 = int(input("Ange sidan b: "))
angle = int(input("Ange vinkeln alfa: "))

sida_3 = math.sqrt(sida_1**2+sida_2**2 - (sida_2-sida_1)*math.cos(angle))

if sida_3 == sida_1 and sida_2 == sida_1:
    print("Liksidigt")
elif sida_3 == sida_1 or sida_2 == sida_1 or sida_2 == sida_3:
    print("Likbent")
else:
    print("Oliksidigt")
