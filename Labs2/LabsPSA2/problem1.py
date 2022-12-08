import random


def dice():
    return random.randint(1, 6)


def prob9(tries):
    prob = 0
    for i in range(tries):
        roll1 = dice()
        roll2 = dice()
        if roll1 + roll2 == 9:
            prob += 1
    return prob / tries


def prob10(tries):
    prob = 0
    for i in range(tries):
        roll1 = dice()
        roll2 = dice()
        roll3 = dice()
        if roll1 + roll2 + roll3 == 10:
            prob += 1
    return prob / tries


tries = 100000
print(prob9(tries))
print(prob10(tries))
