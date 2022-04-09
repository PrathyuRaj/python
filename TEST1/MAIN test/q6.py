# functions with arguments with return type from range of 40-80
def sum_of_odd(r1,r2):
    sum=0
    for i in range(r1,r2+1):
        if i%2!=0:   #mam said method
            sum+=i
    return sum
print(sum_of_odd(40,80))

#
# def sumofodd(initial,final):
#     sum=0
#     while initial<=final:
#         if initial%2==1:
#             sum=sum+initial     #this too crct outpt acquired
#         initial=initial+1
#     return sum
# print(sumofodd(40,80))
#     # n=int(input("enter your num")