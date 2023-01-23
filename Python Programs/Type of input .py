a=input("enter any keyword : ")
if a.isalpha()==True :
    print ("the keyword is in letter")
    if a.islower()==True:
        print("The letters is in lowercase")
    else :
        print("the letters is in uppercase")
elif a.isdigit()==True :
    print ("the keyword is in number") 
else :
    print ("the keyword is in special character or in combination")

    
