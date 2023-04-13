p = 2333
q = 2383
n = p * q
phi = (p - 1) * (q - 1)

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letdict = {}
for i in range(len(letters)):
    temp = str(i + 1)
    if len(temp) < 2:
        temp = '0' + temp
    letdict.update({letters[i]: temp})


def gcd(a, b):
    while (b):
        a, b = b, a % b
    return abs(a)


def getE(x):
    for e in range(512342, int(x / 2)):
        if gcd(e, x) == 1:
            return e
    return 0


def getD(e, n):
    for d in range(int(n)):
        if (e % n) * (d % n) % n == 1:
            return d


e = getE(phi)
d = getD(e, phi)


def optimusprime(a, dict):
    ans = ""
    for i in range(len(a)):
        ans = ans + dict[a[i]]
    if ans[0] == '0':
        ans = list(ans)
        ans.remove(ans[0])
        return int(''.join(ans))
    return int(ans)


message = int(input())

print(message)
encrypted = pow(message, e, n)
print(encrypted)
decrypted = pow(encrypted, d, n)
print(decrypted)
