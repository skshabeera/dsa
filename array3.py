a = list(map(int,input("\nEnter the numbers : ").split()))
number=int(input("enter the number"))
for i in range(1,len (a)):
    for j in range(i,len(a)):
        if a[i-1]+a[j]==number:
            print(i-1,j)
            break
else:
    print("not exist")
        
        
