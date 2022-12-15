import random


def game():
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    wins = 1
    if y<x:
        while y < x:
            y = random.uniform(0, 1)
            wins += 1
    else:
        return 0
    return wins - 1


money = 0
tries = 100000
for i in range(tries):
    money += game()

print(money / tries)
