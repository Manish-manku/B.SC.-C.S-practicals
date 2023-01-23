a=input("enter any word : ")
b=input("enter any other word : ")
c=int(input("how many words you want to swapped : "))

x=a[:c]+b[c:]
y=b[:c]+a[c:]
    
print("There are your swapped words:",x,"and",y)