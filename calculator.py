a=int(input("enter value 1: "))
b=int(input("enter value 2: "))
cal=str(input("addition(a),subtraction(s),division(d),multiplication(m): "))

for i in cal:
    if (i=="a") :
        print("add=",a+b)
    elif (i=="s"):
        print("sub=",a-b)
    elif(i=="d"):
        print("div=",a/b)
    else:
        print("mul=",a*b)

