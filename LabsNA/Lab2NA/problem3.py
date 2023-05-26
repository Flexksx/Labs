# Read the dataset from the file
# Read the dataset from the file
def read_dataset(file_path):
    dataset = []
    with open(file_path, 'r') as file:
        next(file)  # Skip the header
        for line in file:
            line = line.strip()
            if line:
                values = line.split(',')
                items = int(values[0].strip())
                time = float(values[1].strip()) if values[1].strip().lower() != 'nan' else None
                dataset.append((items, time))
    return dataset

file_path = 'Assets/dataset_3.txt'
dataset = read_dataset(file_path)


file_path = 'Assets/dataset_3.txt'
dataset = read_dataset(file_path)
# Lagrange Interpolation
def lagrange_interpolation(x, x_values, y_values):
    n = len(x_values)
    result = 0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result
# Piecewise Linear Interpolation
def piecewise_linear_interpolation(x, x_values, y_values):
    n = len(x_values)
    for i in range(n-1):
        if x_values[i] <= x <= x_values[i+1]:
            y = y_values[i] + (x - x_values[i]) * (y_values[i+1] - y_values[i]) / (x_values[i+1] - x_values[i])
            return y
    return None
# Newton's Divided Difference Interpolation
def newton_interpolation(x, x_values, y_values):
    n = len(x_values)
    coefficients = [y_values[0]]
    for i in range(1, n):
        f_diff = [y_values[j] for j in range(i, n)]
        for j in range(i):
            f_diff[j] = (f_diff[j+1] - f_diff[j]) / (x_values[j+i] - x_values[j])
        coefficients.append(f_diff[0])
    result = coefficients[0]
    for i in range(1, n):
        term = coefficients[i]
        for j in range(i):
            term *= (x - x_values[j])
        result += term
    return result
# Cubic Spline Interpolation
def cubic_spline_interpolation(x, x_values, y_values):
    n = len(x_values)
    h = [x_values[i+1] - x_values[i] for i in range(n-1)]
    alpha = [0] + [(3 * (y_values[i+1] - y_values[i]) / h[i]) - (3 * (y_values[i] - y_values[i-1]) / h[i-1]) for i in range(1, n-1)]
    l, mu, z = [1], [0], [0]
    for i in range(1, n-1):
        l.append(2 * (x_values[i+1] - x_values[i-1]) - h[i-1] * mu[i-1])
        mu.append(h[i] / l[i])
        z.append((alpha[i] - h[i-1] * z[i-1]) / l[i])
    l.append(1)
    z.append(0)
    c, b, d = [0] * n, [0] * n, [0] * n
    for j in range(n-2, -1, -1):
        c[j] = z[j] - mu[j] * c[j+1]
        b[j] = (y_values[j+1] - y_values[j]) / h[j] - h[j] * (c[j+1] + 2 * c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3 * h[j])
    for i in range(n-1):
        if x_values[i] <= x <= x_values[i+1]:
            y = y_values[i] + b[i] * (x - x_values[i]) + c[i] * (x - x_values[i]) ** 2 + d[i] * (x - x_values[i]) ** 3
            return y
    return None
x_values = [data[0] for data in dataset]
y_values = [data[1] for data in dataset]

x = 30
lagrange_result = lagrange_interpolation(x, x_values, y_values)
linear_result = piecewise_linear_interpolation(x, x_values, y_values)
newton_result = newton_interpolation(x, x_values, y_values)
spline_result = cubic_spline_interpolation(x, x_values, y_values)

print(f"Lagrange Interpolation: {lagrange_result}")
print(f"Piecewise Linear Interpolation: {linear_result}")
print(f"Newton's Divided Difference Interpolation: {newton_result}")
print(f"Cubic Spline Interpolation: {spline_result}")
