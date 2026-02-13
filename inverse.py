import numpy as np

class Inverse:
    def inv(self,A):
        return np.linalg.inv(A)
    
    def check_inv(self,A,B):
        I = np.identity(A.shape[0],dtype=A.dtype) # construct an identity matrix
        return A@B == I

    
I = Inverse()
A = np.array([[1,2],[3,4]])
A_inv = I.inv(A)
print("A^-1\n",A_inv)

B = np.array([[4,3],[2,1]])
if I.check_inv(A,B) == False:
    print("B is not the inverse of A.")
else:
    print("B is the inverse of A.")