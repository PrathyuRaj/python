def vaccinecheck(func):
    def wrapper(a,b):
        if b>=18:
            return func(a,b)
        else:
            raise Exception("notallowed")
    return wrapper


@vaccinecheck
def vaccine(name,age):
    print(name,"vaccinated successfully")
vaccine("anu",19)