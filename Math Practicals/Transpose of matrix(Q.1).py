import  numpy as np
from sympy import *
a= Matrix(

[[10,20,40],[70,80,100],[30,50,60]]

)
print("your Matrix is:")
print (a)


M_rref= a.rref()
print("Echelon form of matrix:\n" ,M_rref)

my_matrix = np.array([[10,20,40],[70,80,100],[30,50,60]])
print(my_matrix)
rank = np.linalg.matrix_rank(my_matrix)
print("Rank of the given Matrix is : ",rank) 





