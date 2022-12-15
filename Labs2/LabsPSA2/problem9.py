import random


def game():
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    wins = 0
    while y < x:
        y = random.uniform(0, 1)
        wins += 1
    return wins - 1


money = 0
tries = 100000
for i in range(tries):
    money += game()

print(money / tries)
