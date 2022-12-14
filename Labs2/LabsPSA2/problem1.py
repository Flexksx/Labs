import random
from matplotlib import pyplot as plt


def dice():
    return random.randint(1, 6)


def prob9():
    occurance = 0
    roll1 = dice()
    roll2 = dice()
    roll3 = dice()
    if roll1 + roll2 + roll3 == 9:
        occurance += 1
    return occurance


def prob10():
    occurance = 0
    roll1 = dice()
    roll2 = dice()
    roll3 = dice()
    if roll1 + roll2 + roll3 == 10:
        occurance += 1
    return occurance


tries = 100000
tens = []
times = 0

for i in range(tries):
    result = prob10()
    if result == 1:
        tens.append(times + result)
        times += 1
    else:
        tens.append(times)

nines=[]
times=0
for i in range(tries):
    result = prob9()
    if result == 1:
        nines.append(times + result)
        times += 1
    else:
        nines.append(times)

horizontal=[]
for i in range(tries):
    horizontal.append(i)

plt.plot(horizontal,nines, label="Occurance of 9")
plt.plot(horizontal, tens, label="Occurance of 10")
plt.legend()
plt.show()