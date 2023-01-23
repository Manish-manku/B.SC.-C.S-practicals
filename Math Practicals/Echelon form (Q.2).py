from numpy import*

a=array([

[10,20,30],[40,50,60],[70,80,90]


])

print("given matrix:\n",a)

d = linalg.det(a)
print("\ndeterminant of given matrix is:- ", int(d))

co= linalg.inv(a).T * d
print("\ncofactor matrix of the given matrix is\n",co)

inv= linalg.inv(a)
print("\ninverse of given matrix:- \n",inv)

tran = co.transpose()
print("\nadjoint of given matrix:- \n",tran)