import random
import numpy


def random_point():
    alpha = random.uniform(0, numpy.pi)
    r = random.uniform(0, 10)
    x, y = r * numpy.cos(alpha), r * numpy.sin(alpha)
    return [x, y, r]


def distance(a, b):
    return numpy.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


R_half = 0
Less5 = 0
More5 = 0
Within = 0
tries = 10000
for i in range(tries):
    point = random_point()
    if point[0] > 0:
        R_half += 1
    if point[2] < 5:
        Less5 += 1
    else:
        More5 += 1
    if distance([point[0], point[1]], [0, 5]) < 5:
        Within += 1

print('Right half: ', R_half / tries)
print('< 5 inch from center: ', Less5 / tries)
print('> 5 inches from center: ', More5 / tries)
print('5 inches from (0, 5): ', Within / tries)
