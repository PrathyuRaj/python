#FOR SORTING IN LIST
# l=[1,2,4,6,8,7,9]
# l.sort()  #built in keyword sort used for sorting
# print(l)

l=[1,2,4,6,8,7,9]
newlist=[]
while l:
    minimum=l[0]
    for i in l:
        if i<minimum:
            minimum=i     #importnt
    newlist.append(minimum)
    l.remove(minimum)
print(newlist)













# l=[1,6,8,9,2,3,4]  #[]
# newlist=[]         #[1,2,3,4,5]
# while l:
#     minimum=l[0]    #min=6
#     for i in l:     #i=6,8,9,4
#         if i<minimum:
#             minimum=i   #min=4
#     newlist.append(minimum)
#     l.remove(minimum)
# print(newlist)


#
# l=[1,6,8,9,2,3,4]
# def binary_search():
#     list.sort()
#     e=input("enter a element to search")
#     flag=0
#     low=0
#     upper=len(list)-1
#     while lower<=upper:
#         mid=(lower+upper)//2
#         if e==list[mid]:
#             flag=1
#             break
#         elif e<list[mid]:
#             low=mid+1
#         elif e>list[mid]:
#             upper=mid-1
#     if flag==1:
#         print("element found")
#     else:
#         print("element notfound")
# print(binary_search)