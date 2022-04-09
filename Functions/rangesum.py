def rangesum(initial,final):
    sum=0
    while initial<=final:
        if initial%2==0:
            sum=sum+initial
        initial=initial+1
    return sum
print(rangesum(1,10))
    # n=int(input("enter your num")