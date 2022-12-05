import random


def do():
    x1 = random.uniform(0, 1)
    a = x1
    b = 1 - a
    if a > b:
        x2 = random.uniform(0, a)
        c = a - x2
        a -= c
    else:
        x2 = random.uniform(0, b)
        c = b - x2
        b -= c
    if a + b > c and b + c > a and a + c > b:
        return 1
    else:
        return 0


tries = 1000000
prob = 0
for i in range(tries):
    prob += do()

print(prob / tries)
