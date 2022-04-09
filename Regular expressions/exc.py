import re
count=0
match=re.finditer('ab',"abbaababbbba")
for i in match:
    print(i.start())
    print(i.group())      #i.group   ,i.start commands built in command python
    count=count+1
print(count)
