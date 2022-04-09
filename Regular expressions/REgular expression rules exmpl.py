# import re
# x='[abc]'
# match=re.finditer(x,"hello ab@ghff")     #to chck abc
# for i in match:
#     print(i.start())
#     print(i.group())
#
#
#
#
#
# import re
# x='[^abc]'       #TO NOT CHCK ABC
# match=re.finditer(x,"hello ab@ghff")
# for i in match:
#     print(i.start())
#     print(i.group())
#
#
#
#
#
#
# import re
# x='[^a-z]'       #TO NOT CHCK small letters
# match=re.finditer(x,"hello ab@ghff")
# for i in match:
#     print(i.start())
#     print(i.group())
#
#
#

#
# import re
# x='[^A-Z0-9a-z]'
# match=re.finditer(x,"hello 123 ab@ghff")
# for i in match:
#     print(i.start())
#     print(i.group())




# import re
# x='\D'
# match=re.finditer(x,"hello 123 ab@ghff")     #except digits [ 'd' only digits]
# for i in match:
#     print(i.start())
#     print(i.group())




# import re
# x='\w'
# match=re.finditer(x,"hello 123 ab@ghff")    #'\w'no special chrcts
# for i in match:
#     print(i.start())
#     print(i.group())



import re
x='[\s\d]'
match=re.finditer(x,"hello 123 ab@ghff")
for i in match:       #\s=to check spaces     #\d=to check numbers
    print(i.start())
    print(i.group())