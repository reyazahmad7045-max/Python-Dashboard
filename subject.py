def result(a):
    if a>33:
        return "pass"
    else:
        return "fail"
if __name__ == "__main__":
    
    a=int(input("enter your subject marks: "))
    print(result(a))