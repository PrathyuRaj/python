# 2,3,5,7
# to check prime or not prime
# num=int(input("enter your num"))
# if num>0:
#     for i in range(2,num):
#         if num%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")

#
# #
# initial=int(input("enter ur initial"))
# final=int(input("enter ur final range"))
# i=1
# for num in range(initial,final+1):
#     if num>0:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)
#




            # NON PRIME NUMBERS TO PRINT?????


initial=int(input("enter your num1"))
final=int(input('enter your num2'))
num=1
for num in range(initial,final+1,):
    if num>0:
        for i in range(2,num,):
            if num%i==0:
                break
        else:
            print(num)