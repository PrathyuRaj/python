# number=int(input("enter number"))
# sum=0
# for i in range(1,number+1) :#i=1,2,3
# #sum=sum+i #sum=6
#     sum+=i
# print(i,sum)
#
#
# student_mark = int(input("enter your mark"))
# def grade(student_mark):
#     if student_mark > 100:
#         print("mark exceeds/invalid input")
#     elif student_mark >= 90:
#         print("A+")
#     elif student_mark >= 80:
#         print("A")
#     elif student_mark >= 70:
#         print("B+")
#     elif student_mark >= 60:
#         print("B")
#     else:
#         print("fail")
#     return student_mark
# print(student_mark(20))
#
initial=1
final=10
num=1
for num in range(initial,final+1,):
    if num>0:
        for i in range(2,num,):
            if num%i==0:
                break
        else:
            print(num)