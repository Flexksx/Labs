import numpy as np
from math import sin,cos,exp,log2,log10,sqrt

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
    x = np.array(x0, dtype=float)
    for i in range(max_iter):
        f = F(x)
        Jf = J(x)
        dx = np.linalg.solve(Jf, -f)
        x = x + dx
        if np.linalg.norm(dx) < tol:
            return x
    raise ValueError("The Newton-Raphson method did not converge.")


# num_eq = int(input("Enter the number of equations: "))
# equations = []
# x0 = []
# for i in range(num_eq):
#     equations.append(input(f"Enter equation {i+1}: "))
#     x0.append(float(input(f"Enter initial guess for x{i+1}: ")))
# F, J = read_equations(num_eq, equations)
# tol = float(input("Enter the tolerance: "))  #1e-6

# x = newton_raphson_system(F, J, x0, tol=tol)
# print("Roots found:", x)

tests=[["2*x[0] + 3*x[1] - 4*x[2] + 5*x[3] - 6*x[4]",
    "-3*x[0] + 4*x[1] + 5*x[2] - 6*x[3] + 7*x[4]",
    "4*x[0] - 5*x[1] + 6*x[2] - 7*x[3] + 8*x[4]",
    "-5*x[0] + 6*x[1] - 7*x[2] + 8*x[3] - 9*x[4]",
    "6*x[0] - 7*x[1] + 8*x[2] - 9*x[3] + 10*x[4]"],
       ["x[0]-x[1]-x[2]",
        "x[0]+x[1]+x[2]",],
       ["sin(x)",
        "cos(x)"]]
guesses=[[9,1.5,-0.8,3,10],
         [2.1,6.01],
         [3.14/3.5, 3.14/3.4]
]

for i in range(0,len(tests)-1):
    equations = tests[i]
    guess=guesses[i]
    n=len(equations)
    F,J=read_equations(n,equations)
    tol=1e-6
    x=newton_raphson_system(F,J,guess,tol)
    print("Roots: ", x)
