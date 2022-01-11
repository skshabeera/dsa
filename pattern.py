n=int(input("enter the number"))
for i in range(0,n):
    for j in range(0,i):
        print(" ",end="")
    for k in range(0,n-i):
        print("*",end=" ")
    print()
for x in range(0,n-1):
    for  y in range(0,n-2-x):
        print(" ",end="")
    for z in range(0,x+2):
        print("*",end=" ")
    print()
