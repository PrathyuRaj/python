#a=abcab    #ab     is recursive element,frst duplicated elemnt
#
# s='aaaaaaabha'
# b=""
# c=""
# for i in s:
#     if i not in b:
#         b=b+i
#     else:
#         print(i)
#         break
# #

















# TO PRINT SECOND ELEMENT IN DUPLICATED ELEMENTS
a='abc'
b=""
c=""
for i in a:
    if i not in b:
        b=b+i
    elif i not in c:
        c=c+i
if c=="":
        print("no recrsive elements")
elif len(c)>1:
    print("secnd recursv element is ",c[1])
else:
    print("only one recursive element")










    # abcabd   c,or d
# to print 1 element



