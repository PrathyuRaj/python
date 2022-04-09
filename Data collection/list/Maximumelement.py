l=[2,3,6,9,4,5]
newlist=[]         #[1,2,3,4,5]
while l:
    minimum=l[0]    #min=6
    for i in l:     #i=6,8,9,4
        if i<minimum:
            minimum=i   #min=4
    newlist.append(minimum)
    l.remove(minimum)
print(newlist)
print("max element",newlist[-1])
print("min element",newlist[0])