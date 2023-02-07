num = int(input("enter your number:-")) 
 a= False 
 if num > 1: 
      for i in range(2, num): 
         if (num % i) == 0: 
             a= True        
             break 
 if a: 
     print(num, "is not a prime number") 
 else: 
     print(num, "is a prime number") 
 list1=[]     
  
 print("The Prime Numbers less then your are: ") 
 for j in range(0, num + 1): 
     if j > 1: 
         for i in range(2, j): 
             if (j % i) == 0: 
                 break 
         else: 
             list1.append(j) 
 print(list1)