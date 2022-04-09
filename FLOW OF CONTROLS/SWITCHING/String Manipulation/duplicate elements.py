# TO PRINT DUPLICATE ELEMENTS IN GIVEN INPUT


# a='appjjjjjkjkjkjkjkjkkjle'
# b=""
# c=""
# for i in a:
#     if i not in b:
#         b=b+i
#     else:
#         if i not in c:
#             c=c+i
# print(c)



# to avoid duplicated elemnts in string

# s='malayalam'
# b=""
# for i in s:
#     if i not in b:
#         b=b+i
# print(b)
# #



# FIRST RECURSIVE ELEMENT
# FIRST DUPLICATED ELEMNT

s='malayalam'
b=""
c=""
for i in s:
    if i in b:
        b=b+i
        # if i not in c:
        #     c=c+i
print(b)
