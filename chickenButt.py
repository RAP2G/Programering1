
# Soma Szabo
# INF20
# 14-09-2021
# Lön på farigt arbetsplats
import time

print("Why do you wanna work here?")
print("This place is very dangerous.")
print("Oh! So you think the pay is good?")
print("Ha Haaa HAAAAAHAAAHAAAHAHAAAHAAAAHAAAHAAAA")
time.sleep(2)
print("""
Alright. How long do you plan to work here? If you tell me I will tell you how much money you will get.
Or how much money do you want? Then I will tell you how many days you have to work here.
""")
time.sleep(2)
answer = input("Which one is it then? Wanna now the MONEY or the DAYS?")
while answer != "END":
    if answer == "MONEY" or answer == "money" or answer == "Money":
        days = int(input("How long do you plan to work here? "))
        money = 1
        for i in range(0, days):
            money *= 2
        if money < 100:
            print(f"You will get {money}öre if you work {days}days")
            print("Are you in?")
        else:
            money /= 100
            print(f"You will get {money}kr if you work {days}days")
            print("Are you in?")
            break
    elif answer == "DAYS" or answer == "days" or answer == "Days":
        money = int(input("So how much money do you want? In kr. "))
        pay = money
        money *= 100
        days = 0
        while money > 1:
            money /= 2
            days += 1
        print(f"You need to work {days}days  to get {pay}kr")
        print("Now get to work!")
        break
    input("DID YOU NOT HEAR ME? You want to know the MONEY or the DAYS? Or do you want to END you work here?")
else:
    print("Then get out of here!")
