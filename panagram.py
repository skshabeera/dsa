n=input("enter the string")
a="abcdefghijklmnopqrstuvwxyz"
j=True

for i in a:
    if i not in n.lower():
        j=False
if j==True:
    print("panagram")
else:
    print("not panagram")
        
        