queries=[]
a=int(input("enter the number"))
b=int(input("enter the number"))
k=int(input("enter the number"))
n=int(input("enter the numbers"))
arr=[0]*(n+2)
for a,b,k in queries:
    arr[a]+=k
    arr[b+1]-=k
print(arr)
temp=0
maximum=0
for val in arr:
    temp+=val
    maximum=max(maximum,temp)
print(maximum)
    