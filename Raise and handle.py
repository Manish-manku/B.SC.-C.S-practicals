a=input("enter username: ")
if a.isalpha():
    print("Great! You succesfully entered a username" )
else:
    print("not valid ")
while True:
    try:
        a=input("please enter letters: ")
        a=str(a)
        break
    except ValueError:
        print("please try again")
print ("Great! You succesfully entered a username")