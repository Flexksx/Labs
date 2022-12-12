q = 4283
p = 4349
n = q * p
fi = (q - 1) * (p - 1)


def gete(fi):
    for e in range(2, fi*2):
        if e % fi == 1:
            return e


print(n)
print(fi)
print(gete(fi))
