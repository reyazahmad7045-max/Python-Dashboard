a=int(input("enter your Number: "))
b=int(input("enter your Number: "))
c=int(input("enter your Number: "))
if a>b:
    if a>c:
        print("A is greatest")
    else:
        print("C is greatest")
elif b>c:
    print("B is greatest")
else:
    print("C is greatest")