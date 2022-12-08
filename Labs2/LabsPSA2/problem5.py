import random
from numpy import sqrt

def equation():
    ans = []
    b = random.uniform(-1, 1)
    c = random.uniform(-1, 1)
    if (pow(b, 2) - 4 * c) < 0:
        ans.append("Complex")
    else:
        ans.append("Real")
    x1 = (-b + sqrt(pow(b, 2) - 4 * c)) / 2
    x2 = (-b - sqrt(pow(b, 2) - 4 * c)) / 2
    if ans[0] == "Real" and x1 > 0 and x2 > 0:
        ans.append("Positive")
    else:
        ans.append("Negative")
    return ans

tries=10000
real=0
positive=0
for i in range(tries):
    roots=equation()
    if roots[0]=="Real":
        real+=1


