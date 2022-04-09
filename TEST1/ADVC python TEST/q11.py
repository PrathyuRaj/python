import re
s=input("enter string")
x='a[0-9]{5}b'
match=re.fullmatch(x,s)
if match is not None:
    print("valid")
else:
    print("invalid")
