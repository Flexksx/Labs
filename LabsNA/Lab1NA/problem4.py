import numpy as np

def read_equations(num_eq, equations):
    def F(x):
        f = np.zeros(num_eq)
        for i in range(num_eq):
            f[i] = eval(equations[i])
        return f

    def J(x):
        Jf = np.zeros((num_eq, num_eq))
        eps = 1e-6
        for i in range(num_eq):
            for j in range(num_eq):
                dx = np.zeros(num_eq)
                dx[j] = eps
                Jf[i, j] = (F(x + dx)[i] - F(x - dx)[i]) / (2 * eps)
        return Jf

    return F, J


def newton_raphson_system(F, J, x0, tol=1e-6, max_iter=100):
    x = np.array(x0)
    for i in range(max_iter):
        f = F(x)
        Jf = J(x)
        dx = np.linalg.solve(Jf, -f)
        x = x + dx
        if np.linalg.norm(dx) < tol:
            return x
    raise ValueError("The Newton-Raphson method did not converge.")


num_eq = int(input("Enter the number of equations: "))
equations = []
x0 = []
for i in range(num_eq):
    equations.append(input(f"Enter equation {i+1}: "))
    x0.append(float(input(f"Enter initial guess for x{i+1}: ")))
F, J = read_equations(num_eq, equations)
tol = float(input("Enter the tolerance: "))  #1e-6

x = newton_raphson_system(F, J, x0, tol=tol)
print("Roots found:", x)



