t1=(1,2,5,7,9,2,4,6,8,10)
t2=(11,13,15)
m=5
a=t1[m:]
b=t1[:m]
print("the first half",b)
print("the second half",a)

for i in t1:
  if i%2==0:
    print ("the even numbers in the given tuple:",i)
    
t3=t1+t2
print(t3)
    
c=min(t3)
d=max(t3)
print("the min. value is" ,c ,"and the max. one is ",d)

    
    