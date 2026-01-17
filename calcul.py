def calculate(a,b):
    total=a*b
    difference=a-b  
    product=a*b
    quotient=a/b
    mod=a%b
    return total, difference, product, quotient, mod
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
s,d,p,q,m=calculate(a,b)
print("Total:",s)
print("Difference:",d)
print("Product:",p)
print("Quotient:",q)
print("Modulus:",m)
