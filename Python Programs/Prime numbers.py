num=int(input("enter a number: ")) 
list1=[] 
if (num%2)!=0: 
   print(num," is a prime number") 
   for i in range(2, num): 
       if (i%2)!=0 or i==2: 
          list1.append(i) 
else: 
  print("it is not a prime number")
  
if len(list1) == 0:
   print("no prime number less then yours") 
else: 
   print(list1,"are all prime less then yours")