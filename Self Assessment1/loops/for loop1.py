# for(for=keyword)variable( variablename) in(in=membership function) range()(range=int):
    # looping code

# for num in range(7,2,-1):
#     print("hello",num)





# # to check odd/even
# num=int(input("enter your num"))
# if num<0:
#     print("enter a valid input")
# elif num%2==0:
#     print(num,"is even")
# else:
#     print(num,"is odd")


# to check even numbers from  1-10 numbers and to print
# for i in range(0,10+1,2):
#     if i%2==0:
#         print(i)
#
# for i in range(1,10):
#     if i%2==0 and i>=6:   #to print even num greater than 5
#         print(i)

        # OR


# for i in range(1,10):
#     if i%2==0:
#         if i>5:
#             print(i)    #nesting if inside if.

# to find odd numbers from range user enters
# initial_range=int(input("enter your initial range"))
# final_range=int(input("enter your final range"))
# for i in range(initial_range,final_range+1):
#     if i%2!=0:
#         print(i)




# 1*2=2

# .......
# 10*2=20
# to print multiplication table from user entered range

# num=int(input("enter your table number"))
# for i in range(1,10+1):
#     print(i,"*",num,"=",i*num)


# to find sum from user entered number
#
# num=int(input("enter your number"))
# sum=0   #sum isinitialised outside the loop
# for i in range(1,num+1):
#     sum=sum+i              # used to store tha vale after sum+i calc and sum is initialised outside the loop
# print(sum)


# to find factorial 5!=5*4*3*2*1
num=int(input("enter your num"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)