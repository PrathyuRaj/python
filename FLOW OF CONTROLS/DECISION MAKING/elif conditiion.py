# num1=int(input("enter your number"))
# if num1<0:
#     print("it is a negative number")
# elif num1==0:
#     print("it is 0,not negative or positive")
# else:
#     print("it is positive number")
#


# num1=int(input("enter your number1"))
# num2=int(input("enter your number2"))
# if num1>num2:
#     print("num1 is greater than num2")
# elif num1==num2:               #more condition can be given by using elif(more than 2 condition )
#     print("it is equal")
# else :
#     print("num2 is greater than num1")
#
# num1=int(input("enter your number1"))
# num2=int(input("enter your number2"))
# num3=int(input("enter your number3"))
# if num1==num2==num3:
#     print("equal")
# elif num2>=num1 and num2>=num3:
#     print("num2 is greater")
# elif num1>=num2>=num3:  # more condition can be given by using elif(more than 2 condition )
#     print("num1 greater")
# else:
#     print("num3 is greater than num1 and num2")

# EXAMPLE FOR MULTIPLE ELIF
student_mark=int(input("enter your mark"))
if student_mark>100:
    print("mark exceeds/invalid input")
elif student_mark>=90:
    print("A+")
elif student_mark>=80:
    print("A")
elif student_mark>=70:
    print("B+")
elif student_mark>=60:
    print("B")
else:
    print("fail")
