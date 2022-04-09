import re
s=input("enter any word :")
x='[A-Z]{5,10}\w'
match=re.fullmatch(x,s)
if match is not None:
    print("valid word")
else:
    print("invalid word")