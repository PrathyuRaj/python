# decorators
def changevalue(func):   #func=sub(n1,n2)
    def wrapper(a,b):    #a=4,b=7
        if a>=b:
            return func(a,b)
        else:
            a,b=b,a   #a=7 b=4
            return func(a,b)   #sub(7,4)
    return wrapper

@changevalue
def sub(n1,n2):
    print(n1-n2)
sub(4,7)
sub(7,4)