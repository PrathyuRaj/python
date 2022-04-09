s=input("enter string")
new=""
e="aeiouAEIOU"
for i in s:
    if i not in e:
        new=new+i
print(new)