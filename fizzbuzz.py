
for n in range(101):
    if n % 2 == 0 and n % 3 == 0 and n != 0:
        print("FizzBuzz")
    elif n % 3 == 0 and n != 0:
        print("Buzz")
    elif n % 2 == 0 and n != 0:
        print("Fizz")
    else:
        print(n)
