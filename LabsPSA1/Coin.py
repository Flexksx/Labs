import random


def flip():
    wins = 0
    coin = 1
    while coin == 1:
        wins += 1
        coin = random.uniform(0, 1)
        if coin < 0.5:
            coin = 0
        else:
            coin = 1
    return pow(2, wins)


res = 0
tries = 1000000
for i in range(tries):
    res += flip()

print(res / tries)
