# *
# * *
# * * *
# * * * *
# * * * * *


# for i in range(5):   #i=0,1,2,3
#     for j in range(i):  #j=0,1,2
#         print("*",end=" ")
#     print()
#
#

#     NEXT PATTERN  reverse
# * * * * *
# * * * *
# * * *
# * *
# *




n=6
m=10
for i in range(1,n):
    for k in range(0,m):
        print(' ',end="")
    for j in range(i):
        print("*", end=" ")
    m-=2
    print()