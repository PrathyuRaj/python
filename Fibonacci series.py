# 0 1 1 2 3 5 8 13,using while loop
n1=0
n2=1
count=0
while count<10:
    print(n1)  #0 1 1 2
    nth=n1+n2
    n1=n2    #n1=2
    n2=nth   #n2=3
    count=count+1  #3
