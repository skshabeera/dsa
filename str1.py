
vowels="aeiou"
consonents="bcdfghjklmnpqrstvwxyz"
others="!@#$%&*"
n=input("enter the string")
a=0
b=0
c=0
i=0
while i<len(n):
    if n[i] in vowels:
        a=a+1
    if n[i] in consonents:
        b=b+1
    if n[i]==" " or n[i] in others:
        c=c+1
    i=i+1
print(a, "vowels count")
print(b,"consonents count")
print(c,"other characters")

