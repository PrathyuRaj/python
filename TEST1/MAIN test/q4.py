# to find number of a's from string from user input

# l=input("enter any word :")
# n=0
# for i in l:
#     if i=='a':   # this s also correct
#         n+=1
# print(n)

s=input("enter any word :")    #proper way  mam told
count=0
for i in s:
    if i in 'a':
        count+=1
print(count)