l = [[1,2,3], [-1,5,6], [7,8,9]]
result = []
for sublist in l:
    for item in sublist:
        result.append(item)
n=3
square=n**2
for i in range(1,square+1):
    if i not in result:
        print(i)
        