min=int(input("enter your initial range"))
max=int(input("enter your final range"))
for i in range(min,max):
    if i%2==0:
        for a in range(5,0,-1):
            for j in range(a):
                print(i,end=" ")
            print()
    else:
        for a in range(1,5+1):
            for j in range(a):
                print(i,end=" ")
            print()