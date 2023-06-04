import numpy as np


def newton_Int(x1, y1, z):
    # Initialize k to 1 and Q to a list of zeros to hold the coefficients
    n = len(x1)
    a = y1.copy()
    # Calculate the divided differences using nested loops
    for j in range(1, n):
        for i in range(n-1, j - 1, -1):
            a[i] = (a[i] - a[i - 1]) / (x1[i] - x1[i - j])
    # Calculate the coefficients of the polynomial using the divided differences
    p = a[-1]
    for i in range(n-2, -1, -1):
        p = a[i] + (z - x1[i]) * p
    # Return the value of the polynomial at the given point x
    return p


def lagrange_interp(x, y, x_interp):
    n = len(x)
    y_interp = 0.0
    for j in range(n):
        L = 1.0
        for k in range(n):
            if k != j:
                L *= (x_interp - x[k]) / (x[j] - x[k])
        y_interp += L * y[j]
    return y_interp


def piecewise_linear_interp(x, y, x_interp):
    n = len(x)
    if x_interp <= x[0]:
        return y[0]
    if x_interp >= x[-1]:
        return y[-1]
    for i in range(1, n):
        if x_interp <= x[i]:
            t = (x_interp - x[i - 1]) / (x[i] - x[i - 1])
            y_interp = (1 - t) * y[i - 1] + t * y[i]
            return y_interp


def cubic_spline_interp(x, y, x_interp):
    n = len(x)
    if x_interp <= x[0]:
        return y[0]
    if x_interp >= x[-1]:
        return y[-1]
    h = np.diff(x)
    alpha = np.zeros(n)
    l = np.ones(n)
    c = np.zeros(n)
    b = np.zeros(n)
    d = np.zeros(n)
    for i in range(1, n - 1):
        alpha[i] = h[i] / (h[i - 1] + h[i])
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * alpha[i - 1]
        c[i] = h[i] / l[i]
        b[i] = h[i - 1] / l[i - 1]
        d[i] = (3 / (h[i - 1] + h[i])) * (alpha[i - 1] * (y[i + 1] - y[i]) - (alpha[i] * (y[i] - y[i - 1])))
    c[-1] = 0
    for j in range(n - 2, -1, -1):
        c[j] = c[j] - b[j] * c[j + 1]
        d[j] = d[j] - b[j] * d[j + 1]
    index = np.searchsorted(x, x_interp)
    interval = index - 1
    t = (x_interp - x[interval]) / h[interval]
    y_interp = ((d[interval] * t + c[interval]) * t + b[interval]) * t + y[interval]
    return y_interp



def romberg_integration(x, y):
    n = len(x)
    h = np.diff(x)
    sum_terms = (y[:-1] + y[1:]) * h
    integral = np.sum(sum_terms) / 2
    return integral

with open("LabsNA\\Lab2NA\\Assets\\dataset_3.txt") as f:
    lines = f.readlines()

x1 = []
y1 = []
days = 1
Nan = 0
for line in lines:
    items, time = line.strip().split(",")
    if time == ' Nan':
        Nan += 1
        print(f"Nan nr. {Nan}:")
        time = newton_Int(x1[-10:], y1[-10:], days - 1)
        rounded_number = format(time, ".1f")
        print(f"For {days-1} items this:{rounded_number} by Newton interp.")
        time = lagrange_interp(x1, y1, days - 1)
        print(f"For {days-1} items this:{time} by Lagrange interp.")
        time = piecewise_linear_interp(x1, y1, days - 1)
        print(f"For {days-1} items this:{time} by Piecewise interp.")
        time = cubic_spline_interp(x1, y1, days - 1)
        print(f"For {days-1} items this:{time} by Cubic interp.")
        x_interpolated = np.linspace(x1[0], x1[-1], num=2 * len(x1) - 1)
        y_interpolated = np.interp(x_interpolated, x1, y1)
        integral = romberg_integration(x_interpolated, y_interpolated)
        print(f"Area till {days-1} = {integral}")
        print("--------------------------------------------------------------")
    x1.append(int(items))
    y1.append(int(time))
    days += 1


