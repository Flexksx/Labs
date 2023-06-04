import numpy as np

def g(x, c):
    return 2*x - c*x**2

def fixed_point_iteration(c, initial_guess, num_iterations):
    p = initial_guess
    for _ in range(num_iterations):
        p = g(p, c)
    return p

def do(c, initial_guess):
    num_iterations = 100
    limit = 1 / c
    result = fixed_point_iteration(c, initial_guess, num_iterations)
    print("Limit for c=",c,":", limit)
    print("Result c=",c,":", result)

'''if we assume that it converges to 1/c, and we test for any c that is a positive integer, we can make the initial guess as 0.1,
because 0 will be a root of the function'''

for i in range(1,10):
    do(i,0.1)
