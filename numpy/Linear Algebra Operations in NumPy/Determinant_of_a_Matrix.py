# . Determinant of a Matrix
import numpy as np
# Example: Determinant of a Matrix
arr = np.array([[1, 2], [3, 4]])
determinant = np.linalg.det(arr)
print(determinant)

# Inverse of a Matrix
A = np.array([[1, 2], [3, 4]])
A_inv = np.linalg.inv(A)
print(A_inv)


#Eigenvalues & Eigenvectors (Important for PCA)

A = np.array([[3, 1], [2, 4]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
