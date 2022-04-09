# 8 i=0
# while i<5:
#     print(i)
#     i+=1
#     if i==3:
#         break
#     else:
#         print(0)


# 9..
# x=1
# while True:
#     if x%5==0:
#         break
#     print(x)
#     x+=1


# # 10.
# n=7
# c=0
# while(n):
#     if(n>5):
#         c=c+n-1
#         n=n+1
#     else:
#         break
# print()
#
# #
# # 11
# for i in range(0,2,-1):
#     print("hello")

#12
# x=0
# a=3
# b=4
# c=5
# if a>=3:
#     if b>c:
#         x=x+3
#     elif b<c:
#         x=x+5
#     else:
#         x=x+4
# else:
#     x=x+6
# print(x,a,b,c)


# 13.
# for i in 'luminar-technolab':
#     if i=='r':
#         break
#     print(i)

# x='40'
# y=int(x)+2
# print(y)


# 14
# l=[1,2,3]
# newlist=[]    #[1,2,3,4,5]
# while l:
#     minimum=l[0]    #min=6
#     for i in l:     #i=6,8,9,4
#         if i>minimum:
#             minimum=i   #min=4
#     newlist.append(minimum)
#     l.remove(minimum)
# print(newlist)
# print("max element",newlist[-1])
# print("min element",newlist[0])


#
# num='123'
# rev=''
# for a in num:
#     rev=a+rev
# print(rev)

#
# num=[4,7,9,3,2,11,67,87,34,23,12,98,54,33]
# prime=[0]
# nonprime=[]
# newlist=[]         #[1,2,3,4,5]
# i=1
# for i in num:
#     if num>prime:
#         for i in range(1,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)



# s=input("enter")
# new=""
# e="aeiouAEIOU"
# for i in s:
#     if i not in e:
#         new=new+i
# print(new)
# i=0
# j=0
# for i in range(0,5+1):
#    for j in range(i):
#         print("*",end=" ")
# print()
# print()
num=2
a=1
k=1
for i in range(10,1,-1):
    print(end="    ")
    for j in range(i):
        print("*")
        for k in range(j):
            j=k+j
    print()
print()
print()

