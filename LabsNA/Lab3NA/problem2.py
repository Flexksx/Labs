import numpy as np


# Load matrix data from file
with open('LabsNA\\Lab3NA\\matrix.txt', 'r') as file:
    matrix = [line.strip().split() for line in file]

# Extract names and numbers from the matrix data
names = [name.strip(" '[],") for name in matrix[0][1:] if len(name) > 3]
numbers = np.array([
    [float(x.replace(',', '').replace('[','').replace(']','')) for x in row[1:]]
    for row in matrix[1:]
])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(numbers)

# Find the index of the dominant eigenvalue
dominant_index = np.argmax(np.abs(eigenvalues))

# Retrieve the dominant eigenvalue and its corresponding eigenvector
dominant_eigenvalue = eigenvalues[dominant_index]
dominant_eigenvector = eigenvectors[:, dominant_index]

# Print the dominant eigenvalue and its corresponding eigenvector
print(f"The most dominant person is {names[dominant_index]}, with the Eigenvalue = {dominant_eigenvalue}")
print(" and corresponding Eigenvector:", dominant_eigenvector)
print()

# Print all eigenvalues and eigenvectors
for i, (eigval, eigvec) in enumerate(zip(eigenvalues, eigenvectors.T), start=1):
    print("-------------------------------------------------------------------")
    print(f"Eigenvalue λ{i}:")
    print(eigval)
    print(f"Eigenvector v{i}:")
    print(eigvec)
    print()

# Sort eigenvalues and eigenvectors in descending order based on eigenvalues
sort_indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sort_indices]
eigenvectors = eigenvectors[:, sort_indices]

# Print the sorted eigenvalues
print("-------------------------------------------------------------------")
print("Eigenvalues sorted:")
for eigenvalue in eigenvalues:
    print(eigenvalue)
print()

# Print the sorted eigenvectors
print("Eigenvectors sorted:")
for eigenvector in eigenvectors.T:
    print(eigenvector)
