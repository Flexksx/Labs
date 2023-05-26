import numpy as np

# Define the coefficients matrix A and the constants vector C
A = np.array([[2, -1],
              [3, 2],
              [1, 1],
              [4, -1],
              [1, -3]])

C = np.array([4, 7, 3, 1, -2])

# Solve the system of equations using Gaussian elimination
X = np.linalg.lstsq(A, C, rcond=None)[0]

# Print the solutions for x and y
print("Solution:")
for i, solution in enumerate(X):
    print(f"Stone {i+1}: {solution:.2f}")
