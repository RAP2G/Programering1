# Soma Szabo
# INF20
# 07-09-2021
# NTI Bank

print("""
Hello and Welcome to NTI Bank. What would you like to do?

    1. See your balance
    2. Add money to your balance
    3. Take out money from your balance
    4. Get tips about savings

    0. Stop the program
""")
blance = 1_000_000
choice = int(input("Your choice: "))
print("")

while(choice != 0):

    if(choice == 1):
        print(f"Your blance is {blance}kr")
        print("")
    elif(choice == 2):
        money = int(
            input("How much money would you like to add to you balance? "))
        print(f"Now your balance is {blance+money}kr")
        print("")
        blance += money
    elif(choice == 3):
        money = int(
            input("How much money would you like to withdraw from you balance? "))
        print(f"Now your balance is {blance-money}kr")
        print("")
        blance -= money
    elif(choice == 4):
        print("You should spend less money than what you earn. Then you should save the money you did not spend in the form of stocks or bonds.")
        print("")
    elif choice == 5:
        print("""
        Hello and Welcome to NTI Bank. What would you like to do?

        1. See your balance
        2. Add money to your balance
        3. Take out money from your balance
        4. Get tips about savings

        0. Stop the program
        """)
        print("")
    else:
        print("Please type int numbers which were shown in the start prompt!")
        print("")
    print("If you want to see the menu with the options. Please type in 5 below!")
    choice = int(input("You're choice: "))
print("")
print("Thank you for using our services!")
