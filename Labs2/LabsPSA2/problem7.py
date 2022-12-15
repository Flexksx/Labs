import random
import matplotlib.pyplot as plt

tries = 1000
distribution = {}

for i in range(35, 65):
    distribution.update({i: 0})

for i in range(tries):
    heads = 0
    for j in range(100):
        if random.randint(0, 1) == 1:
            heads += 1
    if heads in distribution:
        distribution[heads] += 1

x = list(distribution.keys())
y = list(distribution.values())

plt.bar(x, y)
plt.show()
