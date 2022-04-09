initial=int(input("enter ur initial"))
final=int(input("enter ur final range"))
i=1
for num in range(initial,final+1):
    if num>0:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)