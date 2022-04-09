# constructor

class Person:
    def  __init__(self,name,age1):
        self.name=name
        self.age=age1
    def printvalue(self):
        print(self.name)
        print(self.age)
pe1=Person("anu",24)
pe1.printvalue()