# Soma Szabo
# INF20
# 14-09-2021
# Gissa Tal

print("You have three tries to guess the number")
print("Can you do it?")
number = 69420

for n in range(3):
    guess = int(input("Your guess: "))
    if guess < number:
        print("Your guess is lower than the number")
    elif guess > number:
        print("Your guess is larger than the number")
    elif guess == number:
        print("You guessed right. You won 1 bobux. Good Job!")
        break
else:
    print("You lose! HA HA HA")
