# import re
# s=input("enter your string to validate")
# x='[+][9][1]\d{10}' #or'[0-10]{10}
# match=re.fullmatch(x,s)
# if match is not None:
#     print("valid",s)
# else:
#     print("invalid")
import re
f = open("fromnumber.txt","r")
f2=open("validnumber.txt","w")
x='[+][9][1]\d{10}'
for i in f:
    id=i.rstrip("\n")
    match=re.fullmatch(x,id)
    if match is not None:
        f2.write(id)
        f2.write("\n")
