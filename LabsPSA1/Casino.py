import random
import matplotlib.pyplot as plt


def graphred(tries):
    casino = ['R', 'G', 'B']
    kapusta = 0
    for i in range(tries):
        kapusta -= 20
        spin = random.choices(casino, weights=(18, 2, 18), k=1)
        if spin == ['R']:
            kapusta += 40
        x.append(i)
        y.append(kapusta)
    plt.plot(x, y)
    plt.savefig("red.jpg")


def graph18(tries):
    kapusta = 0
    for i in range(tries):
        kapusta -= 20
        spin = random.randint(0, 37)
        if spin == 17:
            kapusta += 20 * 35
        m.append(i)
        n.append(kapusta)
    plt.plot(m, n)
    plt.savefig("18.jpg")


m = []
n = []
x = []
y = []
graphred(500)
graph18(500)
