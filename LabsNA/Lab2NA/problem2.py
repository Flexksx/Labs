import matplotlib.pyplot as plt

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

x1, y1, x2, y2 = [], [], [], []
days = 1

with open("C:\\Users\\Cristi\\Documents\\GitHub\\Labs\\LabsNA\\Lab2NA\\Assets\\dataset_2.txt") as f:
    lines = f.readlines()
for line in lines:
    if line.startswith("Date"):
        continue
    date, visitors = line.strip().split(",")
    if visitors == 'Nan':
        visitors = piecewise_linear_interp(x1, y1, days - 1)
        x2.append(days)
        y2.append(int(visitors))
    x1.append(days)
    y1.append(int(visitors))
    days += 1


plt.plot(x1, y1, '-', label='Original data')
plt.plot(x2, y2, 'o', label='Interpolated data')
plt.legend()
plt.show()
