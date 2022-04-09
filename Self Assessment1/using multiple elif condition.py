num1=int(input("enter your number1"))
num2=int(input("enter your number2"))
num3=int(input("enter your number3"))
# if num1==num2 and num1==num3:
#     print("its equal")
if num1==num2 and num2==num1 and num3==num1:
    print("equal1")
elif num1>num2 and num1>num3:
    print("num1 is greater")
elif num1<num2 and num1<num3:
    print("num2 and 3 are greater than num1")
elif num2<num1 and num2<num3:
    print("num1 and 3are greater than num2")
elif num2>num1 and num2>num3:
    print("num3 is greater")
elif num3>num1 and num3>num2:
    print("num 3 is greater")
elif num3<num1 and num3<num2:
    print("num1 and 2 are greater than num3")
else :
    print("entered input wrong")