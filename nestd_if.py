def biggest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
    big = None
for i in range(3):
    a= int(input("Enter value"))
    b= int(input("Enter value"))
    c= int(input("Enter value"))
    big=biggest(a,b,c)
    print("big number=",big)
    