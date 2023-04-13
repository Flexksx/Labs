import random
from numpy import sqrt


def equation():
    ans = []
    b = random.uniform(-1, 1)
    c = random.uniform(-1, 1)
    if (pow(b, 2) - 4 * c) < 0:
        ans = ["C", "N"]
        return ans
    else:
        ans.append("R")
    x1 = (-b + pow((pow(b, 2) - 4 * c), 0.5)) / 2
    x2 = (-b - pow((pow(b, 2) - 4 * c), 0.5)) / 2
    if x1 > 0 and x2 > 0:
        ans.append("P")
    else:
        ans.append("N")
    return ans


tries = 100000
real = 0
positive = 0
for i in range(tries):
    roots = equation()
    if roots[0] == "R":
        real += 1
    if roots[1] == "P":
        positive += 1

print("Probability of both reals:", real / tries)
print("Probability of both positive: ", positive / tries)
