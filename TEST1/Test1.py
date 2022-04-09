
# to print sum of -5 to 5

# sum=0
# for i in range(-5,5+1):
#     if i>0:
#         sum=sum+i
# print(sum)


# func with arg and return typ


# num1=int(input("enter your number"))
# if num1<0:
#     print("it is a negative number")
# elif num1==0:
#     print("it is 0,not negative or positive")
# else:
#     print("it is positive number")
#


# EXAMPLE FOR MULTIPLE ELIF

# def grade(student_mark):
#     if student_mark>100:
#        return("mark exceeds/invalid input")
#     elif student_mark>=90:
#         return("A+")
#     elif student_mark>=80:
#         return("A")
#     elif student_mark>=70:
#         return("B+")
#     elif student_mark>=60:
#         return("B")
#     else:
#         return("fail")
# print(grade(82))

# sum of prime numbers between 1 to 10

# initial=1
# final=10
# sum=0
# for num in range(initial,final+1):
#     if num>0:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             sum=sum+num
# print(sum)


# create a calc with func expo,modulus,floor div

# def expo(x,y):
#     return x**y
# def mod(x,y):
#     return x%y
# def flod(x,y):
#     return x//y
# print("operations\n1.expo\n2.mod\n3.flod\n5.stop")
# while True:
#     operation=int(input("enter operation"))
#     # num1=int(input("enter ur num1"))
#     # num2 = int(input("enter ur num2"))
#     if operation==5:
#         break
#     else:
#         num1=float(input("enter ur num1"))
#         num2=float(input("enter ur num2"))
#     if operation==1:
#         print(num1**num2)
#     elif operation==2:
#         print(num1%num2)
#     elif operation==3:
#         print(num1//num2)
#     # elif operation==4:
#     #     print(num1/num2)
#     else:
#         print("invalid opertaion")


#to create a func with arg to find the fact of num given by user

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
# num=int(input("enter number"))
# factorial(num)



