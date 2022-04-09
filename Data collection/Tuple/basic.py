# tup=1,2,3,4,5   #without brackets also tuple willl work and output will be inside brackets.
# print(tup)
# print(type(tup))
#
#
#
employees=(("anu",1,"developer",50000),
           ("akhil",2,"developer",46000),
           ("amal",3,"developer",30000))
for i in employees:
    if(i[3]>45000):
        print(i)
