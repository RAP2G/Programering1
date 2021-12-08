import math

g = [13.3, 8.51, 7.19, 7.41, 10.06, 9.39]
g_medel = 9.31
n = len(g)
summa = 0

for i in range(0, n):
    summa += (g_medel-g[i])**2

print(f"\nSumman är {summa}")

sigma = math.sqrt(summa/n)
print(f"\nSigma är {sigma}")
