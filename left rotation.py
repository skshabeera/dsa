# n=int(input("enter the number"));
# d=int(input("enter the number"));
# a=[1,2,3,4,5]
# oldindex=0
# array=[]
# while oldindex<len(a):
#     newindex=(oldindex+len(a)-d)%len(a)
#     array[newindex]=a[oldindex]
#     oldindex=+1
    
# n=list(map(int,input("\nEnter the  list  elements: ").split()))
# a=[]
# x=a[0]
# j=0
# while j<len(a)-1:
#     a[j]=a[j+1]
#     j=j+1
# a[j]=x
a=[1,2,3,4,5]
new=[]
shift = int(input("enter the number"))
for i in range(0,shift):
    temp=a[0]
    for j in range(0,len(a)-1):
        a[j]=a[j+1]
    a[len(a)-1]=temp
for i in range(0,len(a)):
    new.append((a[i]))
print(new)


# a=[1,2,3,4,5]
# i=0
# d=4
# while i<d:
#     a.append(a[0])
#     a.remove(a[0])
#     i+=1
# print(a)