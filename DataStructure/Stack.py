# #stack
# operations
# push- its an operation to add data  (..check conditions -check whether stack is full,when stack alrdy full elements cant be added)
# pop-  its an operation remove data  (...check conditions -check whether stack is empty,if the stack is empty pop operation cant be performed,last element should be removed first

#LIFO


stack=[]
size=int(input("enter your stack size"))
top=0
def push():
    global top,size
    if top>=size:
        print("stack is full")
    else:
        e=int(input("enter the element to add"))
        stack.append(e)
        top=top+1
        print(stack)
def pop():
    global top,size
    if top<=0:
        print("stack is empty")
    else:
        stack.pop()
        top=top-1
        print(stack)

while True:
    choice=int(input("enter choice \n1.push \n2.pop"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    else:
        print("invalid input")



