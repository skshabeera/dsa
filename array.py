# n=int(input("enter the length of list"))
# num=int(input("enter the search"))
# l=[]
# flag=-1
# for i in range(0,n):
#     number=int(input("enter the number"))
#     l.append(number)
#     if l[i]==num:
#         flag=i
#         break
# if flag>0:
#     print(flag)
# else:
#     print(-1)

def linearsearch(arr,ele):
    for i in range(0,len(arr)):
        if arr[i]==ele:
            return i
    return -1
arr=input("enter the values").split()
ele=input("enter the values of the elements to the searched")
print("the index of the element is"+str(linearsearch(arr,ele)))
    
    


    
    
