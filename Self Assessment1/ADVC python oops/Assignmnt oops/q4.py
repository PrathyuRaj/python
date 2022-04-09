class Pet:
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def printvalue(self):
        print(self.name,self.type)
class Cat(Pet):
    def __init__(self,color,age,name,type):
        super().__init__(name,type)
        self.color=color
        self.age=age
    def printvalue(self):
        print(self.color,self.age,self.name,self.type)
pe=Cat("black",5,"leo","Persian")
pe.printvalue()

