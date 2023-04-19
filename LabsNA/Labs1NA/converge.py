global TOL
TOl = 1e-5


def g(x, c):
    return 2 * x - c * x * x


def dg(x, c):
    return 2 - 2 * c * x


def FPINewton(c, guess):
    xold = guess
    iter = 0
    while iter < 100:
        xnew = xold - g(xold, c)/dg(xold,c)
        xold = xnew
        iter += 1
        if xold==0.0:
            return xold
    xnew = xold - g(xold, c)
    return xnew

