import numpy as np

def Jacobian(n, equations):
    def F(x):
        f = np.zeros(n)
        for i in range(n):
            f[i] = eval(equations[i])
        return f

    def J(x):
        Jf = np.zeros((n, n))
        eps = 1e-6
        for i in range(n):
            for j in range(n):
                dx = np.zeros(n)
                dx[j] = eps
                Jf[i, j] = (F(x + dx)[i] - F(x - dx)[i]) / (2 * eps)
        return Jf
    return F, J


def Newton(F, J, x0, TOL, MAX_ITER):
    x = np.array(x0)
    for i in range(MAX_ITER):
        f = F(x)
        Jf = J(x)
        dx = np.linalg.solve(Jf, -f)
        x = x + dx
        if np.linalg.norm(dx) < TOL:
            return x

def GetEquations():
    n=0
    x0=[]
    equations=[]
    input("Enter the number of equations: ",n)
    for i in range(n):
        s=""
        initial_guess=0
        equations.append(eval(input("Equation nr. ",s)))
        x0.append(float(input("Enter initial guess", initial_guess)))
    return equations, x0

equations, x0 = GetEquations()
