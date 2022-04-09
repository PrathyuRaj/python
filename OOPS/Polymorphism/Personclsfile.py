class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printpers(self):
        print(self.name,self.age)
f=open("person.txt",'r')
for i in f:
    data=i.rstrip("\n").split(",")
    name=data[0]
    age=data[1]
    pe=Person(name,age)
    pe.printpers()
