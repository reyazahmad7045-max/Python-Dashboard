def biggest(a,b):
    if a>b:
        return a
    else:
        return b

big = None
for i in range(1):
    a= int(input("Enter value"))
    b= int(input("Enter value"))
    big=biggest(a,b)
print("big number=",big)