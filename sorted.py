
    
l=[10,9,8,7,6,5]
i=1
j=len(l)-1
flag=False
target=int(input("enter the  target number"))
while i<j:
    sum=l[i]+l[j]
    if sum>target:
        i=i+1
    elif sum<target:
        j=j-1
    else:
        print(i,j)
        flag=True
        break
if flag is False:
    print("no sum possible")
    

            
    
        
        
