
print ("The Equation should be ax^2 + bx + c = 0")
a = int(input("entr the value of a= "))
b = int(input("entr the value of b= "))
c = int(input("entr the value of c= "))

import cmath

d = (b**2) - (4*a*c)  
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
if d== 0:
     print ("This is a unique soltuion",'The solution is',sol1,)
elif d > 0:
     print ("This equation has two soltuion",'The solution are',sol1, "and",sol2)
else :
      print ("This equation has no real soltuion")
     



 
 

