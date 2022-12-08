import random
import math


def getpoint():
    r = 1
    theta = random.uniform(0, math.pi * 2)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def isacute(a, b, c):
    if a**2+b**2>c**2:
        return True
    else:
        return False


prob=0
tries = 10000
for i in range(tries):
    p1 = getpoint()
    p2 = getpoint()
    p3 = getpoint()
    a = distance(p1[0], p1[1], p2[0], p2[1])
    b = distance(p1[0], p1[1], p3[0], p3[1])
    c = distance(p1[0], p2[1], p3[0], p3[1])
    if isacute(a,b,c):
      prob+=1

print(prob/tries)