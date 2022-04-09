# a=[1,2,3,4]
# square=[]
# for i in a:
#     square.append(i*i)
# print(square)

# a=[1,2,3,4]
# square=[i*i for i in a]
# print(square)


# list1=[1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2]
# newlist=[i for i in list1 if i==2]    #single line code for loop is list comprehension
# print(newlist)



#PROGRAM TO FIND EVEN NUM BETWEEN 1 TO 20 USING EVEN NUMBERS

# list1=[i for i in range(1,20) if i%2==0]
# print(list1)



list_lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
newlist=[]
# common=[]
newlist=[i for i in list_lst if i!=i]
print(newlist)
