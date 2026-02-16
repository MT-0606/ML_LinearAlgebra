# EIGENDECOMPOSITION
# - Defined for square matrices (not rectangular ones)
# - Goal: to extract pairs of eigenvalues and eigenvectors
# - Each eigenvalue has an associated eigenvector
# - lambda*v = A*v => lambda (eigenvalue), v (eigenvector),
#   A (transformation matrix)

# EIGENVALUES AND EIGENVECTORS
# - A*K = lambda*K => A (nxn matrix), K (non-zero solution vector)
# - K (an eigenvector corresponding to eigenvalue lambda)

import numpy as np

A = np.array([[3,4],[-1,7]])
print(A)

l,K = np.linalg.eig(A) # l is short for lambda
print("Eigenvalues:")
print(l)
print("\nEigenvectors:")
print(K)