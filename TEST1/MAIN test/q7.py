# to remove abcde in user input string
s=input("enter string")
n=""
for i in s:
    if i not in "abcde":
        n=n+i
print(n)

