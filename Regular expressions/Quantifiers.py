# quantifiers

# x='a+' a including group

# x='a*' count including zero number of a

# x='a?' count a as each including zero no of a

# x='a{2} 2 no of a position

# x='a{2,3} minimum 2 a and maximum 3 a

# x=¹^a' check starting with a

# x='a$' check ending with a











import re
x='a+'
match=re.finditer(x,"aa bb cc saab@ghff")   #+ to check group  (min count1 position
for i in match:
    print(i.start())
    print(i.group())





import re
x='a*'
match=re.finditer(x,"aa bb cc saab@ghff")   #* to check group  (min count0 position
for i in match:
    print(i.start())
    print(i.group())


import re
x='a?'
match=re.finditer(x,"aa bb cc saab@ghff")   #? to validate position wise
for i in match:
    print(i.start())
    print(i.group())



import re
x='a{2,4}'
match=re.finditer(x,"a aa bb aaa cc saaaaaaab@ghff")
for i in match:
    print(i.start())
    print(i.group())



import re
x='^a'   #to check starts with a
match=re.finditer(x,"a aa bb aaa cc saaaaaaab@ghff")   #
for i in match:
    print(i.start())
    print(i.group())


import re
x='^[^abc]'   #to check starts with except abc
match=re.finditer(x,"a aa bb aaa cc saaaaaaab@ghff")   #
for i in match:
    print(i.start())
    print(i.group())


import re
x='a$'  #to check ending with a
match=re.finditer(x,"a aa bb aaa cc saaaaaaab@ghffa")   #
for i in match:
    print(i.start())
    print(i.group())