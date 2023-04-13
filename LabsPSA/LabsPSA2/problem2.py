import random


def do():
    x1 = random.uniform(0, 1)
    x2 = random.uniform(0, 1)
    if x1 > x2:
        temp = x1
        x1 = x2
        x2 = temp
    a = x1
    b = x2 - a
    c = 1 - x2
    if a + b > c and b + c > a and a + c > b:
        return 1
    else:
        return 0


tries = 1000000
prob = 0
for i in range(tries):
    prob += do()

print(prob / tries)