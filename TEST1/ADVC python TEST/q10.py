import re
s=input("enter word")
x='[A-Z][a-z]+\W+'
match=re.fullmatch(x,s)
if match is not None:
    print("valid word")
else:
    print("invalid word")