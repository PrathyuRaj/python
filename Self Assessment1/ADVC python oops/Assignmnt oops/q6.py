# to start with any number and end with a uppercase
import re
s=input("enter your string to validate")
x='^[0-9]+[a-z]+[A-Z]$'
match=re.fullmatch(x,s)
if match is not None:
    print("valid")
else:
    print("invalid")
