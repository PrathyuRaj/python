#FUNC WITH ,WITHOUT AND RETURN TYPE
#POSITIVE NEGATIVE CHECKING


def num():
    n=int(input("enter number"))
    if n<0:
        print("negative number")  #without argumnt
    else:
        print("it is positive number")
num()



def num(n):
    # n=int(input("enter number"))
    if n<0:
        print("negative number")  #with argumnt
    else:
        print("it is positive number")
num(-99)



n=int(input("enter num"))
def num(n):
    if n<0:
        return("negative number")  #without argumnt return
    else:
        return("it is positive number")
print(num(n))





