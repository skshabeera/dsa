a = list(map(int,input("\nEnter the numbers : ").split()))
j=1
number=30
for i in range(1,len (a)):
    for j in range(i,len(a)):
        if a[i-1]+a[j]==number:
            print(i-1,j)
        
