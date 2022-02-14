

def linearsearch(arr,ele):
    for i in range(0,len(arr)):
        if arr[i]==ele:
            return i
    return -1
arr=input("enter the values").split()
ele=input("enter the values of the elements to the searched")
print("the index of the element is"+str(linearsearch(arr,ele)))
    
    


    
    
