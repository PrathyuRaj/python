# recursion? giv exmpl
#function can call itself is recurssion
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))