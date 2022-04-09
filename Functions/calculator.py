# a=float(input("Enter any digits between 0 to 9 :"))
# operator=input("Choose your operator : For addition choose '+' , For subtraction choose '-' , For multiplication choose '*' , For divsion choose '/' , ")
# b=float(input("enter your second number"))
# if operator =='+':
#     addition=a+b
#     print(addition)
# elif operator =='str':
#     print("err")
# elif operator =='-':
#     subtraction=a-b
#     print(subtraction)
# elif operator =='*':
#     multiplication=a*b
#     print( multiplication)
# elif operator =='/':
#     division=a/b
#     print(division)
# else:
#     print("err")
#


# # num1=int(input("enter num1"))
# # num2=int(input("enter num2"))
# # def add(num1,num2):
# #     return num1+num2
# # print(add(num1,num2))
# #
# # print(add(num1,num2))
#
#
# def sum(initial,final):
#     sum=0
#     while initial+final:
#         if initial+sum==0:
#             sum=sum+initial
#         initial=initial+1
#     return sum
# print(sum(1,2))

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("operations\n1.add\n2.sub\n3.mul\n4.div\n5.stop")
while True:
    operation=int(input("enter operation"))
    # num1=int(input("enter ur num1"))
    # num2 = int(input("enter ur num2"))
    if operation==5:
        break
    else:
        num1=int(input("enter ur num1"))
        num2=int(input("enter ur num2"))
    if operation==1:
        print(num1+num2)
    elif operation==2:
        print(num1-num2)
    elif operation==3:
        print(num1*num2)
    elif operation==4:
        print(num1/num2)
    else:
        print("invalid opertaion")

