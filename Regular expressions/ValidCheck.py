import re
s=input("enter your string to validate")
x='^[A-B][0-9]{5}'
match=re.fullmatch(x,s)
if match is not None:
    print("valid")
else:
    print("invalid")


    #START WITH PNE CAPITAL LETTER
    #EXACT 5 NUMBERS







#to check mobile numbr 10 digits
# import re
# s=input("enter your string to validate")
# x='\d{10}' #or'[0-10]{10}
# match=re.fullmatch(x,s)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")





# import re
# s=input("enter your string to validate")
# x='^[+][9][1][0-9]{10}'
# match=re.fullmatch(x,s)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")
#



# to check vehicle registration number
# import re
# s=input("enter your string to validate")
# x='^[K][L]\s[0-9]{2}\s[A-Z]{2}\s[0-9]{4}'
# match=re.fullmatch(x,s)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")





#starting with a ending with b

# import re
# s=input("enter string")
# x='^a[\w\W]*b$'
# match=re.fullmatch(x,s)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")







#string with numbers or capital letters

#minimum length 3 and maximum length 7

#
# import re
# s=input("enter string")
# x='[0-9][A-Z]'
# match=re.fullmatch(x,s)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")
