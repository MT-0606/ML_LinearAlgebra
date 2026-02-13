# SOLVING LINEAR EQUATIONS USING GAUSSIAN ELIMINATION
import numpy as np

A = np.array([[1,2,1],[2,-1,1],[4,3,3],[3,1,2]])
b = np.array([[1],[2],[4],[3]])

# 1. Combine original matrix A with constant vector b.
A_b = np.concatenate((A,b), axis=1)

# 2. Perform a series of elementary row operations on the augmented matrix.
def to_rref(matrix):
    A = matrix.copy().astype(float) # Make a copy to avoid modifying the original matrix
    rows,cols = A.shape

    for j in range(cols):
        if pivot_row >= rows:
            break
        i = pivot_row   # Find a pivot row
        while i < rows and A[i, j] == 0:
            i += 1
        if i == rows:
            continue

        A[[pivot_row, i]] = A[[i, pivot_row]] # Swap rows

        # Divide row by pivot element to make the pivot 1
        A[pivot_row] /= A[pivot_row, j]

        # Eliminate other non-zero entries in the current column
        for i in range(rows):
            if i != pivot_row:
                A[i] -= A[i, j] * A[pivot_row]

        pivot_row += 1

    return A

pivot_row = 0
AB_RREF = to_rref(A_b)
print("Reduced row echelon form:\n", AB_RREF)

if (len(pivot_row) == AB_RREF.shape[0]) and (len(pivot_row) == AB_RREF.shape[1]-1):
    solution = AB_RREF[:, -1]
    print("\n(x1,x2,x3):",solution)
    print(solution)
else:
    print("\nThe system has either no solution or infinite solutions.")
