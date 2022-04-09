# def printx():
#     x=5                   #LOCAL VARIABLE :- SCOPE ONLY INSIDE FUNCTION
#     print(x)
# printx()


def printx():
    global x
    x=5                   #GLOBAL VARIABLE :- SCOPE  INSIDE AND OUTSIDE FUNCTION,
    print(x)
printx()
print(x)