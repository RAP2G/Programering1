# Soma Szabo
# INF20
# 07-09-2021
# Födelsedags räknare
# Den räknar ut vilken dag din födelse dag kommer ligga på

year = int(input("Current year: "))
month = input("Birth month: ")
day = input("Birth day:")
ancor_year = 2021
ancor_month = 9
ancor_day = 7
ancor_day_num = 2


if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    ancor_day_num += 2
else:
    ancor_day_num += 1
