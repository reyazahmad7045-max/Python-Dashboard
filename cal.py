def calculete(a,b):
    total=a+b
    diff=a-b
    prod=a*b
    div=a/b
    mod=a%b
    return total,diff,prod,div,mod
a=int(input("Enter the a value"))
b=int(input("Enter the b value"))
s,d,p,q,m=calculete(a,b)
print("Sum=",s,"diff=",d,"mul=",p,"div=",q,"mod=",m)
print("diff=",d)
print("mul=",p)
print("div=",q)
print("mod=",m)
