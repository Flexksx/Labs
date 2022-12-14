import random


def circleCenter():
    return [random.uniform(0, 1), random.uniform(0, 1)]


def distance(x1, y1, x2, y2):
    return pow(((x2 - x1) ** 2) + ((y2 - y1) ** 2), 0.5)


wins = 0


def game():
    circle = circleCenter()
    if 0.25 <= circle[0] <= 0.75 and 0.25 <= circle[1] <= 0.75:
        return 1
    else:
        return 0


tries = 10000
for i in range(tries):
    wins += game()

print(wins/tries)
