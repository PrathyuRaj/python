# a='luminar techno lab'
# b=''
# for i in a:
#     b=b+i   #copy a string
# print(b)
#





# a='luminar technolab'
# b=''                               #to omit a element when copying a string
# for i in a:
#     if i not in "a":
#         b=b+i
# print(b)




a='luminar technolab'
b=''                               #to omit a element when copying a string  using continue
for i in a:
    if i=="a":
        continue
    else:
        b=b+i
print(b)



s=input("enter your element")
new_string=""
symbols="'/.,;][{}\~!@#$%^&%*()_+\|'"     #TO OMIT SYMBOLS
for i in s:
    if i not in symbols:
        new_string=new_string+i
print(new_string)

# another way
s=input("enter your element")
new_string=""
symbols="'/.,;][{}\~!@#$%^&%*()_+\|'"     #TO OMIT SYMBOLS
for i in s:
    if i not in symbols:
        new_string=new_string+i
print(new_string)
