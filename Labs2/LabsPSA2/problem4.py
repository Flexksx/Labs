import random
import math


def getpoint():
    theta = random.uniform(0, math.pi * 2)
    x = math.cos(theta)
    y = math.sin(theta)
    return x, y


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def isacute(a, b, c):
    if a ** 2 + b ** 2 > c ** 2 and a ** 2 + c ** 2 > b ** 2 and c ** 2 + b ** 2 > a ** 2:
        return True
    else:
        return False


prob = 0
tries = 100000
for i in range(tries):
    p1 = getpoint()
    p2 = getpoint()
    p3 = getpoint()
    sides = [distance(p1[0], p1[1], p2[0], p2[1]), distance(p1[0], p1[1], p3[0], p3[1]), distance(p2[0], p2[1], p3[0], p3[1])]
    sides.sort()
    if isacute(sides[0], sides[1], sides[2]):
        prob += 1

print(prob / tries)
