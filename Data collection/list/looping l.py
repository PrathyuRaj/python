# l=[1,2,3,4]
# for i in l:
#     print(i)

# l=[1,2,3,6,8,9]
# cube=[]
# for i in l:
#     i=i**3
#     cube.append(i)
# print(cube)

# l=[1,2,3,4,5,6,7]
# e=int(input("enter element"))
# if e in l:
#     print('present')
# else:
#     print('notpresent')

    # abov using for loop
def linearsearch():
    l=[1,2,3,4,5,6,7]
    e=int(input("enter element"))
    flag=0
    for i in l:
        if i==e:
            flag=1
            break
    if flag==1:
        print("present")
    else:
        print("notpresnet")
linearsearch()
