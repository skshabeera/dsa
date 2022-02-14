from re import I


array=list(map(int,input("\nEnter the numbers : ").split()))
for i in range(1,len(array)):
    value=array[i]
    hole=i
    while hole>0 and array[hole-1]>value:
        array[hole]=array[hole-1]
        hole =hole-1
    array[hole]=value
print(array)
