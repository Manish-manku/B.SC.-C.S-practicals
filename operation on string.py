a=input("Enter any word: ")
b=input("which word do you want to count: ")
c=0
d=input("which alphabet you want replace: ")
e=input("with whom: ")

g=input("which word do you want to remove only first time: ")
h=input("which word do you want to remove from the string: ")
for i in a:
    if i==b:
        c=c+1 
print ("the counted word ",b,":",c)
print ("the replaced word:",a.replace(d,e))
print ("the removed word only first time:",a.replace(g,"",1))
print("the removed word:",a.replace(h,""))