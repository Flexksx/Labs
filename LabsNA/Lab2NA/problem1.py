import numpy as np


def Legendre(n, x):
    x = np.array(x)
    if n == 0:
        return x * 0 + 1.0
    elif n == 1:
        return x
    else:
        return ((2.0 * n - 1.0) * x * Legendre(n - 1, x) - (n - 1) * Legendre(n - 2, x)) / n


def DLegendre(n, x):
    x = np.array(x)
    if n == 0:
        return x * 0
    elif n == 1:
        return x * 0 + 1.0
    else:
        return (n / (x ** 2 - 1.0)) * (x * Legendre(n, x) - Legendre(n - 1, x))


def LegendreRoots(polyorder, tolerance=1e-20):
    global roots
    if polyorder < 2:
        err = 1  # roots of bad polyorder can not be founded
    else:
        roots = []
        for i in range(1, int(polyorder) // 2 + 1):
            x = np.cos(np.pi * (i - 0.25) / (polyorder + 0.5))
            error = 10 * tolerance
            iters = 0
            while (error > tolerance) and (iters < 1000):
                dx = -Legendre(polyorder, x) / DLegendre(polyorder, x)
                x = x + dx
                iters = iters + 1
                error = abs(dx)
            roots.append(x)
        roots = np.array(roots)
        if polyorder % 2 == 0:
            roots = np.concatenate((-1.0 * roots, roots[::-1]))
        else:
            roots = np.concatenate((-1.0 * roots, [0.0], roots[::-1]))
        err = 0  # successfully roots has been founded
    return [roots, err]


def GaussLegendreWeights(polyorder):
    W = []
    [xis, err] = LegendreRoots(polyorder)
    if err == 0:
        W = 2.0 / ((1.0 - xis ** 2) * (DLegendre(polyorder, xis) ** 2))
        err = 0
    else:
        err = 1  # we couldn't find any roots then we have no weights
    return [W, xis, err]


# a, b: the interval of what we want to have its integral
# polyorder  : order of the Legendre polynomial to be used

def GaussLegendreQuadrature(func, polyorder, a, b):
    [Ws, xs, err] = GaussLegendreWeights(polyorder)
    if err == 0:
        ans = (b - a) * 0.5 * sum(Ws * func((b - a) * 0.5 * xs + (b + a) * 0.5))
    else:
        # (in case of error)
        err = 1
        ans = None
    return [ans, err]


def func(x):
    return np.cos(x**2) + np.sin(x)


# after inputting the function we should change the order for calculating the integral if we want more Accuracy but it
# takes more time for increased order
print("enter your order:  ")
order = int(input())
[Ws, xs, err] = GaussLegendreWeights(order)
if err == 0:
    print("Number of points  : ", order)
    # this shows us the weights of related function
    print("Weights  : ", Ws)
    # this one shows us the roots of related function
    print("Roots    : ", xs)

else:
    print("Roots/Weights evaluation failed")

# Now we can calculate the integral with the order and our wanted interval and print the answer of it
[ans, err] = GaussLegendreQuadrature(func, order, -2, 2)
if err == 0:
    print("Integral: ", ans)
else:
    print("Integral evaluation failed")
