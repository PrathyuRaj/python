#Queue
# to add element operatopn =enqueue
# toremove element operation = dequeue   (to check condition queue is empty)
#FIFO order [first first in first out]


queue=[]
size=int(input("enter your queue"))
front=0
def enqueue():
    global front,size
    if front>=size:
        print("queue is full")
    else:
        e=int(input("enter the element to add"))
        queue.append(e)
        front=front+1
        print(queue)
def dequeue():
    global front,size
    if front<=0:
        print("queue is empty")
    else:
        queue.remove(queue[0])
        front=front-1
        print(queue)

while True:
    choice=int(input("enter choice \n1.enqueue \n2.dequeue"))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    else:
        print("invalid input")


