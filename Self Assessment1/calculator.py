

def mod(x,y):
    return x**y
def flodiv(x,y):
    return x//y
print("operations\n1.expo\n2.floor div\n3.stop")
while True:
    operation=int(input("enter operation"))
    if operation==3:
        break
    else:
        num1=float(input("enter ur num1"))
        num2=float(input("enter ur num2"))
    if operation==1:
        print(num1**num2)
    elif operation==2:
        print(num1//num2)
    else:
        print("invalid")
