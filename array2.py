a = list(map(int,input("\nEnter the  list  elements: ").split()))
n=int(input("enter the number positoin which you want to eleminate:"))
i=0
while i<len(a):
    if i==n:
        a[i]=""
    else:
        print(a[i])
    i=i+1
    
    
