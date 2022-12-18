p = 2333
q = 2383
n = p * q
phi = (p - 1) * (q - 1)


def gcd(a, b):
    while (b):
        a, b = b, a % b
    return abs(a)


def getE(x):
    for e in range(512342,int(x / 2)):
        if gcd(e, x) == 1:
            return e
    return 0


def getD(e,n):
    for d in range(int(n)):
        if (e % n)*(d%n)%n==1:
            return d

print(getD(getE(phi),phi))
print(getE(phi))