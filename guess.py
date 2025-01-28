import random

random_num = random.randint(1, 100)

while True:
    userguess = float(input())

    if userguess > random_num:
        print("Загаданное число меньше!")

    elif userguess < random_num:
        print("Загаданное число больше!")

    else:
        print("Ты угадал!")
        break