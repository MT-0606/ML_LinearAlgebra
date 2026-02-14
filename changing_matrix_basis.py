# CHANGE OF BASIS MATRIX: a matrix that translates vector representations
# from one basis to another.
import numpy as np

# Original basis
e1 = np.array([[1],[0]])
e2 = np.array([[0],[1]])

# New basis
f1 = np.array([[1],[3]])
f2 = np.array([[2],[1]])
a = np.array([[1],[1]])

A = np.array(f1,f2) # transformation matrix
print(A)
# change = np.dot(A,a) # i.e. change of basis
# print(change)