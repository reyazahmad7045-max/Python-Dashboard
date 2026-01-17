def biggest(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
        else:
            if b>c:
                return b
            else:
                return c
            a=int(input("Enter A value"))
            b=int(input("Enter B value"))
            C=int(input("Enter C value"))
            big=biggest(a,b,c)
            print("big number=",big)
        
