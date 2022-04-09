import re
def mailvalid(func):
    def wrapper(m,p):
        x='[\w\W]+[@][a-z]+[.][a-z]{2,3}'
        match=re.fullmatch(x,m)
        if match is not None:
            return func(m,p)
        else:
            raise Exception("mail not valid")
    return wrapper


@mailvalid
def login(mail,password):
    print("loggedin")
# mail=input("enter mail")
login("shifna@gmail.com",123)
# login(mail,123)