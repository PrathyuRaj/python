# to find factorial
# 5!1*2*3*4*5  (this is factorial)
number=int(input("enter number"))
fact=1
for i in range(1,number+1) :
   fact=fact*i
print(fact)