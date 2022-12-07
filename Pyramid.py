'''

                           WAP to create a pyramid of the character ‘*’ and a reverse pyramid

'''

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")
