# THE SEVEN TYPES OF MATRICES: [A]mxn
# - Rectangular: m!=n
# - Square: m==n
# - Symmetric: [A]mxn = [A]nxm (its transpose)
# - Zero: A = 0
# - Identity: a_ii = 1 (also a square matrix)
# - Diagonal: a_ii != 0 (all identity matrices are diagonal)
# - Triangular: a_ij != 0 if i>j (lower) or i<j (upper)

import numpy as np

class MatrixTypes: # can be rectangular or square
    def isZero(self,matrix):
        return (matrix==0).all() # checks whether all elements in matrix are zero

class Rectangle(MatrixTypes):
    def isRectangular(self,r,c): # r->rows, c->columns
        return r!=c

class Square(MatrixTypes): # most matrix types happen to be square
    def isSquare(self,r,c): # r->rows, c->columns
        return r==c

    def isSymmetric(self,square_matrix):
        return np.array_equal(square_matrix,square_matrix.T)

    def isDiagonal(self,square_matrix):
        diagonal_elements = np.diag(square_matrix) # extract diagonal elements
        diagonal_matrix = np.diag(diagonal_elements)    # reconstruct a diagonal matrix
                                                        # from those elements
        return np.array_equal(square_matrix, diagonal_matrix)

    def isIdentity(self,square_matrix): # a unique diagonal metrix in which all diagonal elements
                                        # are 1s and the rest are 0s
        identity_matrix = np.identity(square_matrix.shape[0],dtype=square_matrix.dtype)
        return np.array_equal(square_matrix, identity_matrix)

    def isTriangular(self,square_matrix):
        upper,lower = 0,1
        if np.array_equal(square_matrix, np.triu(square_matrix)):
            return upper
        elif np.array_equal(square_matrix, np.tril(square_matrix)):
            return lower

#####################################################################
#####################################################################
#####################################################################

# A = np.array([[3,0],[-4,2],[3,-5]])
# A = np.array([[1,0,0],[0,1,0],[0,0,1]])
A = np.array([[3,0],[-4,2],[3,5],[2,7]])
M = MatrixTypes()
if M.isZero(A) == True:
    print("This is a zero matrix.")

rows,columns = np.shape(A)
R = Rectangle()
S = Square()
if R.isRectangular(rows,columns) == True:
    print("This is a rectangular matrix.")
elif S.isSquare(rows,columns) == True:
    print("This is a square matrix.")
    
if S.isIdentity(A):
    print("It's also an identity matrix.")
if S.isSymmetric(A):
    print("It's also symmetric.")
if S.isDiagonal(A):
    print("It's also a diagonal matrix.")

elif S.isTriangular(A)==0:
    print("It's also an upper triangular matrix.")
elif S.isTriangular(A)==1:
    print("It's also a lower triangular matrix.")