# Soma Szabo
# INF20
# 01-09-2021
# Moms

pris = int(input("Hur mycket kostar din vara? "))
procent = input("Är det 6%, 12%, eller 25% moms på din vara? ")
if procent == "6%":
    moms = pris*0.06
elif procent == "12%":
    moms = pris*0.12
elif procent == "25%":
    moms = pris*0.25
else:
    print("På grund av våra chefer så kan vi inte hantera moms som är inte 6%, 12%, eller 25%")
med_moms = pris+moms
print(
    f"Om momsen är {procent}% och varan är {pris}kr. Då blir momsen {moms}kr. Varan kostar {med_moms}kr med moms.")
