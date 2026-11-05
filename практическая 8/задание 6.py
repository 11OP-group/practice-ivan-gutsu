import random
secret = random.randint(1, 10)
guess = False
for i in range(1, 4):
    if guess == False:
        n = int(input(f"Попытка {i}:"))
    if n == secret:
        print("УГАДАЛИ")
        guess = True
    else:
        print("НЕВЕРНО")
        if n > secret:
            print("меньше")
        else:
            print("больше")
if guess == False:
    print("Верное число:", secret)